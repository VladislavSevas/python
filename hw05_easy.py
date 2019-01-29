# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import sys
import os
import shutil


def namedir():
    return[os.path.join(os.getcwd(), 'папка' +str(i)) for i in range(1, 10)]
    
def newdir():
    newd = namedir()
    for i in newd:
        try:
            os.mkdir(i)
            print(os.path.basename('{} создана'.format(i)))
        except FileNotFoundError:
            print('папка уже создана')

           
def deldir():
    deld = namedir()
    for i in deld:
        try:
            os.rmdir(i)
            print(os.path.basename('{} удалена'.format(i)))
        except FileNotFoundError:
            print('такой папки нет')

def seedir():
    print(os.listdir(os.getcwd()))

def selfcopy():
    src = os.path.realpath(__file__)
    dst = os.path.join(os.getcwd(), 'копия 1.py')
    print('Сделал копию {}'.format(shutil.copy (src, dst)))


if __name__ == '__main__':
    while True:
        key = input('Введите ключ:\n'
                    '1 - создать новые папки\n'
                    '2 - удалить вновь созданные папки\n'
                    '3 - посмотреть содержимое текущей директории\n'
                    '4 - создать копию исходного файла\n'
                    'q - выйти из программы\n')
        if key == 'q':
            sys.exit()
        elif key == '1':
            newdir()
        elif key == '2':
            deldir()
        elif key == '3':
            seedir()
        elif key == '4':
            selfcopy()
        else:
            print('Неизвестная команда')
          
