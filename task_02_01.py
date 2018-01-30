def del_some(chr, s):
    print(s)
    for i in chr:
        print(i)
        if s.find(i):
            s = ''.join(s.split(i, '')




# # def is_palindrome(s):
# #     s = ''.join(s.split(' ', '')
# #     print(s)
# #     center = len(s)//2
# #     first_part = s[0:center]
# #     second_part = s[-1:-center-1:-1]
# #     print(second_part)
# #     print(first_part)

# #     print(first_part == second_part)

# # is_palindrome('Сел в озере березов лес')

del_some(' ,.|', '12,3 4.56  6')
