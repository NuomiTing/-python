import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

PRIMES = [112272535095293] * 100


def is_prime(number):
    # 是否是素数  cpu密集型
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(number)))
    for i in range(3, sqrt_n + 1, 2):
        if number % i == 0:
            return False
    return True


def single_thread():
    for number in PRIMES:
        is_prime(number)


def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == "__main__":
    start = time.time()
    single_thread()
    print("single_thread cost", time.time() - start)

    start = time.time()
    multi_thread()
    print("multi_thread cost", time.time() - start)

    start = time.time()
    multi_process()
    print("multi_process cost", time.time() - start)

'''
执行结果：
single_thread cost 42.45777988433838
multi_thread cost 43.40500092506409
multi_process cost 9.744339942932129

多线程效果还没有单线程好，多进程最佳
'''