def fibonacci(n):
    a, b = 0, 1
    sequence = []
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    print(fibonacci(n))
