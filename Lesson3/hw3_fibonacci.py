
def fibonacci(n):
    if n > 1:
        F = (n - 1) + (n - 2)
        print (F)
        n -= 1
        fibonacci(n)
        
    else:
        print('end')


def main():
    number = int(input('input number fibonacci: '))
    fibonacci(number)


if __name__ == '__main__':
    main()
