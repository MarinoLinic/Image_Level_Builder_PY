import PIL.Image
import PIL.features
import numpy as np
import os


class Colors:
    WHITE = [255, 255, 255, 255]
    BLACK = [0, 0, 0, 255]
    PLATFORM = [128, 84, 148, 255]
    PLATFORM2 = [244, 58, 160, 255]
    PLATFORM3 = [211, 18, 241, 255]
    WALL = [51, 24, 231, 255]
    HEALTHORB = [52, 216, 208, 255]
    PLAYER = [27, 233, 42, 255]
    ENEMY = [241, 0, 0, 255]
    BOSS = [120, 0, 0, 255]


def filling_pixels(fill_color):
    for k in range(increment):
        for h in range(increment):
            b[i+k][j+h] = fill_color


def main():
    filename = "Level1.png"
    image = PIL.Image.open(filename)

    size = width, height = image.size
    # print("Shape of the array is : ", np.shape(a))

    # print(size)
    # colors = image.getcolors(maxcolors=256) # how many pixels use what color
    # print(colors)
    # print(PIL.features.pilinfo())
    # print(list(image.getdata()))
    # print(a)
    # print("something:", len(b[1079]))
    # fill_color = 0, 255, 255, 255

    a = np.asarray(image)

    global i
    global j
    global increment
    i = 0
    j = 0
    increment = 1

    global b
    b = a.copy()
    b.setflags(write=1) # making array writable

    f = open("coordinates.txt", "w")
    while i < len(b)-(increment-1):
        j = 0
        while j < len(b[i])-(increment-1):
            # value = b[i][j] == [0, 0, 0, 255] = why did this work?
            if (np.asarray(Colors.BLACK) == b[i][j]).all():
                fill_color = 255, 255, 255, 255

            elif (np.asarray(Colors.PLATFORM) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Platform", j, i, "\n"))
                fill_color = 0, 255, 255, 255

            elif (np.asarray(Colors.PLATFORM2) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("PlatformObject", j, i, "\n"))
                fill_color = 255, 0, 255, 255

            elif (np.asarray(Colors.PLATFORM3) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("PlatformObject2", j, i, "\n"))
                fill_color = 255, 255, 0, 255

            elif (np.asarray(Colors.WALL) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("PlatformWall", j, i, "\n"))
                fill_color = 255, 0, 0, 255

            elif (np.asarray(Colors.PLAYER) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Player", j, i, "\n"))
                fill_color = 0, 255, 0, 255

            elif (np.asarray(Colors.ENEMY) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Enemy", j, i, "\n"))
                fill_color = 0, 0, 255, 255

            elif (np.asarray(Colors.BOSS) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Boss", j, i, "\n"))
                fill_color = 0, 0, 0, 255

            filling_pixels(fill_color)
            j += increment

        i += increment

    f.close()

    # print("something:", b[1])

    # print(b)

    PIL.Image.fromarray(b, mode="RGBA").save("Level1-edited.png", format="PNG")

    del image


if __name__ == "__main__":
    main()
