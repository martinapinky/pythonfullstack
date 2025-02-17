#### Decorator --> a way to modify and extend the behaviour of functions and methods wihout
# changing the actual code

# Allows you to wrap another function
# functions can be passed as an argument to another function

# Wrapper function --> a decorator uses inner function to modify the behaviour

def decorator_function(original_function):
    def wrapper_function():
        print("Function is being decorated")
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("display function is being called")

display()


# The decorator that accepts an argument
import time

# The decorator that accepts an argument

def time_decorator(log_message):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            start_time = time.time()  # Record the start time
            result = original_function(*args, **kwargs)  # Call the original function
            print
            end_time = time.time()  # Record the end time
            execution_time = end_time - start_time
            print(f"{log_message} - Function {original_function.__name__} took {execution_time:.4f} seconds to execute.")
            return result
        return wrapper_function
    return decorator_function

# Using the decorator with a custom message
# TIME DEC = (MSG)(SLOW FUNC)
@time_decorator("Execution Time Log")
def slow_function():
    time.sleep(2)  # Simulate a slow function by sleeping for 2 seconds
    print("Slow function executed.")

slow_function()

