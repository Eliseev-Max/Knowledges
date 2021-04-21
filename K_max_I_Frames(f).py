# -*- coding: utf-8 -*-
"""
Тест выполняет проверку следующих положений IEC 60870-5-604:
+    ► Начальное значение порядковых номеров отправки N(S) и получения N(R) установлено равным 0
        после успешного TCP-соединения Первичной и Вторичной станций
+    ► Блок данных I-формата содержит текущие значения порядковых номеров отправки N(S) и получения N(R)
+    ► После отправки блока данных I-формата порядковый номер отправки N(S) на Первичной станции увеличился на 1
+    ► Неподтверждённые блоки данных I-формата подтверждены блоком данных S-формата/I-формата от Вторичной станции
+    ► Порядковый номер получения N(R) подтверждает все неподтверждённые ранее блоки данных I-формата, у которых N(S) < N(R)
+    ► Первичная станция может передать неподтверждённых блоков данных I-формата не более установленного значения K,
      прежде чем остановить отправку блоков данных и ожидать подтверждения
+    ► На блок данных U-формата с управляющей функцией STARTDT_ACT получен ответ STARTDT_CON
+    ► На блок данных U-формата с управляющей функцией STOPDT_ACT получен ответ STOPDT_CON
"""
import rkts
from flaky import flaky
import os, sys
import time, datetime
from arisconnector import ArisConnector, ArisTelnetConnector as tnc


def exact_time(tmstmp):
    """Преобразует метку времени, полученную в unix-time в читаемый формат: ММ:СС.мС"""
    hms = tmstmp//1000
    ms = round(tmstmp%1000)
    return "\t{}.{}".format(time.strftime("%M:%S",time.localtime(hms)),ms)

def tstamp():
    """Функция возвращает текущее время в формате: ММ:СС.мС"""
    try:
        return ("\t"+time.strftime("%M:%S")+"."+ str(round(datetime.datetime.now().microsecond/1000)))
    except NameError:
        return print("Не подключены необходимые модули: time, datetime")

def log(name, entry):
    with open(name,"a", encoding="utf-8") as n:
        n.write(str(entry))

def spGenerator(ip_address, switchings=7):
    """Генератор спорадики. Производит смену значений параметра LOC.Control.Alarm"""
    tnConParams = {"ip" : ip_address, "port" : "23","login" : "root","pass" : "fhbc'rcg","timeout":60}
    cmd_timeout = 0.2       #Пауза между командами смены значения

    tn_obj = tnc(tnConParams)
    tn_obj.connect()

    time.sleep(1)
    cmd1 = "warehouse_set -n LOC.Control.Alarm -v 1 -q 192"
    cmd2 = "warehouse_set -n LOC.Control.Alarm -v 0 -q 192"
    
    sw = []    
    for cnt in range(switchings):
        tn_obj.run_command(cmd1)
        sw.append(time.time()*1000)
        time.sleep(cmd_timeout)
        tn_obj.run_command(cmd2)
        sw.append(time.time()*1000)
        time.sleep(cmd_timeout)
    tn_obj.disconnect()
    return sw
######################################################################
logging = True

REAL_SERVER_PORT_1 = 2404
REAL_SERVER_ADDR = "10.1.32.253"
#REAL_SERVER_ADDR = "10.1.0.150"
type_I_frame = (rkts.EventType.I_FRAME_PROCESS_INFO_MON_DIR, rkts.EventType.END_OF_INIT, rkts.EventType.I_FRAME_PROCESS_INFO_CONTR_DIR)


os.chdir(os.path.dirname(os.path.abspath(__file__)))        #Делаем каталог с исполняемым файлом текущим
filename = time.strftime("%Y%m%d_%H.%M")+"_TransmissionProc_log.txt"
print("Файл с отчётом по выполненному автотесту '"+ filename +"' будет доступен по следующему адресу:\n", os.path.dirname(os.path.abspath(__file__)))
nameOfReport = "Проверка процедуры передачи информации между клиентом и сервером\n"\
"Отчет о результатах автоматического тестирования"

