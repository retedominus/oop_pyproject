import view as v
import calc_model as cm
from exception import Except


class Menu:
    options = {1: 'Сложение', 2: 'Вычитание', 3: 'Умножение', 4: 'Деление', 5: 'Выход'}

    def __init__(self):
        pass

    def calc(self):
        choose = self.get_operation()
        if choose == 1:
            return cm.SumModel(self.get_value(), self.get_value()).result
        if choose == 2:
            return cm.SubModel(self.get_value(), self.get_value()).result
        if choose == 3:
            return cm.MultModel(self.get_value(), self.get_value()).result
        if choose == 4:
            return cm.DivModel(self.get_value(), self.get_value()).result
        else:
            return None

    def get_operation(self):
        print('Выберите пункт меню: \n')
        v.View.show_options(self.options)
        operation = input()
        while not operation.isdigit() or int(operation) not in self.options.keys():
            print('Указан неверный пункт меню!')
            operation = input('Выберите пункт меню: ')
        return int(operation)

    @staticmethod
    def get_value():
        value = Except.check_number(input("Введите рациональное число: "))
        while not value:
            print("Вы ввели недопустимое значение")
            value = Except.check_number(input("Введите рациональное число: "))
        return float(value)

    def button_clic(self):
        v.View.show_title("\nДобро пожаловать в калькулятор."
                          "\nЯ могу выполнять операции с рациональными числами.\n")
        brake = False
        while not brake:
            result = self.calc()
            if result is None:
                brake = True
            v.View.show_result(result)
