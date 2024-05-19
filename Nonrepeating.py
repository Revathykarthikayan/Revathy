def nonrepeat(l):
    count={}
    for item in l:
        count[item]= count.get(item, 0) +1
    for item in l:
        if count[item] == 1:
            return item
    return None
l=[7, 5, 8, 4, 9, 4, 7]
result= nonrepeat(l)
print("First non repeating element in list",result)



