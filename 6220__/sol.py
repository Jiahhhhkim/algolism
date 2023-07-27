import sys
sys.stdin = open('input.txt', encording='utf-8')

man1 = input()
man2 = input()

if man1 == '가위' and man2 == '가위':
    print('result : Draw')
elif man1 == '가위' and man2 == '바위':
    print('Result : man1 Win!')



