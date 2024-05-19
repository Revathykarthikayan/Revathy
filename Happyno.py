def happy(num):
    seen =set()
    while num!= 1 and num not in seen:
        seen.add(num)
        #sum of squares in each digit in num in string form
        num = sum(int(digit)**2 for digit in str(num))
    return num==1
given_list=[10,22,37,87,100,999,501,357]
happy_count=0
for num in given_list:
    if happy(num):
        print(num,"is happy number")
        happy_count+=1
print("Happy numbers count in list is:",happy_count)
