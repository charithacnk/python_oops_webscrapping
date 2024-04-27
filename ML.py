# for i in range(1,50):
#     if i%2==0:

def is_prime(num):
#    if num<2:
#        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
prime_numbers=[num for num in range(1,51) if is_prime(num)]
for x in prime_numbers:
    print(x)
