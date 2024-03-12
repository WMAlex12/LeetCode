def descending_order(num):
    print(type(num))
    nums = [int(val) for val in str(num)]
    
    descendig = sorted(nums, reverse=True)
    print(type(nums))
    return int("".join([str(i) for i in descendig]))


print(descending_order(12345))

