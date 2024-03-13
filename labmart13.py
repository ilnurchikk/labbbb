#1Написать программу, выполняющую сортировкусписка целых чисел методом пузырьковой сортировки


# def bubble_sort(array):
#     array_lenght = len(array)
#     for i in range(array_lenght):
#         for j in range(0, array_lenght - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     return array
#
# my_list = [1, 4, 2, 8, 6, 3, 5, 9, 7]
# print(f'неотсортированный список {my_list}')
# print(f'отсортированный список {bubble_sort(my_list)}')

# 2 Написать программу, выполняющую сортировку списка целых чисел методом вставок.


# def insertion_sort(array):
#     array_lenght = len(array)
#     for i in range(1, array_lenght):
#         key = array[i]
#         j = i - 1
#         while j >= 0 and key < array[j]:
#             array[j + 1] = array[j]
#             j -= 1
#         array[j + 1] = key
#     return array
#
# my_list = [1, 4, 2, 8, 6, 3, 5, 9, 7]
# print(f'неотсортированный список {my_list}')
# print(f'отсортированный список {insertion_sort(my_list)}')

# 3 Есть список целых. Необходимо первую половину cписка отсортировать по убыванию, вторую половинупо возрастанию.

# def insertion_sort(array):
#     array_lenght = len(array)
#     for i in range(1, array_lenght):
#         key = array[i]
#         j = i - 1
#         while j >= 0 and key < array[j]:
#             array[j + 1] = array[j]
#             j -= 1
#         array[j + 1] = key
#     return array
#
# my_list = [1, 4, 2, 8, 6, 3, 5, 9, 7]
# print(f'неотсортированный список {my_list}')
# print(f'отсортированный список {insertion_sort(my_list)}')




def insertion_sort(array):
    array_lenght = len(array)
    for i in range(1, array_lenght):
        for j in range(1, array_lenght, 10):
            if i // 10 % 2 == 0:
                key = array[i]
                j = i - 1
        while j >= 5 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

my_list = [1, 4, 2, 8, 6, 3, 5, 9, 7, 0]
print(f'неотсортированный список {my_list}')
print(f'отсортированный список {insertion_sort(my_list)}')