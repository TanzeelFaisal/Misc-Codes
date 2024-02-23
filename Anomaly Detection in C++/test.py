import re

def extract_variables_from_cpp(code):
    # Regular expression pattern to match variable assignments
    pattern = r'\b([a-zA-Z_]\w*)\s*=\s*([^;]+);'

    # Find all matches
    matches = re.findall(pattern, code)
    print(matches)

    # Extract variable names
    variables = [match[0] for match in matches]

    # Extract variables from arithmetic expressions in the code
    for match in matches:
        rhs_expression = match[1]
        arithmetic_variables = re.findall(r'\b([a-zA-Z_]\w*)\b', rhs_expression)
        variables.extend(arithmetic_variables)

    return variables

# Example C++ code
cpp_code = """
#include <iostream>

int main() {
    int low = 0, high = 10;
    int mid = (low + high) / 2;
    high = mid - 1;
    return 0;
}
"""

# Extract variables from C++ code
variables = extract_variables_from_cpp(cpp_code)
print(variables)
