list=[10,22,37,100,999,501,87,351]
list_even=[]
list_odd=[]
for number in list:
   if number % 2 == 0:
      list_even.append(number)
   else:
        list_odd.append(number)
print("Odd numbers list :",list_odd)
print("Even numbers list:",list_even)
