import re

def extract_variables_from_code(code):
    # Regular expression patterns
    single_declaration_pattern = r'\b(int|char|float|double)\s+([a-zA-Z_]\w*)(?:\[\d*\])?\s*=\s*[^;]*;'
    multiple_declaration_pattern = r'\b(int|char|float|double)\s+((?:[a-zA-Z_]\w*\s*,\s*)+[a-zA-Z_]\w*)(?:\[\d*\])?\s*;'
    function_header_pattern = r'\b(int|char|float|double)\s+([a-zA-Z_]\w*)(?:\[\d*\])?\s*\(([^)]*)\)\s*{'
    if_statement_pattern = r'\bif\s*\((.*?)\)'

    variables = []
    redefine_anomalies = []
    undeclared_anomalies = []

    # Find all matches of function header pattern
    matches_function = re.findall(function_header_pattern, code)

    # Extract function name and parameters from function header matches
    for match in matches_function:
        func_name = match[1]
        # Extract parameters
        params = match[2].split(',')
        params = [p.strip().split()[-1] for p in params]  # Extract only parameter names
        
        # Check if function variables are already defined
        for param in params:
            # Remove array brackets if present
            param = re.sub(r'\[\d*\]', '', param)
            if param in variables:
                redefine_anomalies.append(param)
            else:
                variables.append(param)

    # Find all matches of single declaration pattern
    matches_single = re.findall(single_declaration_pattern, code)
    # Find all matches of multiple declaration pattern
    matches_multiple = re.findall(multiple_declaration_pattern, code)

    # Extract variable names from single declaration matches
    for match in matches_single:
        variable_name = match[1]
        # Remove array brackets if present
        variable_name = re.sub(r'\[\d*\]', '', variable_name)
        if variable_name in variables:
            redefine_anomalies.append(variable_name)
        else:
            variables.append(variable_name)

    # Extract variable names from multiple declaration matches
    for match in matches_multiple:
        variable_group = match[1].split(',')
        for var in variable_group:
            variable_name = var.strip()
            # Remove array brackets if present
            variable_name = re.sub(r'\[\d*\]', '', variable_name)
            if variable_name in variables:
                redefine_anomalies.append(variable_name)
            else:
                variables.append(variable_name)

    # Find all matches of if statements
    if_matches = re.findall(if_statement_pattern, code, re.MULTILINE | re.DOTALL)
    # Extract variables from each if statement
    for match in if_matches:
        # Regular expression pattern to match variables
        variable_pattern = r'\b([a-zA-Z_]\w*)\b'
        # Find all variables in the if statement
        variable_matches = re.findall(variable_pattern, match)
        for var in variable_matches:
            if var not in variables and var not in undeclared_anomalies:
                undeclared_anomalies.append(var)

    # Check if extracted variables are assigned or not
    assignment_pattern = r'\b([a-zA-Z_]\w*)\b\s*=\s*'
    for line in code.split('\n'):
        if re.search(assignment_pattern, line):
            assigned_variable = re.search(assignment_pattern, line).group(1)
            if assigned_variable not in variables and assigned_variable not in undeclared_anomalies:
                undeclared_anomalies.append(assigned_variable)

    return undeclared_anomalies

def main():
    # Read C++ code from input file
    with open('input.cpp', 'r') as file:
        code = file.read()

    # Extract undeclared anomalies from the code
    undeclared_anomalies = extract_variables_from_code(code)

    # Print undeclared anomalies
    print("Undeclared anomalies:")
    print(undeclared_anomalies)

if __name__ == "__main__":
    main()
