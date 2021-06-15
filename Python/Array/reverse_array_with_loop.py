def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    array = list(map(int, input("Array: ").strip().split()))
    print(f"Current Array: {array}")
    reverse_array(array, 0, (len(array)-1))
    print(f"Reversed Array: {array}")