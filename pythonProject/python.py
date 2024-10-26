# def remove_duplicates(a):
#     return  list(set(a))
# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))



# Напишите функцию multiply_by_index, которая принимает список чисел и возвращает новый список,
# в котором каждый элемент умножен на свой индекс.

# Пример использования:

def multiply_by_index(a):
    n_list = []
    for u, i in enumerate(a):
        n_list.append(u * i)
    print(n_list)
multiply_by_index([1, 2, 3, 4, 5])

# [1, 2, 3, 4, 5]
# Ожидаемый результат: [0, 2, 6, 12, 20]
# num = 5
# print('GG' if num % 2 == 0 else 'not GG')
