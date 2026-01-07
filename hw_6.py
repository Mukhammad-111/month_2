def bubble_sort(numbers):
    len_numbers = len(numbers)

    for i in range(len_numbers - 1):
        for j in range(0, len_numbers - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

random_numbs = [2, 13, 42, 5, 745, 3, 29, 1, 34, 4]
print(bubble_sort(random_numbs))


def binary_search(val, n: list):
    result_ok = False
    first = 0
    last = n[-1]

    while first <= last:
        middle = (first + last) // 2
        if val == n[middle]:
            result_ok = True
            break
        elif val > n[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print(f'Элемент найден: {val}')
    else:
        print("Элемент не найден")

number_list = list(range(1, 100))
binary_search(39, number_list)