def main():
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(to="somebody"):
    print("Hello, ",to)

main()