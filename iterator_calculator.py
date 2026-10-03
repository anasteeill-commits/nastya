class Numbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return (number for number in range(self.start, self.end + 1))


numbers = Numbers(1, 5)

for number in numbers:
    print(number)


def calculator_decorator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            print(expression, "=", result)
            return result
        except ZeroDivisionError:
            print("Помилка: ділення на нуль")
        except SyntaxError:
            print("Помилка: неправильний вираз")
        except NameError:
            print("Помилка: використано невідоме значення")
        except Exception as error:
            print("Помилка:", type(error).__name__, error)

    return wrapper


@calculator_decorator
def calculate(expression):
    return eval(expression)


calculate("10 + 5")
calculate("20 - 7")
calculate("4 * 3")
calculate("10 / 2")
calculate("10 / 0")
calculate("10 +")


class Student:
    def __init__(self, name):
        self.name = name
        self.day = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.day += 1

        if self.day == 1:
            return f"День {self.day}: {self.name} пішла до школи"
        elif self.day == 2:
            return f"День {self.day}: {self.name} написала контрольну"
        elif self.day == 3:
            return f"День {self.day}: {self.name} пішла на танці"
        elif self.day == 4:
            return f"День {self.day}: {self.name} зробила домашнє завдання"
        elif self.day == 5:
            return f"День {self.day}: {self.name} відпочиває"
        else:
            raise StopIteration


student = Student("Настя")

for day in student:
    print(day)
