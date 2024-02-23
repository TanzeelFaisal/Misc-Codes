import re

def extract_variables(line):
    # Regular expression pattern to match variable assignments
    pattern = r'([a-zA-Z_]\w*)'

    # Extract variable names using regular expression
    variables = re.findall(pattern, line)
    
    # Return unique variable names
    return set(variables)

# Example assignment lines
lines = [
    "high = mid - 1", 
    "mid = (low + high) / 2"
]

# Extract variables from each line
for line in lines:
    variables = extract_variables(line)
    print(f"Assignment: {line}  Variables: {variables}")
