def user_info():
    name = input("Username: ")
    age = int(input("Age: "))
    return name, age


try:
    username, age = user_info()

    with open("record.txt", "w") as file:
        file.write(f"{username} - {age}\n")

except ValueError:
    print("Please enter a valid number for age.")

except Exception as error:
    print("Something went wrong:", error)

finally:
    print("\nList of Saved User")
    print("Username - Age")

    try:
        with open("record.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File does not exist.")

    print("System complete.")