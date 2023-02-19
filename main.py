class Calculator():

    def __init__(self):
        print('Hello, This is a Calculator')
        
    def addition(self,list_):
        sum_ = 0
        for i in list_:
            sum_ += i
        return sum_

    def multiplication(self,list_):
        sum_ = 0
        for i in list_:
            if sum_ == 0:
                sum_ = i
            else:
                sum_ *= i
        return sum_

    def persentage(self,list_, total):
        sum_ = 0
        for i in list_:
            sum_ += i
        per = sum_ / total
        return per * 100

    # lambda
    division = lambda self, a, b: a // b
    substraction = lambda self, a, b: a - b
    
    # Main function
    def main_function(self, input_):
        inp = int(input('Length <: '))
        count = 0

        list_ = list()
        while count < inp:
            num = int(input('Number <: '))
            list_.append(num)
            count += 1

        if input_ == 1:
            result = calculator.addition(list_)
            print(f'The result is: {result}')

        elif input_ == 2:
            num1 = int(input('Number_1 <: '))
            num2 = int(input('Number_2 <: '))
            result = calculator.division(num1, num2)
            print(f'The result is: {result}')

        elif input_ == 3:
            result = calculator.multiplication(list_)
            print(f'The result is: {result}')

        elif input_ == 4:
            num1 = int(input('Number_1 <: '))
            num2 = int(input('Number_2 <: '))
            result = calculator.substraction(num1, num2)
            print(f'The result is: {result}')

        elif input_ == 5:
            total = int(input('Total <: '))
            result = calculator.persentage(list_, total)
            print(f'The result is: {round(result,2)} %')

        else:
            print('Invalid input')


if __name__ == '__main__':
    calculator = Calculator()
    print(
        '\n1. Addition'
        '\n2. Division'
        '\n3. Multiplication'
        '\n4. Subtraction'
        '\n5. Parsentage'
        '\n6. Quit'
    )
    input_ = int(input('What Operation Do you need to perform? <: '))
    
    if input_ in [1,2,3,4,5]:
        calculator.main_function(input_)
    elif input_ == 6:
        print('Thank you for using the calculator :) ')
        exit()
    elif input_ < 1 or input_ > 6:
        print('Enter a valid number. ')
        


  