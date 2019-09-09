class TooMuchArg(Exception):
    def __init__(self, text):
        self.text = text
        return
class PositiveNumber(Exception):
    def __init__(self,text):
        self.text = text
        return


def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def multi(a, b):
    return (a * b)

def div(a, b):
    return (a / b)



def main():
    try:
        # command, first_number, second_number = input('Введите выражение через пробел: ').split()
        expression = input('Введите выражение через пробел: ').split()
        if len(expression) != 3:
            raise TooMuchArg('Введено неверное количество элементов')
        command, first_number, second_number = list(expression)
        first_number, second_number = int(first_number), int(second_number)
        if first_number < 0 or second_number < 0:
            raise PositiveNumber('Все числа должны быть положительны')
        assert (command == '+' or command == '-' or command == '*' or command == '/') , 'Неверная команда'
        if command == '+':
            print(add(first_number, second_number))
        elif command == '-':
            print(sub(first_number, second_number))
        elif command == '*':
            print(multi(first_number, second_number))
        elif command == '/':
            print(div(first_number, second_number))
        else:
            print('Неверная команда')
    except TooMuchArg as e:
        print (e)
    except ValueError:
        print('Элемент должен быть числом, а не строкой')
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
    except PositiveNumber as e:
        print (e)
    finally:
        print('Конец программы')




main()
