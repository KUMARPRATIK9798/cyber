import cv2
import hashlib

def decrypt(encrypted_image_path, entered_password, message_length):
    """Decrypts a message from an encrypted image with password verification."""
    img = cv2.imread(encrypted_image_path)
    if img is None:
        print(f"Error: Could not open image '{encrypted_image_path}'.")
        return

    c = {i: chr(i) for i in range(256)}
    n, m, z = 0, 0, 0
    message = ""

    for _ in range(message_length):
        try:
            pixel_value = img[n, m, z]
            message += c[pixel_value]
            n += 1
            m += 1
            z = (z + 1) % 3
        except IndexError:
            print("Error: Image size or message length mismatch.")
            return

    # Retrieve stored password hash.
    stored_hash = ""
    hash_length = 64  # SHA-256 hexdigest is always 64 characters.
    for _ in range(hash_length):
        pixel_value = img[n, m, z]
        stored_hash += chr(pixel_value)
        n += 1
        m += 1
        z = (z + 1) % 3

    # Verify password.
    entered_hash = hashlib.sha256(entered_password.encode()).hexdigest()
    if entered_hash == stored_hash:
        print("Decrypted message:", message)
    else:
        print("Incorrect password.")

if __name__ == "__main__":
    encrypted_image_path = input("Enter encrypted image path: ")
    entered_password = input("Enter passcode for Decryption: ")
    message_length = int(input("Enter the length of the original message: "))
    decrypt(encrypted_image_path, entered_password, message_length)



output:
PS D:\New folder (4)> python -u "d:\New folder (4)\decryption.py"
Enter encrypted image path: encryptedImage.png
Enter passcode for Decryption: 789
Enter the length of the original message: 10
Decrypted message: qwertyuiop
