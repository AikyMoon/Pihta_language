# импортируем классы для языка 
import os
from System.Lexer import *
from System.Parser import *
from System.Memory import *

# создаем класс для компилирования
class Compiler(object):
    # имя файла, который будет компилироваться
    def __init__(self, filename):
        self.compile(filename)
    # создаем медот для компиляции
    def compile(self, filename):
        # проверяем расширение
        if os.path.splitext(filename)[-1] == '.fir':
            # есть ли такой файл
            if os.path.exists(filename):
                # создаем объект класса-памяти
                memory = Memory()
                # открываем файл
                with open(filename, 'r') as f:
                    error = 0
                    # считываем каждую строку
                    for line in f:
                        error += 1
                        # создаем объект класса для токенизирования и подаем нашу строку
                        lex = Lexer(line.strip('\n'))
                        # выполняем токенизацию
                        tokens = lex.tokenize(error)
                        # создаем объект класса для парсинга
                        parser = Parser(tokens, memory, error)
                        # парсим
                        parser.parse()

            else:
                print(f'Нет файла {filename} в дериктории или указан неполный путь')
                quit()
        else:
            print(f'Язык Пихта не имеет расширения {os.path.splitext(filename)[-1]}')
            quit()