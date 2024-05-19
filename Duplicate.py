def dup(list1, list2, list3):
    #converting list into set to remove repeated numbers
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    duplicates= set1.intersection(set2).intersection(set3)
    return list(duplicates)
list1 = [2, 4, 6, 8, 9]
list2 = [3, 6, 9, 4, 1]
list3 = [9, 3, 5, 7, 6]
result=dup(list1,list2,list3)
print("Duplicates list:",result)
