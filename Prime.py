list=[10,22,37,87,100,999,357,501]
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime(list):
    p_num= []
    for n in list:
        if is_prime(n):
            p_num.append(n)
    return p_num
p_num= prime(list)
print("Prime number in the list:", p_num)














