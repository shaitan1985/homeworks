n = int(input())
p = int(input())

with open('data.txt') as f:
    lst = f.read().split()
first_lst = []
second_lst = []
for i in lst:
    int_i = int(i)
    if int_i % n == 0:
        first_lst.append(str(int_i) + ' ')
    second_lst.append(str(int_i ** p) + ' ')

with open('out-1.txt', 'w') as f:
    f.write(''.join(first_lst).strip())
with open('out-2.txt', 'w') as f:
    f.write(''.join(second_lst).strip())

