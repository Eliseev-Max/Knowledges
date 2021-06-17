import time
import datetime
import random
"""
Синтаксис datetime.date() 
datetime.date(year, month, day)
В случае ошибки (некорректно задан день, месяц...) возбуждается ValueError
Формат номера месяца - без 0
"""
print("о чём говорит тебе эта дата? ",datetime.date(2020,1,17))
sd = datetime.date(2020,2,21)
print("Год: ",sd.year,"\nМесяц: ",sd.month,"\nДата: ",sd.day)

#Сегодняшний день
print("Сегодня ",datetime.date.today())
dt = datetime.datetime(1989,3,26,16,40,5)
#Если не передать аргументы, возбудится исключение:
#TypeError: function missing required argument ...
#Часы, минуты и секунды в формате без 0 впереди
print(dt)

#Два разных метода datetime.datetime()
#Разница:
# today() - возвращает текущие дату и время, не принимает параметров
# now([<Зона>]) - возвращает текущие дату и время. Если параметр не задан, now() === today()
m1 = datetime.datetime.today()
m2 = datetime.datetime.now()
print("First method 'today()' ",m1,"\nSecond method 'now()' ", m2)

#Модуль datetime содержит другой метод, под названием strftime

a = datetime.datetime.today().strftime("%Y%m%d")
print(a) # '20170405'
 
today = datetime.datetime.today()
print( today.strftime("%m/%d/%Y") ) # '04/05/2017'
 
print( today.strftime("%Y-%m-%d-%H.%M.%S") ) # 2017-04-05-00.18.00

#разница между двумя датами:
now = datetime.datetime.now()
ryear = random.randrange(2000,2022)
rmonth = random.randrange(1,13)
rday = random.randrange(1,30)
rhour = random.randrange(24)
rmin = random.randrange(60)
rsec = random.randrange(60)
then = datetime.datetime(ryear, rmonth, rday, rhour, rmin, rsec)
delta = now - then
print(then)
print(delta.days, delta.seconds, sep="\n")
seconds = delta.total_seconds()
print("method total_seconds()", seconds)

# Текущее время
cur_time = time.time()
print("time.time() = ", cur_time,"\ntime.ctime(time.time())" ,time.ctime(cur_time))
