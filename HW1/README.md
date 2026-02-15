# ITMO Scientific Python 2026

This repository contains homework assignments for the Scientific Python course.

## Homework 1: Image to Text Conversion

The screenshots for this homework (`HW1_1.png` and `HW1_2.png`) are stored in this repository as text files (`HW1_1.txt` and `HW1_2.txt`). The conversion is done using **Base64 encoding**.

### How to Convert Back to Images

To view the original screenshots, you need to decode the text files back into PNG format. You can do this using the provided Python script.

**Prerequisites:**
*   Python 3 installed on your system.

**Steps:**

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/duckweedGuard/ITMO_ScientificPython_2026.git
    cd ITMO_ScientificPython_2026
    ```

2.  **Run the conversion script** for each file:
    ```bash
    # To decode HW1_1.txt back to HW1_1.png
    python image_text_converter.py decode HW1_1.txt HW1_1_restored.png

    # To decode HW1_2.txt back to HW1_2.png
    python image_text_converter.py decode HW1_2.txt HW1_2_restored.png
    ```

3.  The restored images will be saved as `HW1_1_restored.png` and `HW1_2_restored.png` in the same folder. You can open them with any image viewer.

**One-liner method using Python directly:**
If you prefer not to use the script, you can do it directly in the Python interpreter:
```python
import base64
# For HW1_1.txt
with open('HW1_1.txt', 'r') as f: img_data = base64.b64decode(f.read())
with open('HW1_1_restored.png', 'wb') as f: f.write(img_data)
# Repeat for HW1_2.txt
