import re

class Parser(object):

<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, mem, error_line):
=======
    def __init__(self, tokens, mem, error_line):
        self.tokens = tokens
        self.token_index = 0
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
=======
    def __init__(self, tokens, mem, error_line):
        self.tokens = tokens
        self.token_index = 0
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
        self.variables = {}
        self.mem = mem
        self.error_line = error_line

<<<<<<< HEAD
<<<<<<< HEAD
    def parse(self, tokens):
        self.token_index = 0
        self.tokens = tokens
=======
    def parse(self):

>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
=======
    def parse(self):

>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
        while self.token_index < len(self.tokens):

            type = self.tokens[self.token_index][0]
            value = self.tokens[self.token_index][1]

<<<<<<< HEAD
<<<<<<< HEAD
            if type == 'var_declare' and value == 'var' and self.mem.if_was == False:
                self.var(self.tokens[self.token_index:])
            elif type == 'output' and value == 'console' and self.mem.if_was == False:
                self.console(self.tokens[self.token_index + 1:])
            elif type == 'if' and value == 'trigger':
                self.trigger(self.tokens[self.token_index:])
            elif self.mem.if_was == True:
                self.trigger(self.tokens[self.token_index:])
=======
=======
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
            if type == 'var_declare' and value == 'var':
                self.var(self.tokens[self.token_index:])
            elif type == 'output' and value == 'console':
                self.console(self.tokens[self.token_index + 1:self.token_index + 3])
<<<<<<< HEAD
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
=======
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
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
<<<<<<< HEAD
<<<<<<< HEAD
        self.token_index += 2
=======
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
=======
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579

    
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
<<<<<<< HEAD
<<<<<<< HEAD
                var = re.search(r'[a-zA-Z]+', lst[j][1])[0]
                var_val = self.mem.save_vars[var]
                to_eval_string += lst[j][1].replace(var, str(var_val))
=======
=======
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
                if '(' in lst[j][1]:
                    var_value = self.mem.save_vars[lst[j][1][1:]]
                    to_eval_string += '(' + str(var_value)
                elif ')' in lst[j][1]:
                    var_value = self.mem.save_vars[lst[j][1][:-1]]
                    to_eval_string += str(var_value) + ')'
                else:
                    var_value = self.mem.save_vars[lst[j][1]]
                    to_eval_string += str(var_value)
<<<<<<< HEAD
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
=======
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
            elif lst[j][0] == 'input':
                to_eval_string = input()
            else:
                to_eval_string += str(lst[j][1])
<<<<<<< HEAD
<<<<<<< HEAD

        self.mem.save(lst[1][1], eval(to_eval_string))
        self.token_index += len(lst)
            # self.variables[lst[1][1]] = eval(to_eval_string)


    def trigger(self, tokens_list):
        log_app = ''
        self.token_index += len(tokens_list)
        if self.mem.if_was == False:
            self.mem.save_start(True)
            for i in range(1, len(tokens_list)):
                if tokens_list[i][0] == 'var_ident':
                    var = re.search(r'[a-zA-Z]+', tokens_list[i][1])[0]
                    var_val = self.mem.save_vars[var]
                    log_app += tokens_list[i][1].replace(var, str(var_val))
                elif tokens_list[i][0] == 'start_func':
                    break
                else:
                    log_app += tokens_list[i][1]

            self.mem.if_save(True)
            self.mem.save_condition(log_app)
        else:
            if tokens_list[0][0] != 'end_func' and self.mem.start:
                # print(tokens_list)
                if self.mem.true_condition != None:
                    self.mem.append_true_commands(tokens_list)
                else:
                    self.mem.true_condition = tokens_list
            else:
                if self.mem.condition:
                    self.mem.if_save(False)
                    # print('True')
                    # print(self.mem.true_condition)
                    self.parse(self.mem.true_condition)
=======
=======
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
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

<<<<<<< HEAD
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
=======
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
