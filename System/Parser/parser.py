import re

class Parser(object):

    def __init__(self, tokens, mem, error_line):
        self.tokens = tokens
        self.token_index = 0
        self.variables = {}
        self.mem = mem
        self.error_line = error_line

    def parse(self):

        while self.token_index < len(self.tokens):

            type = self.tokens[self.token_index][0]
            value = self.tokens[self.token_index][1]

            if type == 'var_declare' and value == 'var':
                self.var(self.tokens[self.token_index:])
            elif type == 'output' and value == 'console':
                self.console(self.tokens[self.token_index + 1:self.token_index + 3])
            self.token_index += 1

    def console(self, value):
        if value[1][1] != ';':
            print("Используйте ';' в конце строки")
            print(f"Строка {self.error_line}")
            quit()
        else:
            if value[0][0] == 'var_ident':
                if value[0][1] in self.mem.save_vars.keys():
                    print(self.mem.save_vars[value[0][1]])
                else:
                    print(f'Переменная {value[0][1]} не объявлена')
                    print(f'В строке {self.error_line}')
                    quit()
            else:
                print(value[0][1])

    
    def var(self, tokens_list):
        lst = tokens_list[:-1]
        tok_dict = {
            0 : 'var_declare',
            1 : 'var_ident',
            2 : 'assignment'
        }

        for i in tok_dict.keys():
            if lst[i][0] != tok_dict[i]:
                print(f'Ошибка в {tok_dict[i]}')
                quit()

        to_eval_string = ''

        for j in range(3, len(lst)):
            if lst[j][0] == 'var_ident':
                # var_value = self.variables[lst[j][1]]
                if '(' in lst[j][1]:
                    var_value = self.mem.save_vars[lst[j][1][1:]]
                    to_eval_string += '(' + str(var_value)
                elif ')' in lst[j][1]:
                    var_value = self.mem.save_vars[lst[j][1][:-1]]
                    to_eval_string += str(var_value) + ')'
                else:
                    var_value = self.mem.save_vars[lst[j][1]]
                    to_eval_string += str(var_value)
            elif lst[j][0] == 'input':
                to_eval_string = input()
            else:
                to_eval_string += str(lst[j][1])
        if '(' in lst[1][1] and ')' in lst[1][1]:
            s = lst[1][1].find('(')
            e = lst[1][1].find(')')
            brackets_eval = eval(lst[1][1][s:e+1])
            to_eval_string = to_eval_string[:s] + str(brackets_eval) + to_eval_string[e:]
            self.mem.save(lst[1][1], eval(to_eval_string))
        else:
            # print(to_eval_string)
            self.mem.save(lst[1][1], eval(to_eval_string))
            # self.variables[lst[1][1]] = eval(to_eval_string)

