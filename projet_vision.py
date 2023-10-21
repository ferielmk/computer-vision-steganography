import cv2
import numpy as np

# Function to hide text in an image
def hide_text_in_image(text, image_path, output_image_path):
    # Read the image
    img = cv2.imread(image_path)

    if img is None:
        print("Erreur lors du chargement de l'image.")
        return

    # Convert the text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)

    text_index = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for l in range(3):
                pixel_value = format(img[i][j][l], '08b')
                if text_index < len(binary_text):
                    new_pixel_value = pixel_value[:-1] + binary_text[text_index]
                    img[i][j][l] = int(new_pixel_value, 2)
                    text_index += 1
                else:
                    break

    cv2.imwrite(output_image_path, img)
    print("Texte caché avec succès dans l'image.")

# Function to extract hidden text from an image
def extract_text_from_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    if img is None:
        print("Erreur lors du chargement de l'image.")
        return

    hidden_text = ''
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for l in range(3):
                pixel_value = format(img[i][j][l], '08b')
                hidden_text += pixel_value[-1]

    text = ''
    text_started = False  # A flag to indicate the start of text
    for i in range(0, len(hidden_text), 8):
        character = hidden_text[i:i + 8]
        if text_started:
            if character != "00000000":  # Filter out null characters
                text += chr(int(character, 2))
            else:
                break  # Stop when we encounter null characters
        elif character != "00000000":  # Start when we encounter a non-null character
            text_started = True
            text += chr(int(character, 2))

    return text

# Driver code
text_to_hide = "This is a hidden message."
input_image_path = "slide_1.png"
output_image_path = "image_with_hidden_text.png"
img_avant=cv2.imread(input_image_path,1)
img_apres=cv2.imread(output_image_path ,1)

# Hide text in the image
hide_text_in_image(text_to_hide, input_image_path, output_image_path)

# Extract hidden text from the image
extracted_text = extract_text_from_image(output_image_path)
print("Hidden Message:", extracted_text)
cv2.imshow("image sans code secret ",img_avant)
cv2.imshow("image avec code secret",img_apres)
cv2.waitKey(0)
cv2.destroyAllWindows()
