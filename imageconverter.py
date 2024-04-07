from PIL import Image
import os
from datetime import datetime

# Load the image
img = Image.open("")

# Resize the image if it's larger than 96x64 pixels
if img.size[0] > 96 or img.size[1] > 64:
    img = img.resize((96, 64), Image.LANCZOS)

# Initialize the array to store hexadecimal values
hex_array = []

# Loop over each pixel to fill the array with hex values
for y in range(64):
    for x in range(96):
        pixel = img.getpixel((x, y))
        red = pixel[0] // 8
        green = pixel[1] // 4
        blue = pixel[2] // 8
        hex_value = f"{red:05b}{green:06b}{blue:05b}"
        hex_array.append(f"{int(hex_value, 2):04X}")

# Convert the array to a string format
array_str = ",".join(hex_array)

# Get the current date and time for the filename
now = datetime.now()
date_time_str = now.strftime("%Y%m%d_%H%M%S")

# Create the output file name
output_filename = f"HexImage_{date_time_str}.txt"
# Note: Since the original script uses '__file__', in this context, we'll use a fixed directory. 
# You may need to adjust this according to your actual environment or requirements.
output_path = os.path.join('.', output_filename)

# Save the hexadecimal array to the file
with open(output_path, "w") as file:
    file.write(array_str)

print(f"Hexadecimal array saved to: {output_path}")
