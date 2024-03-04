from PIL import Image
import os

def resize_images(input_folder, output_folder, width, height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            try:
                # Open the image file
                with Image.open(input_path) as img:
                    # Resize the image
                    resized_img = img.resize((width, height), Image.LANCZOS)

                    # Save the resized image to the output folder
                    output_path = os.path.join(output_folder, filename)
                    resized_img.save(output_path)

                    print(f"Resized {filename} successfully.")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
if __name__ == "__main__":
    # Set the input and output folders, and desired width and height
    input_folder = ''
    output_folder = ''
    target_width = 1080
    target_height = 920

    # Resize images
    resize_images(input_folder, output_folder, target_width, target_height)
