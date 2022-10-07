def fib(n):
    arr = []
    arr.append(1)
    arr.append(1)

    fib1 = fib2 = 1

    n = int(n) - 2

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
        arr.append(fib2)
    print("Значение этого элемента:", arr)
    return arr

def sort(N):
    a = []
    for i in range(N):
        a.append(int(input()))
    print("было: {0}".format(a))

    state = str(input("введите направление сортировки: "))
    if state == "(по возрастанию":
        for i in range(N - 1):
            for j in range(N - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
    else:
        for i in range(N - 1):
            for j in range(N - i - 1):
                if a[j] < a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
    print("стало: {0}".format(a))
    return a

def calc(text):
    result = 0
    if text[1] == '+':
        result = int(text[0]) + int(text[2])
    elif text[1] == '-':
        result = int(text[0]) - int(text[2])
    elif text[1] == '*':
        result = int(text[0]) * int(text[2])
    elif text[1] == '/':
        result = int(text[0]) / int(text[2])
    else:
        print("error")
    print(result)
    return result

# Функция поиска простых чисел методом Решето Эратосфена
# Принимает n
# Возвращает список простых чисел < n
# Пример: 11 -> 2, 3, 5, 7
def find_primes(n):
    pre_primes = []
    for i in range(n):
        pre_primes.append(i)
    pre_primes[1] = 0
    for i in range(2, n):
        if pre_primes[i]:
            for j in range(2*i, n, i):
                pre_primes[j] = 0
    primes = []
    for number in pre_primes:
        if number:
            primes.append(number)
    return primes


# Функция проверки упорядоченности элементов списка от наименьшего к наибольшему
# Принимает на вход список
# Возвращает True, если элементы в списке упорядочены от мин к макс
# Иначе - возвращает False
# Пример:
# [1, 2, 3] -> True
# [1, 2, 2] -> True
# [1, 2, 3, 4, 3] -> False
def is_sorted_from_min_to_max(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

