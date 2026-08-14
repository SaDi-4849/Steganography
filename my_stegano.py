
"""
this module is a program to hide 
a massage in a picture by adding colour
"""

from PIL import Image, ImageDraw

def encode_text_to_image(image_path, text, output_path):
    """
    a function for adding code to the picture
    """
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)

    char_index = 0
    text_len = len(text)
    width, height = img.size

    for y in range(0, height, 10):
        for x in range(0, width, 10):
            if char_index < text_len:
                char = text[char_index]
                code = ord(char)
                if code > 255:
                    code = 255

                color = (code, 0, 0)
                char_index += 1
            else:
                color = (0, 0, 0)

            for i in range(x, min(x + 10, width)):
                for j in range(y, min(y + 10, height)):
                    draw.point((i, j), fill=color)

        if char_index >= text_len:
            break

    img.save(output_path)


def decode_text_from_image(image_path):
    """
    a function to see the code from image
    """
    img = Image.open(image_path).convert("RGB")
    decoded_text = ""

    for y in range(0, img.size[1], 10):
        for x in range(0, img.size[0], 10):
            r, g, b = img.getpixel((x, y))

            if r == 0:
                return decoded_text

            decoded_text += chr(r)

    return decoded_text
