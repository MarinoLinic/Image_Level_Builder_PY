import PIL.Image
import PIL.features
import numpy as np
import os


def main():
    filename = "Level1.png"

    image = PIL.Image.open(filename)

    size = width, height = image.size

    print(size)

    colors = image.getcolors(maxcolors=256) # how many pixels use what color

    a = np.asarray(image)

    # print(PIL.features.pilinfo())

    # print(list(image.getdata()))

    print(a)
    print(colors)

    PIL.Image.fromarray(a, mode="RGBA").save("Level2.png", format="PNG")



    del image


if __name__ == "__main__":
    main()
