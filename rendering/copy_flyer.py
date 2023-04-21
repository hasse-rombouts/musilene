import os
from PIL import Image

def copy_flyer():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    flyer_path = get_flyer_path(base_path)
    dest_path = os.path.join(base_path, 'build', 'assets', 'figures', 'flyer.webp')
    with Image.open(flyer_path) as image:
        # Calculate the height based on the aspect ratio.
        height = round(800 / (image.width / image.height))
        # Resize the image.
        resized_image = image.resize((800, height))
        # Convert the image to WebP format and save it.
        resized_image.save(dest_path, format="webp")

def get_flyer_path(base_path):
    extensions = ['png', 'jpg', 'jpeg', 'webp']
    for extension in extensions:
        flyer_path = os.path.join(base_path, 'src', 'flyer.' + extension)
        if os.path.exists(flyer_path):
            return flyer_path
    raise ValueError("No flyer found in the src folder.")