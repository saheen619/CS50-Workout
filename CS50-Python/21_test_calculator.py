from calculator import squared

def main():
    test_squared()

def test_squared():
    try:
        assert squared(2) == 4
    except AssertionError:
        print("2 squared is not 4. Fix it")
    
    try:
        assert squared(3) == 9
    except AssertionError:
        print("3 squared is not 9. Fix it.")
    
    try:
        assert squared(-2) == 4
    except AssertionError:
        print("-2 squared is not 4. Fix it")

    try:
        assert squared(-3) == 9
    except AssertionError:
        print("-3 squared is not 9. Fix it.")

    try:
        assert squared(0) == 0
    except AssertionError:
        print("0 squared is not 0. Fix it.")

    # Automatically testing from 1 - 5 in the squared function

    success = True
    for i in range(1, 6):
        if not (i ** 2 == squared(i)):
            success = False
            break
    if success == True:
        print("The program has successfully passed the test")

if __name__ == "__main__":
    main()

# To run the test program, reaname the 21_calculator.py file to calculator.py as per the pythonic naming conventions.