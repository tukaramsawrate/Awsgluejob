def find_single(arr, arr_size):
    
    for i in range(arr_size):
        
        count = 0
        for j in range(arr_size):
            
            if arr[i] == arr[j]:
                count += 1

        
        if count == 1:
            return arr[i]

    
    return -1


arr_example = [2, 3, 5, 4, 5, 3, 4]
arr_size_example = len(arr_example)


result = find_single(arr_example, arr_size_example)
print("Element occurring once is", result)
