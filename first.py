import requests
import time
import os
from operator import itemgetter
from datetime import datetime

def get_values():
    f = open('values.txt', 'a')
    image = requests.get('https://csfail.live/api/crash/games/history')
    r = image.json()
    for a in r["data"]["games"]:
        f.write(str(a['id']))
        f.write(' ')
        f.write(str(a['createdAt'][8:-13]))
        f.write(' ')
        f.write(str(a['crashedAt']))
        f.write('\n')
    f.close()

def delete_unnecessary():
    f = open('values.txt', 'r+')
    b = f.readlines() #список со значениями
    a = [] # список с удаленным \n
    c = [] # список без повторяющихся значений
    for i in b: # удаление \n в конце
        i = i.split(" ")
        j = i[2].replace('\n', '')
        i.pop()
        i.append(j)
        a.append(i)
    for i in a:
        if i not in c:
            c.append(i)
    f.close()
    os.remove('values.txt') # удаляем старый файл
    f = open('values.txt', 'w+') # создаем файл уже с новыми значениями
    c = sorted(c, reverse=True)
    for i in c:
        f.write(str(i[0]))
        f.write(' ')
        f.write(str(i[1]))
        f.write(' ')
        f.write(str(i[2]))
        f.write('\n')
    f.close()


while True:
    print(datetime.now())
    get_values()
    delete_unnecessary()
    time.sleep(1200)
    

