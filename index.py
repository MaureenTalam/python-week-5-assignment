# File creation and writing
def create_and_write_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line with a number: 42.\n")
            file.write("Python file handling is easy!\n")
        print("File created and text written successfully.")
    except Exception as e:
        print(f"An error occurred while creating or writing to the file: {e}")

# File reading and displaying content
def read_and_display_file():
    try:
        with open("my_file.txt", "r") as file:
            print("\nContents of the file:")
            print(file.read())
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending the fourth line.\n")
            file.write("Here is another number: 100.\n")
            file.write("This is the final appended line.\n")
        print("Text appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    try:
        create_and_write_file()
        read_and_display_file()
        append_to_file()
        read_and_display_file()  
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File operations completed.")

if __name__ == "__main__":
    main()
