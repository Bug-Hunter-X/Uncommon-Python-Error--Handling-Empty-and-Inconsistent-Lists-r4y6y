def function_with_uncommon_error_solution(data):
    if not data:
        return 0  # Handle empty list
    numeric_data = [x for x in data if isinstance(x, (int, float))]
    if not numeric_data:
        return "Error: Data must contain at least one number"
    result = sum(numeric_data) / len(numeric_data)
    return result

# Example usage:
my_list = [1,2,3,4,5]
print(function_with_uncommon_error_solution(my_list))

my_list = []
print(function_with_uncommon_error_solution(my_list))

my_list = [1,2,"a",4,5]
print(function_with_uncommon_error_solution(my_list))