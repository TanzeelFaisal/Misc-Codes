import re

def extract_variables_from_code(code):
    # Regular expression patterns
    single_declaration_pattern = r'\b(int|char|float|double)\s+([a-zA-Z_]\w*)\s*=\s*[^;]*;'
    multiple_declaration_pattern = r'\b(int|char|float|double)\s+((?:[a-zA-Z_]\w*\s*,\s*)+[a-zA-Z_]\w*)\s*;'
    function_header_pattern = r'\b(int|char|float|double)\s+([a-zA-Z_]\w*)\s*\(([^)]*)\)\s*{'
    
    variables = []
    function_variables = {}

    # Find all matches of single declaration pattern
    matches_single = re.findall(single_declaration_pattern, code)
    matches_multiple = re.findall(multiple_declaration_pattern, code)
    matches_function = re.findall(function_header_pattern, code)

    # Extract variable names from single declaration matches
    for match in matches_single:
        variables.append(match[1])

    # Extract variable names from multiple declaration matches
    for match in matches_multiple:
        variable_group = match[1].split(',')
        for var in variable_group:
            variables.append(var.strip())

    # Extract function name and parameters from function header matches
    for match in matches_function:
        func_name = match[1]
        params = match[2].split(',')
        params = [p.strip().split()[-1] for p in params]  # Extract only parameter names
        function_variables[func_name] = params

    return variables, function_variables

def main():
    # Read C++ code from input file
    with open('input.cpp', 'r') as file:
        code = file.read()

    # Extract variables and function variables from the code
    variables, function_variables = extract_variables_from_code(code)

    # Print the extracted variables
    print("Variables declared in the code:")
    for var in variables:
        print(var)

    # Print the function variables
    print("\nFunction variables:")
    for func, vars in function_variables.items():
        print(func, ":", vars)

if __name__ == "__main__":
    main()