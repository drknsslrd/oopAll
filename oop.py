import math, time

# 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        print(math.sqrt(self.x ** 2 + self.y ** 2))

p = Point(3, 4)
p.distance_to_zero()
# 2

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        elapsed_time = end_time - self.start_time

        print(f"Прошло времени: {elapsed_time: .4f} секунд")

with Timer():
    time.sleep(2)

# 3

class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration

        currentValue = self.a
        self.a, self.b = self.b, self.a + self.b
        return currentValue

fib_iter = FibonacciIterator(40)
for num in fib_iter:
    print(num)
