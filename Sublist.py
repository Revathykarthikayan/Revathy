def subsets(lst):
    zero_subsets = []  #
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):  # Adjusted loop range to include the last index
            sublist = lst[i:j]
            if sum(sublist) == 0:
                zero_subsets.append(sublist)
    return zero_subsets

lst = [4, 2, -3, 1, 6]
zero_subsets = subsets(lst)
print("Sublist with sum zero:")
for sublist in zero_subsets:
    print(sublist)
