objects = [1, 3, 'ff', 3, [1], [1], 3]
new_objects = []
ans = 0

for obj in objects:
    if id(obj) not in new_objects:
        ans += 1
        new_objects.append(id(obj))
print(ans)