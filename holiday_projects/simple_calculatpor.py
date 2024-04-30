# defining functions
# they include : add,div,mult,sub
# user operands and operators
def add(a, b):
    c = a + b
    print('answer  is ', c)


def subtract(a, b):
    d = a - b
    print('result of subtraction is  ', d)


def division(a, b):
    e = a / b
    print('result of the above  division is ', e)


def multiplication(a, b):
    f = a * b
    print('quotient of the multiplication is  ', f)


while True:
    print(' enter option A: for Addition \n ')
    print(' enter option B  : for  subtraction \n')
    print(' enter option  C: for  division \n ')
    print(' enter option  D: for  multiplication \n')

    option = input('option of the operation you want to perform ').lower()
    if option == 'a':
        m = int(input("enter operand 'a' to be added "))
        n = int(input("enter operand 'b' to be added "))
        add(m, n)

    elif option == 'b':
        m = int(input("enter operand 'a' to be subtracted "))
        n = int(input("enter operand 'b' to be subtracted "))

        subtract(m, n)


    elif option == 'c':
        m = int(input("enter operand 'a' to be divided  "))
        n = int(input("enter operand 'b' to be divided  "))
        if m == 0 or n == 0:
            print('number cannot be divided by zero')
        else:
            division(m, n)
    elif option == 'd':
        m = int(input("enter operand 'a' to be multiplied "))
        n = int(input("enter operand 'b' to be multiplied   "))
        multiplication(m, n)

    else:
        print('invalid operand')
