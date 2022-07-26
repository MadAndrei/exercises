def fast_sort(array):
    n = len(array)
    if n <= 1:
        return array.copy()

    left_part = fast_sort(array[:n // 2])
    right_part = fast_sort(array[n // 2:])

    merge_array = [0] * n
    left_index = right_index = merge_index = 0

    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] < right_part[right_index]:
            merge_array[merge_index] = left_part[left_index]
            left_index += 1
        else:
            merge_array[merge_index] = right_part[right_index]
            right_index += 1
        merge_index += 1

    for i in range(left_index, len(left_part)):
        merge_array[merge_index] = left_part[i]
        merge_index += 1
    for i in range(right_index, len(right_part)):
        merge_array[merge_index] = right_part[i]
        merge_index += 1

    return merge_array

# Была выбрана сортировка слиянием, т.к. она в худшем, лучшем и среднем случае отработает за n*logn операций,
# что является достаточно быстрым показателем.

# Можно было использовать timsort, который в лучшем случае отработает за n операций, но timsort лучше всего
# работает с реальными частично отсортированными данными, а по условию порядок числел
# выбирается случайно. Также из-за сложности алгоритма и медлительности некоторых операций в python заметного ускорения
# добиться не получится

# Можно было использовать quicksort, который в среднем показывает лучшие показатели, но в худшем случае работает
# за n^2 операций, что непозволительно.

# Сортировка слиянием отсортирует массив быстрее других известных сортировок.
