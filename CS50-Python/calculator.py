def main():
    x = int(input("What's x? "))
    print("The square of x is ",squared(x))

def squared(n):
    return n * n

if __name__ == "__main__":
    main()