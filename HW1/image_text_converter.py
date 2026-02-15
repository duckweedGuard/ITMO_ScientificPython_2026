# File: image_text_converter.py
import base64
import sys
import os

def image_to_text(image_path, output_text_path):
    """
    Converts an image file (e.g., PNG) to a Base64-encoded text file.
    """
    try:
        with open(image_path, 'rb') as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode('utf-8')

        with open(output_text_path, 'w', encoding='utf-8') as text_file:
            text_file.write(encoded_string)

        print(f"Successfully converted '{image_path}' to '{output_text_path}'")
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def text_to_image(text_path, output_image_path):
    """
    Converts a Base64-encoded text file back into an image file.
    """
    try:
        with open(text_path, 'r', encoding='utf-8') as text_file:
            encoded_string = text_file.read()

        decoded_bytes = base64.b64decode(encoded_string)

        with open(output_image_path, 'wb') as img_file:
            img_file.write(decoded_bytes)

        print(f"Successfully converted '{text_path}' back to '{output_image_path}'")
    except FileNotFoundError:
        print(f"Error: Text file '{text_path}' not found.")
    except base64.binascii.Error:
        print(f"Error: '{text_path}' does not contain valid Base64 data.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage:")
        print("  To encode (image -> text): python image_text_converter.py encode <image_path> <output_text_path>")
        print("  To decode (text -> image): python image_text_converter.py decode <text_path> <output_image_path>")
        sys.exit(1)

    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if command == "encode":
        image_to_text(input_file, output_file)
    elif command == "decode":
        text_to_image(input_file, output_file)
    else:
        print(f"Unknown command: {command}. Use 'encode' or 'decode'.")
        sys.exit(1)