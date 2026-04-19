try:
    user_input = input("Please enter a short note: ")
    with open("notes.txt", "w") as file_ptr:
        file_ptr.write(user_input + "\n")

    print("\nReading existing file...")
    with open("notes.txt", "r") as file_ptr:
        data = file_ptr.read()
        print("File Content:", data)

    extra_note = input("Enter another note to add: ")
    with open("notes.txt", "a") as file_ptr:
        file_ptr.write(extra_note + "\n")

    print("\nDisplaying updated content:")
    with open("notes.txt", "r") as file_ptr:
        print(file_ptr.read())

except FileNotFoundError:
    print("Error: The system could not find the file.")
except Exception as err:
    print(f"An error occurred: {err}")