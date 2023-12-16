# File path
file_path = r'C:\Users\juliet\OneDrive - \Desktop\master work\trees_Ify_work.txt'

# Attempt to open the file
try:
    with open(file_path, 'r') as file:
        # Read the contents of the file
        file_contents = file.readlines()
        
        # Process each line and generate abbreviations
        abbreviations = []
        for line in file_contents:
            # Split the line into first and last names
            names = line.strip().split(' ')
            
            # Create the abbreviation
            if len(names) >= 2:
                abbreviation = names[0][0] + names[-1][:2]
                abbreviations.append(abbreviation)
        
        # Print the abbreviations
        print("Abbreviations:")
        for abbreviation in abbreviations:
            print(abbreviation)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
