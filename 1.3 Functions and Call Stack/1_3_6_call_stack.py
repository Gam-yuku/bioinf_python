def g():
    print('g')
def f():
    print('f')
    g()
    print('f')
print('print')
f()
print('print')

"""
1. module - print('print') - функция print('print') на стеке после 
модуля затем снимет ее после выполнения
2. module - f() - print('f') - функция print('f') на стеке после 
f() затем снимет ее после выполнения
3. module - f() - g()
4. module - f() - g() - print('g') - функция print('g') на стеке после 
g() затем снимет ее после выполнения
5. module - f() - g() - функция print('g') была последней внутри 
функции g(), поэтому снимаем ее с исполнения
6. module - f() - print('f')- функция print('f') на стеке после 
f() затем снимет ее после выполнения
7. module - f() - функция print('f') была последней внутри 
функции f(), поэтому снимаем ее с исполнения
8. module
9. module - print('print')
10. module
"""

#стек на примере списка
x = [1,2,3]
x.append(4)
x.append(5)
print(x) #[1,2,3,4,5]

top = x.pop() #pop забирает элемент с конца списка и возвращает его
print(top) #5
print(x) #[1,2,3,4]

top = x.pop()
print(top) #[4]
print(x) #[1,2,3]



