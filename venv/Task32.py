""" Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума) """

def find_index(arr, min_val, max_val):
    index = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            index.append(i)
    return index


nums = [10, 20, 30, 40, 50, 60, 70]
min_val = 10
max_val = 20

result = find_index(nums, min_val, max_val)
print(result)  