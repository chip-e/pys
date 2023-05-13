def prime_checker(number):
  if number == 2 or number == 3:
    print(f"{number} IS a prime number")
  elif number % 2 != 0 and number % 3 != 0:
    print(f"{number} IS a prime number")
  else:
    print(f"{number} IS NOT a prime number")

n = int(input("Check this number: " ))
prime_checker(number=n)