# import pandas as pd

# chunk_size = 100  # Adjust chunk size based on your memory capacity
# chunks = pd.read_csv('/Users/z3540536/Desktop/test.csv', chunksize=chunk_size)

# for chunk in chunks:
#     # Perform operations with 'chunk', which is a DataFrame
#     # For example, basic data inspection
#     print(chunk.head())

import pandas as pd

# Path to your CSV file
file_path = '/Users/z3540536/Desktop/test.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Find the first row where the 'target' column equals 1
# first_row_target_1 = df[df['target'] == 1].head(1)

first_ten_rows_target_1 = df[df['target'] == 1].head(5)


# Display the row
# print(first_row_target_1)

# # Convert the row to JSON
# row_json = first_row_target_1.to_json(orient='records', lines=True)
# print(row_json)

# Print the names of all the columns
column_names = df.columns
print("Column names:")
print(column_names)

# columns_of_interest = ['index', 'Access Gained', 'Attack Origin', 'Authentication Required',
#        'Availability', 'CVE ID', 'CVE Page', 'CWE ID', 'Complexity',
#        'Confidentiality', 'Integrity', 'Known Exploits', 'Publish Date',
#        'Score', 'Summary', 'Update Date', 'Vulnerability Classification',
#        'add_lines', 'codeLink', 'commit_id', 'commit_message', 'del_lines',
#        'file_name', 'files_changed', 'func_after', 'func_before', 'lang',
#        'lines_after', 'lines_before', 'parentID', 'patch', 'project',
#        'project_after', 'project_before', 'target', 'vul_func_with_fix',
#        'processed_func', 'flaw_line', 'flaw_line_index']

# # Print the values of the specified columns
# for column in columns_of_interest:
#     if column in first_row_target_1.columns:
#         print(f"{column}: {first_row_target_1.iloc[0][column]}")
#     else:
#         print(f"Column '{column}' not found in the data.")

# Assuming 'first_ten_rows_target_1' contains the first 10 rows where 'target' equals 1
# columns_of_interest = ['index', 'Access Gained', 'Attack Origin', 'Authentication Required',
#        'Availability', 'CVE ID', 'CVE Page', 'CWE ID', 'Complexity',
#        'Confidentiality', 'Integrity', 'Known Exploits', 'Publish Date',
#        'Score', 'Summary', 'Update Date', 'Vulnerability Classification',
#        'add_lines', 'codeLink', 'commit_id', 'commit_message', 'del_lines',
#        'file_name', 'files_changed', 'func_after', 'func_before', 'lang',
#        'lines_after', 'lines_before', 'parentID', 'patch', 'project',
#        'project_after', 'project_before', 'target', 'vul_func_with_fix',
#        'processed_func', 'flaw_line', 'flaw_line_index']

columns_of_interest = ['Score', 'Summary', 'Vulnerability Classification',
       'commit_message', 'func_after', 'func_before', 'lang',
        'target', 'CWE ID', 'Vulnerability Classification', 'vul_func_with_fix']

for index, row in first_ten_rows_target_1.iterrows():
    print(f"Row {index + 1}:")
    for column in columns_of_interest:
        if column in first_ten_rows_target_1.columns:
            print(f"{column}: {row[column]}")
        else:
            print(f"Column '{column}' not found in the data.")
    print("------")  # Separator between rows


# read_large_json('/Users/z3540536/Desktop/MSR_data_cleaned.json')




