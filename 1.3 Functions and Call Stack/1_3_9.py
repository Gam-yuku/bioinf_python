def closest_mod_5(x):
    y = 0
    if x % 5 == 0:
        y = x
        return y
    else:
        y = (x+5)//5 * 5
        return y
    

print(closest_mod_5(6))

"""
6//5 = 1
(6+5)//5 = 2
y = (x + 5)//5 * 5 
"""