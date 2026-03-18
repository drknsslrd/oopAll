import math

# 1-1
str = "Hello, World!"
print(str, '\n')


# 1-2
tuple = (1, 2, 3, 'a', 'b', 'c', [1, 2, 3], 0.1, 22.8, 322.0)
print(tuple, '\n')


# 2-1
result = 0
i = 15
while i in range(15, 31):
    if (i != 19) or i != 23 or (i != 27):
        result += i
    i += 1
print(result, '\n')


# 2-2
num = 45 ** 2
if num in [12345, 'qwerty', '13638', '64737', 1643.75, 1643.0]:
    print(num, " Входит в список", '\n')
else:
    print(num, " Не входит в список", '\n')


# 2-3
base = 5 # задаем переменной base значение integer = 5
height = 8 # задаем переменной height значение integer = 8
area = 0.5 * base * height # считаем область (присвоение, умножение и тд)
print(area, '\n') # вывод переменной


# 2-4
x = 1.24 # 0.8370 NO Err
print( x ** math.atan(x) / x ** 2 + math.sqrt(x) / ((1 + x) ** 2) )
print()


# 3-1
answer = input("Вы веган? ")
if answer == 'да':
    print("Вы веган")
else:
    print("Вы не веган")
print()


# 3-2
x = float(input())
y = float(input())
z = float(input())
print(x, y, z)

if (x + y + z) < (x**2 + y**2 + z**2):
    x = min(y, z)
    y = min(x, z)
    z = min(x, y)
else:
    x = max(y, z)
    y = max(x, z)
    z = max(x, y)
print(x, y, z, '\n')


# 3-3
x = int(input())

def func(x):
    if 0 < x <= 1:
        print(math.acos(math.e**(-x)))
    elif 1 < x <= 3:
        print(math.atan(x))
    elif 3 < x <= 6:
        print((1 + x) ** 2)
    elif 6 < x <= math.inf:
        print(math.log(x, math.e))
func(x)
print()


# 4-1
arr = [x for x in range(20)]
for i in arr:
    if (i % 9 == 0):
        continue
    else:
        print(i)
print()


# 4-2
def foo(x, N):
    y = 0.0
    multiply = 1

    for i in range(1, N+1):
        x = math.sin(x)
        multiply *= 2 * i
        y += x / multiply
    return y

print(foo(2.22, 4), '\n')


# 5-1
n = [1.0, 0.3, 322.0, 102.2, 228.1, 148.8, -10.2, -0.2]
C = 40
quantityMoreC = 0
for x in n:
    if x > C:
        quantityMoreC += 1

maxIndex = 0
maxAbs = abs(n[0])

for i in range(1, len(n)):
    if abs(n[i]) > maxAbs:
        maxAbs = abs(n[i])
        maxIndex = i


result = 1
for x in n[maxIndex + 1:]:
    result *= x

print(quantityMoreC)
print(result, '\n')



# 6-1
matrix = [
    [1, 2, 3, 4],
    [2, -2, -4, 4],
    [1, 0, 8, 8],
    [2, 3, 2, 2]
]

def firstZeroColumn(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(cols):
        for j in range(rows):
            if matrix[j][i] == 0:
                return i
    return None

def rowCharacteristic(row):
    return sum(x for x in row if x < 0 and x % 2 == 0)

def sortByCharacteristic(matrix):
    return sorted(matrix, key=rowCharacteristic, reverse=True)


sortedMatrix = sortByCharacteristic(matrix)

print(firstZeroColumn(matrix))
for row in sortedMatrix:
    print(row)
print()


# 7-1
words = ["abc", "cba", "amogus", "java", "death", "avaj"]
duplicateWords = words.copy()

result = []
for word in words:
    reverseWord = word[::-1]

    if reverseWord not in duplicateWords:
        result.append(reverseWord)

print([x[::-1] for x in result])