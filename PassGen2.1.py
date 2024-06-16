
import random
import string
import os
import pyfiglet  # Import pyfiglet library

# Define a leetspeak translation table
leet_table = {
    'A': '4', 'a': '4',
    'E': '3', 'e': '3',
    'I': '1', 'i': '1',
    'O': '0', 'o': '0',
    'S': '5', 's': '5',
    'T': '7', 't': '7'
}

def leetspeak(word):
    """Convert a word to leetspeak."""
    return ''.join(leet_table.get(char, char) for char in word)

def generate_password(word, min_length, max_length):
    """Generate a password based on a leetspeak word and random characters."""
    leet_word = leetspeak(word)
    password_length = random.randint(min_length, max_length)
    
    if password_length < len(leet_word):
        leet_word = leet_word[:password_length]
    else:
        additional_characters = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_length - len(leet_word)))
        leet_word += additional_characters
    
    return leet_word

def main():
    while True:
        # Print a stylized title using pyfiglet
        custom_fig = pyfiglet.Figlet(font='Doom')
        print(custom_fig.renderText('PassGen2.1'))
        
        # Ask the user for 10 words
        print("\nPlease enter 10 words to describe your target:")
        user_words = [input(f"Word #{i+1}: ") for i in range(10)]
        
        # Ask the user for the minimum and maximum length of the passwords
        min_length = int(input("\nEnter the minimum length of the passwords: "))
        max_length = int(input("Enter the maximum length of the passwords: "))
        
        # Ask the user for the filename to save the passwords
        filename = input("\nEnter the filename to save the passwords (e.g., my_passwords): ").strip()
        
        # Ensure filename ends with .txt
        if not filename.endswith(".txt"):
            filename += ".txt"
        
        # Ask the user for the number of passwords to generate
        num_passwords = int(input("Enter the number of passwords to generate: "))
        
        # Open the file to write the passwords to
        with open(filename, "w") as file:
            file.write("")
            for _ in range(num_passwords):
                # Select a random word from the user's words
                word = random.choice(user_words)
                
                # Generate the password
                password = generate_password(word, min_length, max_length)
                
                # Write the password to the file
                file.write(password + "\n")
        
        print(f"\n{num_passwords} passwords have been generated and saved to {filename}")
        
        # Ask the user if they want to generate more passwords
        while True:
            choice = input("\nDo you want to generate more passwords? (yes/no): ").strip().lower()
            if choice in ["yes", "no"]:
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        
        if choice == "no":
            print("Exiting Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
