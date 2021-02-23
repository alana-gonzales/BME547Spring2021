import logging

def fibonacci(fib_list):
    next_number = fib_list[-1] + fib_list[-2]
    logging.info("{} + {} = {}".format(fib_list[-1], fib_list[-2], next_number))
    fib_list.append(next_number)
    if next_number < 100:
        fibonacci(fib_list)
    else:
        logging.warning("Reached end of list")
    return fib_list


def main():
    x = [0, 1]
    answer = fibonacci(x)
    print(answer)


if __name__ == "__main__":
    logging.basicConfig(filename="fib.log", filemode='w', level=logging.INFO)
    main()