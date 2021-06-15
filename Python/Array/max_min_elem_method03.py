# Maximum and minimum of an array using minimum number of comparisons
# Time complexity: O(n)
# Total Comparison: if n is even -> 3(n)/2 - 2 if n is odd then it does more than 3n/2 -2 comparisons


def get_max_min(low, high, arr):
    if low == high:
        arr_max = arr_min = arr[low]
        return arr_max, arr_min
    elif high == (low+1):
        if arr[high] > arr[low]:
            arr_max = arr[high]
            arr_min = arr[low]
        else:
            arr_max = arr[low]
            arr_min = arr[high]
        return arr_max, arr_min
    else:
        mid = (low+high) // 2
        arr_max1, arr_min1 = get_max_min(low, mid, arr)
        arr_max2, arr_min2 = get_max_min(mid+1, high, arr)

    return max(arr_max1, arr_max2), min(arr_min1, arr_min2)


if __name__ == '__main__':
    array = list(map(int, input("Array: ").strip().split()))
    print(f"Current Array: {array}")
    mx, mn = get_max_min(0, (len(array)-1), array)
    print(f"max:{mx} & min: {mn}")
