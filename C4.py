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

def c4(x, t):
    return -x + t + 1

def c4_sol(t):
    return np.exp(-t) + t

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Estimate x(5) using 3 different values of h
    print("C4a:")
    for h in [0.2, 0.1, 0.05]:
        steps = (int)(5 / h)
        sol = euler_method(c4, 0, 5, 1, steps)
        print("h:", h, "x(5):", sol[steps])

    #Compare the errors using the diffierent values of h
    print("\nC4b:")
    for h in [0.2, 0.1, 0.05, 0.01, 0.005, 0.001]:
        steps = (int)(5 / h)
        sol = euler_method(c4, 0, 5, 1, steps)
        print("h:", h, "Error:", abs(sol[steps] - c4_sol(5)))
        