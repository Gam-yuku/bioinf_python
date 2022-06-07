def h():
  print(12)

def f():
  g(h)

def g(a):
  a()

g(f)

"""
1. module - g(f)
2. module - g(f) - g(a) 
3. module - g(f) - g(a) -   a()
4. module - g(f) - g(a) 
5. module - g(f) 
6. module - g(f) - f()
7. module - g(f) - f() - g(h)
8. module - g(f) - f() - g(h) - g(a)
9. module - g(f) - f() - g(h) - g(a) - a() = 6
10. module - g(f) - f() - g(h) - g(a)
11. module - g(f) - f() - g(h)
12. module - g(f) - f() - g(h) - h()
13. module - g(f) - f() - g(h) - h() - print(12) = 6
14. module - g(f) - f() - g(h) - h()
15. module - g(f) - f() - g(h)
16. module - g(f) - f() 
17. module - g(f) 
18. module  
"""