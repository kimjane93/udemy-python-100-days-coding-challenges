# check if number is prime
# can only divided by one and itself without decimals


def prime_checker(number):
    for n in range(2, number):
        if number % n == 0:
            print(f"{number} is not a prime number")
            break
        else:
            print(f"{number} is a prime number")
            break

n = int(input("Check this number: "))
prime_checker(number=n)