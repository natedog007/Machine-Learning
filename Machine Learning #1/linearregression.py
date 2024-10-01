# linear Regression 
# Comments may be seen as obivious but its just so I can better learn the syntax
from numpy import *

def compute_error_for_line_given_points(b, m, points):
    #initialize error at 0
    totalError = 0

    # Finding the error per point
    for i in range(0 , len(points)):
        # Get x and y within the range of points
        x = points[i,0]
        y = points[i,1]

        #Equation of Sum y(distance from line) - mx+b (line) ^2
        totalError += (y - (m * x + b)) ** 2

    # returns average total error over the amount of points = the average error per point
    return totalError / float(len(points))

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    # Starting value for slope and y intercept
    m = starting_m
    b = starting_b
    
    #gradient decent
    for i in range(num_iterations):
        
        b, m = step_gradient(b, m, array(points), learning_rate)
    
    return [b,m]

# sometime ig
def step_gradient(b_currnet, m_current, points, learning_rate):
    
    b_gradient = 0
    m_gradient = 0
    
    for i in range(0, len(points)):
        # Points for the gradient
        x = points[i,0]
        y = points[i,1]
        
        N = float(len(points))

        #Direction with respect to b and m (the parital derivative of the error function)
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_currnet))
        b_gradient += -(2/N) * (y - ((m_current * x) + b_currnet))
        
    # Update b and m
    new_b = b_currnet - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return[new_b, new_m]
        
def run():
    # Collect Data
    # Delimiter seperates data points from comments allowing the program to distinguished between point
    points = genfromtxt('data.csv', delimiter=',')

    # Define hyperparameters
    # Speed of converge 
    learning_rate = 0.00001
    # y = mx + b 
    # y-intercept
    initial_b = 0
    # Slope
    initial_m = 0
    num_iterations = 1000

    print(points)
    # Training model
    #print starting gradient desent at b = {0}, m = {0}, error = {0}.format(initail_b,initail_m, compute_error_for_line_given_points(initail_b, initail_m, points))
    #[b ,m] = gradient_decent_runner(points, initail_b, initail_m, learning_rate, num_interations))
    print(f"Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
    print("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print(f"After {num_iterations} iterations b = {b}, m = {m}, error = {compute_error_for_line_given_points(b,m,points)}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))




# Main function (similar to C/C++)
if __name__ == '__main__':
    run()
