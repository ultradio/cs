seek_element = 7
some_list = [2, 3, 5, 7, 11]

def binary_search(seek, some_list):
    
    some_list = sorted(some_list)
    start = 0
    end = len(some_list)-1
    mid = (start + end)//2

    for i in range(len(some_list)//2 + 1):
        if seek == some_list[mid]:
            return mid
        
        if seek < some_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    
    return -1

print(binary_search(seek_element, some_list))