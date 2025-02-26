# Image Steganography with Password Protection

This project demonstrates a simple image steganography technique with password protection using Python, OpenCV, and hashlib.

## Files

* `encryption.py`: Contains the encryption algorithm.
* `decryption.py`: Contains the decryption algorithm.
* `README.md`: This file, providing instructions and information about the project.

## Requirements

* Python 3.x
* OpenCV (`cv2`)
* hashlib

You can install OpenCV using pip:

```bash
pip install opencv-python

Encryption (encryption.py)
Functionality
     The encrypt function takes an image, a secret message, and a password as input. It hides the message within the image's pixel data and appends a SHA-256 hash of the password for verification during decryption.

Usage
Run encryption.py:

Bash

python encryption.py
You will be prompted to enter:

    The path to the image file.
    The secret message to hide.
    A password for encryption.
The encrypted image will be saved as encryptedImage.png.

Algorithm
     Loads the input image using OpenCV.
     Creates a dictionary d to map characters to their ASCII values.
     Iterates through the message and writes the ASCII values of each character to the image's RGB pixel data in a sequential manner.
     Calculates the SHA-256 hash of the provided password.
     Appends the hash to the end of the pixel data.
     Saves the modified image as encryptedImage.png.

Decryption (decryption.py)
Functionality
    The decrypt function takes an encrypted image, a password, and the length of the original message as input. It retrieves the hidden message from the image and verifies the password before displaying the message.

Usage
Run decryption.py:

Bash

python decryption.py
You will be prompted to enter:
   The path to the encrypted image (encryptedImage.png).
   The password used for encryption.
   The length of the original message.
   If the password is correct, the decrypted message will be displayed. Otherwise, an "Incorrect password" message will be shown.

Algorithm:
     Loads the encrypted image using OpenCV.
     Creates a dictionary c to map ASCII values back to characters.
     Retrieves the message from the image's pixel data using the provided message length.
     Retrieves the stored password hash from the end of the pixel data.
     Calculates the SHA-256 hash of the entered password.
     Compares the calculated hash with the stored hash.
     If the hashes match, displays the decrypted message. Otherwise, displays an error message.

Important Notes
    Image Format: The code defaults to saving the encrypted image as a PNG (.png) to avoid lossy compression that can alter pixel values.
    Password Security: While SHA-256 hashing provides a good level of password protection, this steganography method is not intended for highly sensitive data.
    Message Length: The decryption script requires the original message length because the length is not encoded within the image.
    Error Handling: Basic error handling is implemented to catch file loading issues and pixel access errors.
    Pixel Capacity: The image must have sufficient pixel capacity to hold the message and the password hash.
    Debugging: Debugging print statements are included in the encryption and decryption scripts to help track pixel values and characters. Remove or comment out these lines for production use.
