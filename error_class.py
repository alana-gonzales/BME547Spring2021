def function_error(a, b):
    try:
        c = a + b
        print(c)
        return c
    except TypeError:
        print("Please only add inputs of the same type")

def calc_square_root(n):

    try:
        from calculator import sqrt
    except ModuleNotFoundError:
        print("The my_calculator module did not exist.")
        print("Use the built-in math module instead.")
        import math
    except ImportError:
        print("The sqrt function did not exist")
    
    answer = sqrt(n)
    return answer

def main():
    print(calc_square_root(2))

if __name__ == '__main__':
    main()

