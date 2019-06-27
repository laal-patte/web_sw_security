#This program calculates the LCM of the two numbers entered by the user

def LCM(number1, number2):
    '''This function calculates LCM of two numbers inputed by the user'''
    maximum = max(number1, number1)
    while True:
        if (i % number1 == 0  and i % number2 == 0):
            lcm = i
            break
        i += maximum
    return lcm

if __name__ == '__main__':
    userInput1 = input('Enter first number: ')
    userInput2 = input('Enter second number: ')
print('LCM of {} and {} is {}'.format( userinput1, userInput2, LCM(userInput1, userInput2)))
