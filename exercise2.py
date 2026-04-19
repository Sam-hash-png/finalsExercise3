try:
    
    note1 = input("Enter a short note: ")
    with open("notes.txt", "w") as file:
        file.write(note1 + "\n")

   
    print("\nFile content:")
    with open("notes.txt", "r") as file:
        print(file.read())

    
    note2 = input("Enter another note: ")
    with open("notes.txt", "a") as file:
        file.write(note2 + "\n")

    
    print("\nUpdated content:")
    with open("notes.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")