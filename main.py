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


def main():
    filename = "Level1.png"

    image = PIL.Image.open(filename)

    size = width, height = image.size

    print(size)

    colors = image.getcolors(maxcolors=256) # how many pixels use what color

    # print(list(image.getdata()))


    a = np.asarray(image)

    print("Shape of the array is : ", np.shape(a))

    # print(PIL.features.pilinfo())

    # print(list(image.getdata()))

    # print(a)
    print(colors)

    b = a.copy()

    b.setflags(write=1) # making array writable


    print("something:", len(b[1079]))

    f = open("coordinates.txt", "w")

    for i in range(0, len(b)-60, 50):
        for j in range(0, len(b[i]), 50):
            # value = b[i][j] == [0, 0, 0, 255]
            # print(type(value))
            if (np.asarray(Colors.BLACK) == b[i][j]).all():
                for k in range(50):
                    for h in range(50):
                        b[i+k][j+h] = 255, 255, 255, 255

            # print(Colors.BLACK == b[i][j])

            elif (np.asarray(Colors.PLATFORM) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Platform", j, i, "\n"))
                b[i][j] = 0, 255, 255, 255

            elif (np.asarray(Colors.PLATFORM2) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("PlatformObject", j, i, "\n"))
                b[i][j] = 255, 0, 255, 255

            elif (np.asarray(Colors.PLATFORM3) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("PlatformObject2", j, i, "\n"))
                b[i][j] = 255, 255, 0, 255

            elif (np.asarray(Colors.WALL) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("PlatformWall", j, i, "\n"))
                b[i][j] = 255, 0, 0, 255

            elif (np.asarray(Colors.PLAYER) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Player", j, i, "\n"))
                b[i][j] = 0, 255, 0, 255

            elif (np.asarray(Colors.ENEMY) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Enemy", j, i, "\n"))
                b[i][j] = 0, 0, 255, 255

            elif (np.asarray(Colors.BOSS) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Boss", j, i, "\n"))
                b[i][j] = 0, 0, 0, 255

    f.close()

    # print("something:", b[1])

    # print(b)

    PIL.Image.fromarray(b, mode="RGBA").save("Level1-edited.png", format="PNG")

    del image


if __name__ == "__main__":
    main()
