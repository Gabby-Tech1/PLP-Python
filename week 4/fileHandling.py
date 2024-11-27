def read_and_write_file():
    try:
        # Ask the user for the input filename
        input_file = input("Enter the name of the file to read: ")

        # Attempt to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()  # Read the content of the file
            print("Original Content:")
            print(content)

            # Modify the content (e.g., converting to uppercase)
            modified_content = content.upper()

        # Ask the user for the output filename
        output_file = input("Enter the name of the file to write the modified content: ")

        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to '{output_file}'.")

    except FileNotFoundError:
        print("Error: The file you are trying to read does not exist.")
    except IOError:
        print("Error: There was an issue reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
read_and_write_file()
