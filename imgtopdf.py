import os
from pathlib import Path
from PIL import Image


def folder_images_to_pdf(folder_path, output_pdf_path):
    # Convert folder path string to a Path object
    img_dir = Path(folder_path)

    # Define valid image extensions
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}

    # 1. Automatically find all images in the folder and sort them alphabetically
    image_paths = sorted([
        p for p in img_dir.iterdir()
        if p.suffix.lower() in valid_extensions
    ])

    if not image_paths:
        print(f"No valid images found in folder: '{folder_path}'")
        return

    # 2. Open all images and correctly use .convert("RGB")
    images = [Image.open(img).convert('RGB') for img in image_paths]

    # Extract the first image and append the rest
    first_image = images[0]
    remaining_images = images[1:]

    # Save all images into one PDF
    first_image.save(
        output_pdf_path,
        "PDF",
        save_all=True,
        append_images=remaining_images
    )
    print(f"Successfully created: {output_pdf_path} from {len(images)} images.")


# Example usage
# Make sure "image_folder" is the correct path relative to where you run the script
folder_images_to_pdf("image_folder", "combined_document.pdf")
