
import cv2
import hashlib
import string

def encrypt(image_path, message, password, output_path="encryptedImage.png"):
    """Encrypts a message into an image with password hashing."""
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not open image '{image_path}'.")
        return

    d = {chr(i): i for i in range(256)}
    n, m, z = 0, 0, 0
    for char in message:
        pixel_value = d[char]
        img[n, m, z] = pixel_value
        n += 1
        m += 1
        z = (z + 1) % 3

    # Store password hash in the last few pixels.
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    hash_length = len(password_hash)
    for i in range(hash_length):
        img[n, m, z] = ord(password_hash[i])
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite(output_path, img)
    
if __name__ == "__main__":
     image_path = input("Enter image path: ")
     message = input("Enter secret message: ")
     password = input("Enter a passcode: ")
     encrypt(image_path, message, password)
