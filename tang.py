
tang_V = 10
def tang_add(tang_list):
    tang_sum = 0
    for i in range(len(tang_list)):
        tang_sum += tang_list[i]
    return tang_sum
tang_list = [1,2,3,4,5]
print(tang_add(tang_list))
