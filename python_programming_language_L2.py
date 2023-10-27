"""
作业要求
编写一个Python程序，实现一个计数器函数，该函数能够记录特定函数的调用次数。你需要使用闭包和装饰器来实现这个功能。
"""


def get_count(func):
    """
    外部函数：计数
    :param func: 调用函数
    :return: num: 调用次数
    """
    num = 0

    def inner_func():
        func()
        nonlocal num
        num = num + 1
        print(f"该函数调用次数为：{num}")
    return inner_func


@get_count
def work1():
    pass


if __name__ == "__main__":
    for i in range(3):
        work1()