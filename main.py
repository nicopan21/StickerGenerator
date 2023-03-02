from rembg import remove
import os
import cv2
from cv2 import dnn_superres


def remove_background(input_image_path, output_image_path):
    with open(input_image_path, 'rb') as input_image:
        with open(output_image_path, 'wb') as output_image:
            input = input_image.read()
            output = remove(input)
            output_image.write(output)
    return None


def upgrade_image(image):
    # Create an SR object
    sr = dnn_superres.DnnSuperResImpl_create()

    # Read image
    image = cv2.imread(image)

    # Read the desired model
    path = "Modulos/Models/EDSR_x4.pb"
    sr.readModel(path)

    # Set the desired model and scale to get correct pre- and post-processing
    sr.setModel("edsr", 3)

    # Upscale the image
    result = sr.upsample(image)

    #Save the image
    cv2.imwrite("output/temp/temp.jpeg", result)
    return result


def main(input_folder = 'images', output_folder = 'output'):
    #? get input files and add relative path
    files = os.listdir(input_folder)
    input_files = [f'{input_folder}/{file}' for file in files]
    output_files = [f'{output_folder}/{file}' for file in files]

    for i, (input, output) in enumerate(zip(input_files, output_files)):
        print(f'\nimage ({i+1}/{len(input_files)}): Upgrading image')
        upgrade_image(input)
        input = 'output/temp/temp.jpeg'

        print(f'image ({i+1}/{len(input_files)}): removing background')
        remove_background(
            input_image_path = input, 
            output_image_path = output
        )
    return None


if __name__ == "__main__":
    #? run codes
    main()