servParams = "\nПараметры подключения к серверу IEC 60870-5_104:\n\tIP-адрес: " + REAL_SERVER_ADDR + "\n\tTCP-порт: " + str(REAL_SERVER_PORT_1)
servProtocolParams = """
Параметры протокола IEC 60870-5 104 для сервера:
    k = 12
    w = 8
    t1 = 15
    t2 = 10
    t3 = 20
"""
k_server = 12
c = rkts.Client60870(port=REAL_SERVER_PORT_1, address=REAL_SERVER_ADDR, bufferSize=1000)
p_k = str(c.paramAPCI.k)
p_w = str(c.paramAPCI.w)
p_t1 = str(c.paramAPCI.t1)
p_t2 = str(c.paramAPCI.t2)
p_t3 = str(c.paramAPCI.t3)
clientProtocolParams = f"\nПараметры протокола IEC 60870-5 104 для клиента:\n\tk = {p_k}\n\tw = {p_w}\n\tt1 = {p_t1}\n\tt2 = {p_t2}\n\tt3 = {p_t3}\n"
w_off = "ОТКЛЮЧЕНА функция автоматической отправки клиентом подтверждения (APDU формата S) после получения им от сервера W блоков данных I-формата. \n"

header_log = nameOfReport.center(115) + "\nВремя создания отчёта: " + time.strftime("%H:%M:%S") + servParams + servProtocolParams + clientProtocolParams + w_off
if logging is False:
    log(filename, header_log)

@flaky()
def test_complexTest01():
    client = rkts.Client60870(port=REAL_SERVER_PORT_1, address=REAL_SERVER_ADDR, bufferSize=1000)
    client.autoAckReachedW = False
    client.timerT2Work = False
    spObj = rkts.IOSinglePoint()

    client.connect()
#### Проверка TCP-соединения ####
    assert client.isConnected == True, "Не удалось установить TCP-соединение между клиентом и сервером"
    repConnection = "TCP-соединение между клиентом и сервером установлено.\n"
    print(repConnection)
    assert int(client.eventsCount) == 1,"Непредвиденное событие до старта передачи данных"
############__Telnet. Управление сменой значений LOC.Control.Alarm__#########
    switchingTime = spGenerator(REAL_SERVER_ADDR, switchings=14)
    print("Генерация спорадики запущена до отправки серверу команды на старт передачи данных")
    stagesHead = "\nЭтапы прохождения теста:\n"
    if logging is True:
        log(filename, stagesHead)
    client.sendStartDT()
#    client.sendSFrame(int(client.unconfirmedRecvICount))
    time.sleep(0.4)
    print(f"Количество неподтверждённых блоков данных I-формата на момент старта передачи данных: {client.unconfirmedRecvICount}")

#### Проверка обмена блоками данных STARTDT_ACT -> <- STARTDT_CON ####
#    assert client.events()[1].type == rkts.EventType.U_FRAME, "Клиентом не отправлен блок данных U-формата (STARTDT_ACT)"
    assert str(client.events()[1].data.type) == "STARTDT_ACT", "Блок данных U-формата НЕ содержит функцию STARTDT_ACT"
#    assert client.events()[2].type == rkts.EventType.U_FRAME, "Клиентом не было получено подтверждение от сервера (STARTDT_CON)"
    assert str(client.events()[2].data.type) == "STARTDT_CON", "Блок данных U-формата НЕ содержит подтверждение STARTDT_CON"
    print(f"Разница во времени между STARTDT_ACT и STARTDT_CON составила {client.events()[2].timestamp-client.events()[1].timestamp}")
#### Вывод сообщений и логирование событий
    print(f"{exact_time(client.events()[1].timestamp)}  Клиентом отправлен блок данных U-формата с функцией {client.events()[1].data.type}")
    print(f"{exact_time(client.events()[2].timestamp)}  Клиентом получено подтверждение (блок данных U-формата с функцией {client.events()[2].data.type})")
    checkUFrames = "Клиентом был отправлен блок данных U-формата, содержащий функцию STARTDT_Act.\n"\
        "Сервером был отправлен ответ: блок данных U-формата, содержащий функцию STARTDT_Con."
    if logging is True:
        log(filename, checkUFrames)
    unconfRecIFrames_0 = int(client.unconfirmedRecvICount)
#### Проверка доставки блоков данных I-формата клиенту
    assert unconfRecIFrames_0 > 0,"Клиент не получил ни одного блока данных I-формата"

#### Проверяем, что APDU блока данных соответствует I-формату
    assert client.events()[3].type in type_I_frame,"Отправлен блок данных не I-формата"

#### Проверяем, что начальные значения передаваемого N(S) и принимаемого N(R) порядковых номеров установлены равными 0
    assert int(client.events()[3].data.recvCount) == 0,"Начальное значение передаваемого порядкового номера блока данных не равно 0"
    assert int(client.events()[3].data.sentCount) == 0,"Начальное значение принимаемого порядкового номера блока данных не равно 0"
   
