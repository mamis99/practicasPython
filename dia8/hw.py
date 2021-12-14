def find(list, num):
    if num in list:
        return True
    return False
def find_                                                                             (list, num):
    for num_ in list:
        if num_ == num:
            return [True, list.index(num)]
    return False
print(find([1,2,3,4,5],5))
print(find_([1,2,3,4,5],5))