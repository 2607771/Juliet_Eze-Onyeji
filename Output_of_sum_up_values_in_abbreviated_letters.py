# Second file path
values_file_path = r'C:\Users\juliet\OneDrive - \Desktop\master work\values_ify_data.txt'

# Function to calculate the total sum for each abbreviated name
def calculate_abbreviation_sums(values_file_path):
    try:
        # Read values from value_ify_data.txt
        values = {}
        with open(values_file_path, 'r') as values_file:
            values_contents = values_file.readlines()
            for line in values_contents:
                parts = line.strip().split()
                if len(parts) == 2:
                    letter, value = parts
                    values[letter] = int(value)
        
        # Read abbreviations from the result
        abbreviations = [
            "FMa", "POa", "SOa", "SPi", "BPo", "ERo", "CWh", "STr", "WTr", "STr",
            "BWi", "CWi", "WWi", "AWi", "EYe", "ABu", "PBu", "CDo", "RWh", "GWi",
            "PWi", "COs", "EWi", "GRo", "Wtr", "CPr", "PEl"
        ]

        # Calculate and print the total sums for each abbreviated name
        print("Abbreviations and Total Sums:")
        for abbreviation in abbreviations:
            total_sum = sum(values.get(letter, 0) for letter in abbreviation[:-1]) + values.get(abbreviation[-1], 0)
            print(f"{abbreviation}: {total_sum}")

    except FileNotFoundError:
        print(f"Error: The file '{values_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Calculate and print the total sums for each abbreviated name
calculate_abbreviation_sums(values_file_path)


