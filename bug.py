def function_with_uncommon_error(data):
    try:
        # Assume 'data' is a list of numbers
        result = sum(data) / len(data) 
        return result
    except ZeroDivisionError:
        return 0
    except TypeError:
        return "Error: Data must be a list of numbers"

# Example usage:
my_list = [1,2,3,4,5]
print(function_with_uncommon_error(my_list))

my_list = []
print(function_with_uncommon_error(my_list))

my_list = [1,2,"a",4,5]
print(function_with_uncommon_error(my_list))