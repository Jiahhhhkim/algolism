import sys
sys.stdin = open('input.txt')

# N = int(input())

# if N %2 == 1:
#     print('홀수')
# else:
#     print('짝수')

# N = int(input())

# if N %2 == 1:
#     print('홀수')
# else:
#     print('짝수')

TC = int(input())

for i in range(TC):
    N = int(input())

    if N % 2 == 1:
        print('홀수')
    else:
        print('짝수')

numbers = input().split()
for number in numbers:
   int_num = int(number)

   if int_num %2 == 1:
       print(f'{int_num}은 홀수입니다.')
