import threading

def task_1(): 
    def calculate_squares() -> None:
        for i in range(1, 11):
            print(f"Квадрат числа {i}: {i ** 2}")

    def calculate_cubes() -> None:
        for i in range(1, 11):
            print(f"Куб числа {i}: {i ** 3}")
            
    thread1 = threading.Thread(target=calculate_squares)
    thread2 = threading.Thread(target=calculate_cubes)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Вычисления завершены!")
    
task_1()

import time

def task_2():
    def print_with_delay() -> None:
        for num in range(1, 11):
            time.sleep(1)
            print(num)
        
    thread1 = threading.Thread(target=print_with_delay)
    thread2 = threading.Thread(target=print_with_delay)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    
task_2()

import asyncio

def task_3(): 
    async def calc_square(num) -> int:
        print(f"Вычисляю квадрат {num}...")
        await asyncio.sleep(0.3)
        print(f"Квадрат {num} – {num**2}")

    async def main(num_list):
        squared_nums = [calc_square(num) for num in num_list]
        await asyncio.gather(*squared_nums)

    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    
    if __name__ == '__main__':
        asyncio.run(main(num_list))

task_3()

import multiprocessing
import math

def calculate_factorial(n: int) -> None:
    result = math.factorial(n)
    print(f"Факториал числа {n}: {result}")

def task_4():
    processes = []
    
    for i in range(1, 11):
        process = multiprocessing.Process(target=calculate_factorial, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Все вычисления завершены!")

if __name__ == "__main__":
    task_4()
