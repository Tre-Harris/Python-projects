def reverse_list(input_list):
    reversed_list = []
    # Iterate over the input list from end to start
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list

# Example usage:
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Original list:", original_list)
print("Reversed list:", reversed_list)
def reverse_list(list):
    result=[]
    for i in range(len(list))
    result.append(list[-i-1])
    print(result)
    reverse_list([1,2,3,4])