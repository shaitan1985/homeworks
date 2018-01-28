x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

l1 = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
l2 = ((x2 - x3) ** 2) + ((y2 - y3) ** 2)
l3 = ((x3 - x1) ** 2) + ((y3 - y1) ** 2)

mybool = False

if l1 + l2 == l3:
    mybool = True
elif l2 + l3 == l1:
    mybool = True
elif l1 + l3 == l2:
    mybool = True

if mybool:
    print("yes")
else:
    print("no")