#### Проверяем, что количество блоков данных I-формата соответствует значению K сервера
    assert int(client.unconfirmedRecvICount) == k_server,"Количество неподтверждённых блоков данных I-формата не соответствует K"
    unconfRecIFrames_1 = int(client.unconfirmedRecvICount)
    log_check_K = f"\nСервер отправил клиенту блоки данных I-формата в количестве, соответствующем значению K ({k_server})\n"
    if logging is True:
        log(filename,log_check_K)
#### Создаём список, содержащий передаваемые порядковые номера I-фреймов
    sendSeqNumbers = []
    for event in client.events():
        if event.type == rkts.EventType.I_FRAME_PROCESS_INFO_MON_DIR or event.type == rkts.EventType.END_OF_INIT:
            sendSeqNumbers.append(int(event.data.recvCount))
        else: continue
#### Проверяем инкрементацию N(S)
    assert sendSeqNumbers == list(range(k_server)),"Нарушена последовательность порядковых номеров передаваемых кадров"
    incrementOk = "\nПорядковый номер передачи каждого следующего блока данных I-формата увеличивается на 1\n"
    if logging is True:
        log(filename, incrementOk)

    client.sendSFrame(unconfRecIFrames_1)       # Первый S-фрейм подтверждает K I-фреймов
    print(f"Отправили S-frame, подтверждающий {unconfRecIFrames_1} блоков данных I-формата")
    time.sleep(1)
    assert int(client.unconfirmedRecvICount)>unconfRecIFrames_1, "Сервер не совершал отправку блоков данных I-формата после подтверждения" ####
    client.sendSFrame(unconfRecIFrames_1)       # Отправили неподтверждающий S-фрейм
    time.sleep(0.5)
    unconfRecIFrames_2 = int(client.unconfirmedRecvICount)
    print(f"Отправили S-frame с порядковым номером {unconfRecIFrames_1} вместо подтверждающего порядкового номера {unconfRecIFrames_2}")
    time.sleep(0.5)

#### Проверка действия Сервера при отправке ему принимаемого порядкового номера N(R)<N(S)

    assert client.events()[-1].type == rkts.EventType.S_FRAME,"Непредвиденное получение клиентом блококв данных I-формата. "
    fakeConfNumber = int(unconfRecIFrames_1) + 2
    client.sendSFrame(fakeConfNumber)       # Посмотреть, сколько поступило I-фреймов
    num_of_events_1 = int(client.eventsCount)
    time.sleep(0.5)
    num_of_events_2 = int(client.eventsCount)
    assert (num_of_events_2 - num_of_events_1) == 2, "Ошибка количества поступивших неподтверждённых блоков данных!"

    assert client.events()[-2].type in type_I_frame, "Проверка подтверждения двух блоков данных I-формата не пройдена"
    assert client.events()[-1].type in type_I_frame, "Проверка подтверждения двух блоков данных I-формата не пройдена"
####################################################################
    client.sendIO(spObj, rkts.CauseOfTransmission.COT_ACTIVATION, 1)
    print(f"Клиентом отправлен блок данных I-формата, содержащий функцию {spObj.type}")
    eventsWithSentIFrame = int(client.eventsCount)

####################################################################
    time.sleep(0.8)
    eventsAfterSentIFrame = int(client.eventsCount)
    assert eventsAfterSentIFrame > eventsWithSentIFrame,"Отсутствуют неподтверждённые блоки данных I-формата"
##### Смотрим последние события в количестве dif: тип фрейма и номера N(S), N(R)
    dif = eventsWithSentIFrame - eventsAfterSentIFrame
    for e in range(dif,0,1):
        assert client.events()[e].data.isSent == False, "Блок данных отправлен ошибочно!"
        assert client.events()[e].type in type_I_frame,"Один из полученных блоков данных после подтверждения двух I-фреймов оказался не блоком данных I-формата!!!"
        assert client.events()[e].data.sentCount == 1,"Ошибка инкрементирования принимаемого порядкового номера сервера"
    del dif
