def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

def main():
    print("Welcome to the Caesar Cipher Tool!")

    while True:
        print("\nChoose an operation:")
        print("a) Encrypt a message")
        print("b) Decrypt a message")
        print("c) Exit")

        choice = input("Enter your choice (a/b/c): ")

        if choice == "a":
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher(text, shift, "encrypt")
            print(f"Encrypted message: {encrypted_text}")

        elif choice == "b":
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher(text, shift, "decrypt")
            print(f"Decrypted message: {decrypted_text}")

        elif choice == "c":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
