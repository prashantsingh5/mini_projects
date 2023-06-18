import random
import string

def generate_password(length=8):
    # Define the characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Random Password Generator!")

    # Prompt the user for the desired password length
    length = int(input("Enter the length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Print the generated password
    print("Generated Password:", password)

if __name__ == '__main__':
    main()
