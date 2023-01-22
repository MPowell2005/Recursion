'''
Names: Michael Powell and Cal Cunnion
Narrative: This program returns an output through a recursive function for any given integer input. Functions include:
- Factorial
- Summation
- Powers
- Fibonacci
- Sum of a number's digits
- Product of a number's digits
- Product of two whole numbers
- Sum of numbers in a range
- Reverse the digits of a number
- Euclid's GCD algorithm
- Compound interest

Author: mpowell23@gcds.net and ccunnion23@gcds.net
'''

# Import Box
from _operator import mod

def factorial(n):
    """
        Summary:
        This function returns the product of all natural numbers starting at the input, n.
       
        Parameters:
        n (int >= 0): The input and starting value of the product.
       
        Returns:
        result (int >= 0): The output of the product of all natural numbers starting at n.
       
        Example:
        factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    """

    if n == 0 :
        return 1
   
    else :
        return n * factorial(n-1)


def summation(n):
    """
        Summary:
        This function returns the sum of all numbers from 1 to n, where n is a natural number.
       
        Parameters:
        n (int >= 0): The ending value of the summation. 
       
        Returns:
        result (int >= 0): The output after the summation of 1 to n. 
       
        Example:
        summation(5) = 5 + 4 + 3 + 2 + 1 = 15
    """

    if n == 0 :
        return 0
   
    else :
        return n + summation(n-1)


def powers(a, n):
    """
        Summary:
        This function returns the value of a number, a, raised to the power of a number, n.
        
        Parameters:
        n (int >= 0): The input and the exponent.
        a (float): The base of the power.
       
        Returns:
        result (float): The output of the base raised to the exponent. 
       
        Example:
        powers(5, 3): 5 * 5 * 5 = 125
    """
    
    if n == 0 :
        return 1
   
    else :
        return a * powers(a, (n - 1))


def Fibonacci(n):
    """
        Summary:
        This function returns the sum of the two preceding numbers of Fibonacci term, n. 
        
        Parameters:
        n (int >= 0): The term of the Fibonacci number sequence. 
       
        Returns:
        result (int >= 0): The value of the Fibonacci number sequence given the nth term.
       
        Example:
        Fibonacci(5) = 5
    """
    
    if n == 0 :
        return 0
   
    elif n == 1 :
        return 1
   
    else :
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def SND(n) :
    """
        Summary:
        This function returns the sum of a number's digits.
        
        Parameters:
        n (int >= 0): The number's digits that will be summed.

        Returns:
        result (int >= 0): The summed digits.
       
        Example:
        SND(12) = 1 + 2 = 3
    """
    
    if n <= 9 :
        return n
   
    else :
        return SND(int(n/10)) + (n % 10)


def PND(n) :
    """
        Summary:
        This function returns the product of a number's digits.
        
        Parameters:
        n (int >= 0): The number's digits that will be multiplied.

        Returns:
        result (int >= 0): The multiplied digits.
       
        Example:
        PND(52) = 5 * 2 = 10
    """
    
    if n <= 9 :
        return n
   
    else :
        return SND(int(n/10)) * (n % 10)


def product(x, y) :
    """
        Summary:
        This function returns the product of two whole numbers (x, y) recursively.
        
        Parameters:
        x (int >= 0): The first whole number.
        y (int >= 0): The second whole number.

        Returns:
        result (int >= 0): The product of x and y.
       
        Example:
        product(5, 3) = 5 + 5 + 5 = 15
    """
    
    if y == 0 :
        return 0
   
    else :
        return x + product(x, y - 1)


def SNR(x, y) :
    """
        Summary:
        This function returns the sum of all natural numbers in the range of [x, y].
        
        Parameters:
        x (int >= 0): The lower bound.
        y (int >= 0): The upper bound.

        Returns:
        result (int >= 0): The sum of all natural numbers between the lower and upper bound.
       
        Example:
        SNR(2, 5) = 2 + 3 + 4 + 5 = 14
    """
    
    if x == y :
        return x
   
    else :
        return y + SNR(x, (y-1))
   

