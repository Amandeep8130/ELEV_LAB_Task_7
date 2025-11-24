import os
from PIL import Image

input_folder = "images"
output_folder = "resized_images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

width = int(input("Enter new width: "))
height = int(input("Enter new height: "))
new_size = (width, height)

for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img_resized = img.resize(new_size)

        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        img_resized.save(output_path, "JPEG")

        print(f"Resized and saved: {output_path}")
