def triplist(lst):
    triplists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            triplist = lst[i:j]
            if sum(triplist) == 59:
                triplists.append(triplist)
    return triplists

lst = [10, 20, 30, 9]
result = triplist(lst)
print("Triplets in the list whose sum is equal to 59:")
for triplist in result:
    print(triplist)
