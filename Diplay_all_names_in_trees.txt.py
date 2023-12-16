# File path
file_path = r'C:\Users\juliet\OneDrive - \Desktop\master work\trees_Ify_work.txt'

# Attempt to open the file
try:
    with open(file_path, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()
        print(f"File contents:\n{file_contents}")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
