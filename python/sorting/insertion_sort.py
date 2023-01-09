def insertion_sort(arr):
    if len(arr) < 2:
        return arr
    
    new_arr=[arr[0]]

    for i in arr[1:]:
        if i <= new_arr[0]:
            new_arr.insert(0, i)
            continue
        if i >= new_arr[-1]:
            new_arr.append(i)
            continue
        for (j, prev_value), next_value in zip(enumerate(new_arr[:-1]), new_arr[1:]):
            if prev_value < i and next_value >= i:
                new_arr.insert(j+1, i)
                break

    return new_arr


if __name__ == "__main__":
    from time_counter import timeit

    arr = [3, 2, 5, 4, 3, 12, 32, -2, 34, -54, 22]
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)

    timeit(insertion_sort)
