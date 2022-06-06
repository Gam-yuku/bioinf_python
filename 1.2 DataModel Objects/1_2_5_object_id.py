x = [1, 2, 3]
print(id(x))
print("id списка", id([1,2,3]))
y = x
print(id(y))
y.append(4) #изменился объект, теперь [1, 2, 3, 4]
print(id(x))
print(id(y))
print("id списка", id([1,2,3]))
print("id списка", id([1,2,3,4]))
print("id списка", id([1,2,3,4,5]))

s = "123"
t = s
t = t + "4"

print(str(x) + " " + s) #x = [1, 2, 3, 4], s не изменится