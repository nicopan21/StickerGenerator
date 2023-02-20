from rembg import remove
import os

def remove_background(input_image_path, output_image_path):
    with open(input_image_path, 'rb') as input_image:
        with open(output_image_path, 'wb') as output_image:
            input = input_image.read()
            output = remove(input)
            output_image.write(output)
    return None

def main(input_folder = 'images', output_folder = 'output'):
    #? get input files and add relative path
    files = os.listdir(input_folder)
    input_files = [f'{input_folder}/{file}' for file in files]
    output_files = [f'{output_folder}/{file}' for file in files]

    for i, (input, output) in enumerate(zip(input_files, output_files)):
        print(f'image ({i+1}/{len(input_files)}): removing background')
        remove_background(
            input_image_path = input, 
            output_image_path = output
        )
    return None

if __name__ == "__main__":
    #? run codes
    main()
