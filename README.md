# Image to PDF Converter

A simple Python utility to merge multiple images from a directory into a single PDF file.

## Features

- **Multiple Formats**: Supports `.jpg`, `.jpeg`, `.png`, and `.bmp`.
- **Automatic Sorting**: Images are automatically sorted alphabetically before converting.
- **Color Correction**: Converts images to RGB to ensure consistent output.

## Prerequisites

- Python 3.8+
- [Pillow](https://python-pillow.org/)

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/woott07/ImageToPDF.git
   cd imgTopdf
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your images inside the `image_folder` directory (or specify any folder path).
2. Run the script:
   ```bash
   python imgtopdf.py
   ```
3. The converted PDF will be saved as `combined_document.pdf`.

### Customizing in Python

You can also import and use the function in your own code:

```python
from imgtopdf import folder_images_to_pdf

folder_images_to_pdf(
    folder_path="path/to/images",
    output_pdf_path="output/document.pdf"
)
```
