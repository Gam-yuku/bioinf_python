def printab(a,b):
    print(a)
    print(b)

printab(10,30) #позиционные 'keyword arguments' (порядок всегда важен)
printab(a=10, b=20) #именованные

#keyword arguments always after non-keyword arguments
printab(10,b=20)

lst=[10,20]
printab(*lst) # = printab(lst[0], lst[1]) - 'keyword arguments'

args = {'a':10, 'b':20}
printab(**args) 
# = printab(key1 = args[key1], key2 = args[key2])