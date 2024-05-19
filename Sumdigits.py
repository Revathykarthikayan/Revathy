number=input("Enter the number:")
def sum_digits(number):
    #converting number into string to itetrate in list
    num=str(number)
    list_dig=[]
    for char in num:
        list_dig.append(char)
    first_digit=int(num[0])
    last_digit=int(num[-1])
    sum_dig = first_digit + last_digit
    return sum_dig
result = sum_digits(number)
print("Sum is:", result)

