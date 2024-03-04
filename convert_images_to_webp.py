import os
import subprocess

def convert_images_to_webp(input_dir, output_dir, quality=80):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Loop through each file in the input directory
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)

        # Check if the file is an image (you can add more image extensions as needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Construct the output path with the same filename but with a '.webp' extension
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.webp')

            # Convert the image to WebP
            convert_to_webp(input_path, output_path, quality)

def convert_to_webp(input_file, output_file, quality=80):
    try:
        # Run the cwebp command using subprocess
        subprocess.run(['cwebp', '-q', str(quality), input_file, '-o', output_file], check=True)
        print(f"Conversion successful: {input_file} -> {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    # Replace 'input_directory' and 'output_directory' with your actual directory paths
    input_directory = './low_resolution/lr'
    output_directory = './low_resolution/lr_webp'

    # Call the function to convert images to WebP
    convert_images_to_webp(input_directory, output_directory)
