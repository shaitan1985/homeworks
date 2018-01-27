

year = int(input())

cond100 = year % 100 == 0
cond400 = year % 400 == 0
cond4 = year % 4 == 0

if cond400 or cond4 and not cond100:
    print("yes")
else:
    print("no")

