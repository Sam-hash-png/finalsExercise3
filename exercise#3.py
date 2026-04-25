def get_user():
    username = input("Enter Username: ")
    age = int(input("Enter Age: "))
    return username, age


try:
    file = open("users.txt", "w")

    user, age = get_user()
    file.write(user + " - " + str(age) + "\n")

    file.close()

except ValueError:
    print("Invalid input! Age must be a number.")

except Exception as e:
    print("An error occurred:", e)

finally:
    print("\nSaved Users:\nUsername - Age")

    try:
        file = open("users.txt", "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("No saved users found.")

    print("System complete.")