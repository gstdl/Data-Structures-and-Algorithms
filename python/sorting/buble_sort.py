def buble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr



if __name__ == "__main__":
    from time_counter import timeit
    
    arr = [3, 2, 5, 4, 3, 12, 32, -2, 34, -54, 22]
    sorted_arr = buble_sort(arr)
    print(sorted_arr)
    
    timeit(buble_sort)

