from turtle import position


def printab(a,b,*args):
    print('positional argument a ', a)
    print('positional argument b ', b)
    print('additional arguments:')
    for arg in args:
        print(arg)

printab(10,20,30,40,50)

"""
additional arguments: 
30
40
50
"""

def printab(a,b,**kwargs):
    print('positional argument a ', a)
    print('positional argument b ', b)
    print('additional arguments:')
    for key in kwargs:
        print(key, kwargs[key])

printab(10,20,c=30,d=40,jimmi=123)

"""
additional arguments: 
c 30
d 40
jimmi 123
"""

def function_name([positional_args, #a,b,c
                  [positional_args_with_default, #a=0, b=True
                  [*pos_args_name, #*lst
                  [keyword_only_args, #часто не используется
                  [**kw_args_name]]]]]): #**kw
    pass
                   
def printab(a,b=10, *args, c=10, d, **kwargs):
    print(a,b,c,d)
#positional_args = a
#positional_args_with_default = b=10
#*pos_args_name = *args
#keyword_only_args = c=10, d (аргументы, которые можем передать только по имени)
#**kw_args_name = **kwargs

printab(15, d = 15) #чтобы вызвать функцию необходимо первому позицинному аргументу a
#передать 15, и должны явно по имени передать d, т.к. он находится в том блоке
#куда аргумент передать можно только по имени
