import re

def extract_variables_and_code(code):
    # Find all variable declarations
    matches = re.findall(r'\b(int|bool|char)\s+([a-zA-Z_]\w*)(?:\s*=\s*\w+)?\s*;', code)
    print(matches)
    
    # Extract only variable names from declarations
    variables = [match[1] for match in matches]
    print(variables)
    
    return variables, code

def remove_strings_and_comments(code):
    code = re.sub(r'(<<)\s*".*?"\s*', '', code) # Remove strings
    code = re.sub(r'//.*', '', code) # Remove single-line comments
    return code

def find_anomalies(code):
    variables, code = extract_variables_and_code(code)
    anomalies = []

    code = remove_strings_and_comments(code)
    print(code)

    # Check for variable usage
    for var in variables:
        if re.search(r'\b{}\b'.format(re.escape(var)), code):
            # print(f"Variable '{var}' is used.")
            pass
        else:
            anomalies.append(f"Variable '{var}' declared but not used")

    return anomalies

# Read code from file
file_path = 'input2.cpp'
# file_path = 'input.cpp'
with open(file_path, 'r') as file:
    code = file.read()

anomalies = find_anomalies(code)
if anomalies:
    print("Data flow anomalies detected:")
    for anomaly in anomalies:
        print(' - ', anomaly)
else:
    print("No data flow anomalies detected.")