\# ITMO Scientific Python 2026 Homework 1



The screenshots for this homework (`HW1\_1.png` and `HW1\_2.png`) are stored in this repository as text files (`HW1\_1.txt` and `HW1\_2.txt`). The conversion is done using \*\*Base64 encoding\*\*.



\### How to Convert Back to Images



To view the original screenshots, you need to decode the text files back into PNG format. You can do this using the provided Python script.



\*\*Prerequisites:\*\*

\*   Python 3 installed on your system.



\*\*Steps:\*\*



1\.  \*\*Clone the repository\*\*:

&nbsp;   ```bash

&nbsp;   git clone https://github.com/duckweedGuard/ITMO\_ScientificPython\_2026.git

&nbsp;   cd ITMO\_ScientificPython\_2026

&nbsp;   ```



2\.  \*\*Run the conversion script\*\* for each file:

&nbsp;   ```bash

&nbsp;   # To decode HW1\_1.txt back to HW1\_1.png

&nbsp;   python image\_text\_converter.py decode HW1\_1.txt HW1\_1\_restored.png



&nbsp;   # To decode HW1\_2.txt back to HW1\_2.png

&nbsp;   python image\_text\_converter.py decode HW1\_2.txt HW1\_2\_restored.png

&nbsp;   ```



3\.  The restored images will be saved as `HW1\_1\_restored.png` and `HW1\_2\_restored.png` in the same folder. You can open them with any image viewer.



\*\*One-liner method using Python directly:\*\*

If you prefer not to use the script, you can do it directly in the Python interpreter:

```python

import base64

\# For HW1\_1.txt

with open('HW1\_1.txt', 'r') as f: img\_data = base64.b64decode(f.read())

with open('HW1\_1\_restored.png', 'wb') as f: f.write(img\_data)

\# Repeat for HW1\_2.txt

