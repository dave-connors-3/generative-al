import os
import random
from argparse import ArgumentParser
from PIL import Image

def get_random_image(image_directory):
    images = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]
    return random.choice(images)

def open_image(image_path):
    with Image.open(image_path) as img:
        img.show()

def main():
    parser = ArgumentParser(description="Generative-Al: Generate a random Al Roker image.")
    parser.add_argument("command", help="command to run. use generate to see generative Al in action")
    args = parser.parse_args()

    command = args.command
    image_directory = 'img'

    if command != "generate":
        print(f"Error: Unknown command '{command}'. Use 'generate'")
        return

    random_image = get_random_image(image_directory)
    image_path = os.path.join(image_directory, random_image)
    open_image(image_path)

if __name__ == "__main__":
    main()