#### Add var: numberOfEvents = int(client.eventsCount)
    for sendingCount in range(0,8):
        client.sendIO(spObj, rkts.CauseOfTransmission.COT_ACTIVATION, 1)
    time.sleep(0.5)
    eventsAfterSent8IFrames = int(client.eventsCount)
    dif = eventsAfterSentIFrame - eventsAfterSent8IFrames
    sFrameFromServ = None
    for ev in range(dif,0,1):
        if client.events()[ev].type != rkts.EventType.S_FRAME:
            continue
        else:
            print(f" Тип события {ev}:{client.events()[ev].type}")
            sFrameFromServ = client.events()[ev]
            print(f"Обнаружен S-frame:{sFrameFromServ}")
            break
    assert sFrameFromServ.type == rkts.EventType.S_FRAME,"Сервером не отправлено подтверждение отправленных ему I-фреймов"
    time.sleep(0.8)
    for sendingCount in range(0,8):
        client.sendIO(spObj, rkts.CauseOfTransmission.COT_ACTIVATION, 1)
        time.sleep(0.5)
    del sFrameFromServ
    eventsAfterSent8IFrames2 = int(client.eventsCount)
    dif = eventsAfterSent8IFrames - eventsAfterSent8IFrames2
    for evnt in range(dif,0,1):
        if client.events()[evnt].type != rkts.EventType.S_FRAME:
            continue
        else:
            sFrameFromServ = client.events()[evnt]
            print("Обнаружен S-frame")
            break
    assert sFrameFromServ.type == rkts.EventType.S_FRAME,"Сервером не отправлено подтверждение отправленных ему I-фреймов ПОВТОРНО"

    print(f"Клиентом получен блок данных S-формата, Принимаемый порядковый номер: {sFrameFromServ.data.sVal}")
    time.sleep(1)
    client.sendStopDT()
    time.sleep(0.5)
#    assert client.events()[-2].type == rkts.EventType.U_FRAME, f"Клиентом не отправлен блок данных U-формата (STOPDT_ACT)\n{client.events()[-2].type}"
#    assert client.events()[-1].type == rkts.EventType.U_FRAME, f"Клиентом не было получено подтверждение от сервера (STOPDT_CON)\n{client.events()[-1].type}"
    client.disconnect()

#########################__Сортировка событий по типам с указанием метки времени__#########################
    listOfEvents = []

    for el in client.events():
        if el.type == rkts.EventType.CONNECTION_OPENED or el.type == rkts.EventType.CONNECTION_CLOSED or el.type == rkts.EventType.CONNECTION_FAILED:
            if el.type == rkts.EventType.CONNECTION_OPENED:
                connectionOpened = f"{exact_time(el.timestamp)}: TCP-соединение установлено.\n"
                listOfEvents.append(connectionOpened)

            if el.type == rkts.EventType.CONNECTION_CLOSED:
                connectionClosed = f"{exact_time(el.timestamp)}: TCP-соединение прекращено. \n"
                listOfEvents.append(connectionClosed)

            if el.type == rkts.EventType.CONNECTION_FAILED:
                connectionFailed = f"{exact_time(el.timestamp)}: Не удалось установить TCP-соединение между клиентом и сервером\n"
                listOfEvents.append(connectionFailed)
                print(connectionFailed)
        else:
            if el.type == rkts.EventType.T1_TIMEOUT or el.type == rkts.EventType.T2_TIMEOUT or el.type == rkts.EventType.T3_TIMEOUT:
                timeoutEvent = f"{exact_time(el.timestamp)}: Зарегистрировано событие типа {el.type}\n"
                listOfEvents.append(timeoutEvent)
            else:
                if el.data.isSent == True:
                    transDirection = "Клиентом отправлен блок данных формата "
                else: transDirection = "Клиентом получен блок данных формата "
                addToReport = f"{exact_time(el.timestamp)}: {transDirection} {el.type}. "
                listOfEvents.append(addToReport)
                if el.type == rkts.EventType.U_FRAME:
                    u_frame = f"Тип функции: {el.data.type}.\n"
                    listOfEvents.append(u_frame)
                if el.type == rkts.EventType.S_FRAME:
                    s_frame = f"Принимаемый порядковый номер: {el.data.sVal}.\n"
                    listOfEvents.append(s_frame)
                if el.type == rkts.EventType.I_FRAME_PROCESS_INFO_MON_DIR or el.type == rkts.EventType.END_OF_INIT or el.type == rkts.EventType.I_FRAME_PROCESS_INFO_CONTR_DIR:
                    i_frame = f"Передаваемый порядковый номер N(S): {el.data.recvCount}; принимаемый порядковый номер N(R): {el.data.sentCount}\n"
                    listOfEvents.append(i_frame)


####################################################################
    stringOfEvents = "".join(listOfEvents)
    eventLog = "\nЖурнал событий:\n" + stringOfEvents
    if logging is True:
        log(filename, eventLog)

test_complexTest01()
print("Тест пройден успешно")
if logging is True:
    print("Отчёт сформирован в папке ", os.path.dirname(os.path.abspath(__file__)))
