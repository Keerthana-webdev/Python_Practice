def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def analyze(n):
    even = n % 2 == 0
    positive = n > 0
    digits = len(str(abs(n)))
    prime = is_prime(n)

    return even, positive, digits, prime

num = int(input("Enter number: "))
print("Even, Positive, Digits, Prime:", analyze(num))