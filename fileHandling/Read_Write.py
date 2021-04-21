#-*- coding: utf-8 -*-
import os

#wr = open(os.getcwd()+r"\newfile.txt", 'w', encoding="utf-8")
#wr.write("Once upon a time...\n")
#wr.close()
f = open(os.getcwd()+r"\newfile.txt", 'w', encoding="utf-8")        #на этом этапе создаётся пустой файл
                                                                    # os.getcwd() - текущий рабочий каталог
first = "Однажды в студёную зимнюю пору\n"
second = "Я из лесу вышел."
third = "Был сильный мороз..."
f.writelines([first, second, third])        #запись идёт в одну строку, если нет символа \n
f.close()
