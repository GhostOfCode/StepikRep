# fib = lambda x: 1 if x <= 2 else fib(x - 1) + fib(x - 2)
# print(fib(31))
n = int(input('Укажите число строк n\n'))


def summary_ints(iter_num: int) -> int:
    sum_list = [int(input(f'Введите число № {i+1}: ')) for i in range(iter_num)]
    return sum(sum_list)

# n = int(input())
#
# sum_list = [int(input()) for i in range(n)]
# print(sum(sum_list)) - work on Stepik....
