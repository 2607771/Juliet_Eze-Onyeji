# First file path
trees_file_path = r'C:\Users\juliet\OneDrive - \Desktop\master work\trees_Ify_work.txt'

# Second file path
values_file_path = r'C:\Users\juliet\OneDrive - \Desktop\master work\values_Ify_data.txt'

# Function to read and print file contents
def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            print(f"File contents for {file_path}:\n{file_contents}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Load and print contents of the first file
read_and_print_file(trees_file_path)

# Load and print contents of the second file
read_and_print_file(values_file_path)
