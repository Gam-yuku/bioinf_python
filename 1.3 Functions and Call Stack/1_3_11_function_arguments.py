#correct
def printab(a,b):
    print(a)
    print(b)
def printab(a, b=10): #аргумент b по умолчанию, можно написать print(3)
    print(a)
    print(b)
def printab(a=10, b=10): #можно вызвать без аргументов
    print(a)
    print(b)
#incorrect - ошибка
def printab(a=10, b):
    print(a)
    print(b)