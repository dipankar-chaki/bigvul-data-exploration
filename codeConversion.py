# def function_to_string(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             # Read all lines from the file
#             lines = file.readlines()
#             # Convert each line to a format that includes \n at the end
#             # Except for the last line to avoid adding an extra newline character
#             formatted_lines = [line.rstrip('\n') + '\\n' for line in lines[:-1]] + [lines[-1].rstrip('\n')]
#             # Combine all lines into a single string
#             function_string = ''.join(formatted_lines)
#             return function_string
#     except FileNotFoundError:
#         return "The specified file was not found."

# # Example usage
# file_path = '/Users/z3540536/Desktop/beforeFunction.txt'  # Change this to the path of your text file
# print(function_to_string(file_path))

# Example multi-line code
code = """def hello_world():
    print("Hello, world!")
"""

# Convert the multi-line code into a single line by escaping newlines
escaped_code = code.replace("\n", "\\n")

# The escaped_code can now be fed into the LLM as a single line
print(escaped_code)


