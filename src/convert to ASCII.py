from PIL import Image
import json
import os

def convert_to_ascii(path):
    # Open image and convert to grayscale
    image = Image.open(path).convert("L")

    # Define ASCII characters to represent different shades of gray
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    # Resize image to desired dimensions
    width, height = image.size
    aspect_ratio = height / width
    new_width = 100
    new_height = int(aspect_ratio * new_width * 0.5)
    resized_image = image.resize((new_width, new_height))

    # Convert image to list of grayscale pixel values
    pixel_values = list(resized_image.getdata())

    # Convert pixel values to ASCII characters
    ascii_chars = [ASCII_CHARS[int(pixel_value / 25)] for pixel_value in pixel_values]

    # Convert ASCII characters to string
    ascii_str = "".join(ascii_chars)

    # Split string into lines of desired width
    lines = [ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)]

    # Print ASCII art to console
    return "\n".join(lines)

# Define the folder path
folder_path = "./input"

# Get a list of file names in the folder
file_names = os.listdir(folder_path)

# Create a list to hold the file paths in order
file_paths = []

# Loop through every file in the folder
for file_name in file_names:

    # Check if the file is a PNG file
    if file_name.endswith(".png"):

        # Extract the frame number from the file name
        frame_number = int(file_name.split("_")[2].split(".")[0])

        # Get the full path for the file
        file_path = os.path.join(folder_path, file_name)

        # Add the file path to the list in the correct order
        file_paths.insert(frame_number, file_path)

dictJSON = {}

# Loop through every file path in the correct order
for index, file_path in enumerate(file_paths):

    #print path
    print(file_path)

    # Process the file as needed
    strASCII = convert_to_ascii(file_path)

    #put it in dictJSON
    dictJSON[index] = strASCII

# Convert the dictionary to JSON
my_json = json.dumps(dictJSON)

# Write the JSON to a file
with open("./output/ASCII.txt", "w") as file:
    file.write(my_json)


