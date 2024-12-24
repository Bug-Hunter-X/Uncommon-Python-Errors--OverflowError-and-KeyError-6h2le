def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input types.")
        return None

# Uncommon scenario: a is a very large number and b is a very small number
# This can lead to an OverflowError due to floating-point precision limits.
a = 1e308  # A very large number
b = 1e-308  # A very small number
result = function_with_uncommon_error(a, b)
print(f"Result: {result}")

#Another uncommon error: The function attempts to access a non-existent key in a dictionary.
my_dict = {'a': 1, 'b': 2}

# Uncommon scenario: attempting to access a key that might not exist
try:
    value = my_dict['c']
    print(f"Value: {value}")
except KeyError:
    print("Error: Key not found in dictionary.")