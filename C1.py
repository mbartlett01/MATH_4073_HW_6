#MATH 4073 Homework 9 - Michael Bartlett
import numpy as np
def euler_method(f, a, b, alpha, steps):
    '''
    Function that estimates the solution of a differential equation using Euler's method
    :param f: The function that is equal to x'(t). Function of the form f(x, t)
    :param a: The initial time
    :param b: The final time
    :param alpha: The initial value; x(a) = alpha
    :param steps: The number of steps to use
    :return: A list containing the estimated function values
    '''

    #Define the step size and initial solution list
    h = (b-a) / steps
    solution = []

    #Set the inital values
    t = a
    x = alpha

    for i in range(steps+1): #Add one to make sure we calculate the value at the final time
        #Add the solution to the solution list
        solution.append(x)

        #Update the values of x and t
        x = x + h*f(x, t)
        t = a + h * i

    return solution

def c2_a(x, t):
    return 1 + (t-x)**2

def c2_b(x, t):
    return t**(-2) * (np.sin(2*t) - 2*t*x)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("C2a solution:")
    for i in euler_method(c2_a, 2, 3, 1, 20):
        print(i)

    print("C2b solution:")
    for i in euler_method(c2_b, 1, 2, 2, 40):
        print(i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