def reverse(n, r):
    """
        Summary:
        This function reverses a number's digits given a natural number input. 
        
        Parameters:
        n (int >= 0): The number's digits that will be reversed. 
        r (int >= 0): The reversing parameter.

        Returns:
        result (int >= 0): The reversed digits. 
       
        Example:
        reverse(15, 0) = 51
    """
    
    if n == 0 :
        return r
   
    else :
        return reverse(n//10, r*10 + n%10)


def GCD(x, y):
    """
        Summary:
        This function returns the greatest common divisor between two whole numbers. 
        
        Parameters:
        x (int >= 0): The first whole number.
        y (int >= 0): The second whole number.

        Returns:
        result (int >= 0): The great common divisor between x and y.
       
        Example:
        GCD(12, 66) = 6
    """
    
    if y <= x and mod(x, y) == 0 :
        return y
   
    else :
        return GCD(y, mod(x, y))


def CIB(p, r, t):
    """
        Summary:
        This functions returns the value of an initial deposit, p, after being computed with an annual interest, r, for t years. 
        
        Parameters:
        p (float): The initial value of the deposit.
        r (float): The annual interest rate.
        t (int >= 0): The number of years that the deposit was compounded. 

        Returns:
        result (float): The compounded deposit after t years. 
       
        Example:
        CIB(2000, 0.05, 2) = (1 + 0.05) * (1 + 0.05) * 2000 = 2000(1.05)^2 = 2205.00.
    """
    
    if t == 0 :
        return p
   
    else :
        return (1 + r) * CIB(p,r,t-1)
   
   
   
def main():
   
    # Description
   
    print('This program returns an output through a recursive function for any given integer input.')
    print("The list of functions available are:\n(1) Factorial\n(2) Summation\n(3) Powers\n(4) Fibonacci\n(5) Sum of a number's digits\n(6) Product of a number's digits\n(7) Product of two whole numbers\n(8) Sum of numbers in a range\n(9) Reverse the digits of a number\n(10) Euclid's GCD algorithm\n(11) Compound Interest")
   
    # Defining variables in the main
    
    restart = 'yes'                                                                                     
   
    function_list = ['factorial', '1', 'summation', '2', 'powers', '3', 'fibonacci', '4', "sum of a number's digits", '5', "product of a number's digits", '6', 'product of two whole numbers', '7', 'sum of numbers in a range', '8', 'reverse the digits of a number', '9', "euclid's gcd algorithm", '10', 'compound interest', '11']
    
    # While loop that repeats the program if the user prompts so
    
    while restart == 'yes' :
       
        # Inserting a function
       
        while True :
            function = input('What function do you want to use?\n')
            function = function.lower()
           
            if function in function_list :
                break
           
            else :
                print('Please insert a function given in the description above.')
                continue
       
        # If statement #1: Functions that take two different inputs for recursion
        
        if function == 'product of two whole numbers' or function == '7' or function == 'sum of numbers in a range' or function == '8' or function == "euclid's gcd algorithm" or function == '10':
            
            # Ask for the two inputs 
            
            while True :
                x = input('Insert a first whole number.\n')
                y = input('Insert a second whole number.\n')
               
                # Ensure the inputs are positive integers greater than zero
               
                try :
                    x = int(x)
                    y = int(y)
                   
                    if x >= 0 and y >= 0 and x < 997 and y < 997 :
                        break
                   
                    else :
                        print('Please insert a whole number less than 997.')
                        continue
                
                # Otherwise, ask the user to enter the inputs again
                
                except :
                    print('Please insert a whole number less than 997.')
                    continue
           
            # Run the functions 
            if function == 'product of two whole numbers' or function == '7':
                result = product(x, y)
           
            elif function == 'sum of numbers in a range' or function == '8' :
                result = SNR(x, y)
           
            else :
                result = GCD(x, y)
       
        # If statement #2: Compound interest 
       
        elif function == 'compound interest' or function == '11' :
            
            # Ask the user for each parameter: p, r, t
            
            while True :
                p = input('What is the initial value of the account?\n')
                r = input('What is the interest rate?\n')
                t = input('How many years is the account being compounded?\n')
               
                # Convert the parameters into their proper numerical forms
                
                try :
                    p = float(p)
                    r = float(r)
                    t = int(t)
                   
                    if p < 0 or t < 0 or t >= 997 :
                        print('Please make the initial value and year positive integers. The year must be less than 997.')
                        continue
                   
                    else :
                        break
               
                # If the latter cannot happen, ask the user to reenter the parameters
               
                except :
                    print('Please insert a positive real number for the initial value, a real number for the interest rate, and a positive integer less than 997 for the year.')
                    continue
            
            # Run the function 
            
            result = CIB(p, r, t)
            
        # If statement #3: All functions that only take in one input
     
        else :
           
            # While True loop to ensure the user enters a single input
            while True :
                n = input('Please insert an input for the function to take in.\n')
               
                # Try and except statement to convert the input into an integer
               
                try :
                    n = int(n)
                   
                    if n >= 0 and n < 997 :
                        break
                   
                    else :
                        print('Please insert a positive integer less than 997 for the function to take in.')
                        continue
               
                except :
                    print('Please insert a positive integer less than 997 for the function to take in.')
                    continue
           
            # Runs the functions
           
            if function == 'factorial' or function == '1' :
                result = factorial(n)
           
            elif function == 'summation' or function == '2' :
                result = summation(n)
               
            elif function == 'powers' or function == '3' :
                
                # Ensures the user enters an appropriate value for the base
                
                while True :
                    a = input('What initial value do you want to use?\n')
                   
                    try :
                        a = float(a)
                        break
                   
                    except:
                        print('Please insert a real number for the initial value.')
                        continue
               
               
                result = powers(a, n)
           
            elif function == 'fibonacci' or function == '4' :
                result = Fibonacci(n)
           
            elif function == "sum of a number's digits" or function == '5' :
                result = SND(n)
           
            elif function == "product of a number's digits" or function == '6' :
                result = PND(n)
               
            elif function == 'reverse the digits of a number' or function == '9' :
                result = reverse(n, 0)
   
        # Returns the result after running the function 
        
        print('The output for the function is ' + str(result) + '.')
       
        # Play Again Option
       
        while True :
   
            restart = input('Do you wish to use this program again?\n')                
            restart = restart.lower()
           
            if restart == 'yes' or restart == 'y' :                      
                print('The program will restart.')
                break
           
            elif restart == 'no' or restart == 'n' :                        
                print('Thanks for using this program...')
                break
           
            else :                                                          
                print('Please insert an appropriate value.')
   

if __name__ == '__main__':
    main()