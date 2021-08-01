#-*- coding: utf-8 -*-


def get_rating(list_of_ip):
    """
    Функция принимает список IP-адресов из лог-файла access.log, с которых совершались запросы на сервер.
    Возвращает словарь вида {"IP-адрес": количество вхождений в список (==количество запросов)}

    """
    origin_ip_list = list(set(list_of_ip))
    rating = dict()
    for i in origin_ip_list:
        rating.update({i:list_of_ip.count(i)})
    return rating