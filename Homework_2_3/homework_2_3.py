class Too_much_arg(Exception):
    def __init__(self, text):
        self.text = text
        return
class Positive_number(Exception):
    def __init__(self,text):
        self.text = text
        return


def add(a, b):
    print (f'\nОтвет: {a + b}')

def sub(a, b):
    print(f'\nОтвет: {a - b}')

def multi(a, b):
    print(f'\nОтвет: {a * b}')

def div(a, b):
    print(f'\nОтвет: {a / b}')



def main():
    try:
        # command, first_number, second_number = input('Введите выражение через пробел: ').split()
        expression = input('Введите выражение через пробел: ').split()
        if len(expression) != 3:
            raise Too_much_arg('Введено неверное количество элементов')
        command, first_number, second_number = list(expression)
        first_number, second_number = int(first_number), int(second_number)
        if first_number < 0 or second_number < 0:
            raise Positive_number('Все числа должны быть положительны')
        assert (command == '+' or command == '-' or command == '*' or command == '/') , 'Неверная команда'
        if command == '+':
            return add(first_number, second_number)
        elif command == '-':
            return sub(first_number, second_number)
        elif command == '*':
            return multi(first_number, second_number)
        elif command == '/':
            return div(first_number, second_number)
    except Too_much_arg as e:
        print (e)
    except ValueError:
        print('Элемент должен быть числом, а не строкой')
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
    except Positive_number as e:
        print (e)
    finally:
        print('Конец программы')




main()