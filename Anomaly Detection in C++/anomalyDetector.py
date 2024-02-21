import re

def extract_variables_from_code(code):
    # Regular expression patterns to match different declaration statements
    single_declaration_pattern = r'\b(int|char|float|double)\s+([a-zA-Z_]\w*)\s*=\s*[^;]*;'
    multiple_declaration_pattern = r'\b(int|char|float|double)\s+((?:[a-zA-Z_]\w*\s*,\s*)+[a-zA-Z_]\w*)\s*;'
    
    variables = []

    # Find all matches of single declaration pattern
    matches_single = re.findall(single_declaration_pattern, code)
    # Find all matches of multiple declaration pattern
    matches_multiple = re.findall(multiple_declaration_pattern, code)

    # Extract variable names from single declaration matches
    for match in matches_single:
        variables.append(match[1])

    # Extract variable names from multiple declaration matches
    for match in matches_multiple:
        variable_group = match[1].split(',')
        for var in variable_group:
            variables.append(var.strip())

    return variables

def main():
    # Read C++ code from input file
    with open('input2.cpp', 'r') as file:
        code = file.read()

    # Extract variables from the code
    variables = extract_variables_from_code(code)

    # Print the extracted variables
    print("Variables declared in the code:")
    for var in variables:
        print(var)

if __name__ == "__main__":
    main()
