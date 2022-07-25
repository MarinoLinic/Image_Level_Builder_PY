import PIL.Image
import PIL.features
import numpy as np
import os


class TextVariables:
    def __init__(self, x, y, w, h):
        self.platform = "Platform.generateRectangle({{x: {},\ty: {},\tw: {},\th: {},\t sprite: {{default: `${{PATH_SPRITES}}/Level 2/Platform.png`}}}});".format(
            x, y, w, h)

        self.enemy_melee = "{{x: {}, y: {}, w: {}, h: {}, jumpHeight: 0, jumps: 0, movespeed: 3, seekingMovespeedFactor: 1.5, "
        "HP: 50, contactDamage: 15, patrolDistance: 500, attackCooldown: 3000}},".format(x, y, w, h)

        # self.enemy_ranged = "{{x: {}, y: {}, w: {}, h: {}, jumpHeight: 0, jumps: 0, movespeed: 0, HP: 30, contactDamage: 5, patrolDistance: 1500, attackCooldown: 1000, weapon: new Weapon({{"
        # "\n\tname: \"Izazgrabi\",\n"
        # "\n\tdamage: 10,"
        # "\n\tsound: createSound(`${PATH_AUDIO}/Weapons/Ranged/Izazgrabi/Fire.mp3`),"
        # "\n\tmissileSpeed: 7,"
        # "\n\tmissileSize: {w: 30, h: 15},"
        # "\n\tfireEffectSize: {w: 64, h: 64},"
        # "\n\tmissileSprite: {"
        # "\n\t\tleft: `${PATH_SPRITES}/Weapons/Ranged/Izazgrabi/MissileLeft.png`,"
        # "\n\t\tright: `${PATH_SPRITES}/Weapons/Ranged/Izazgrabi/MissileRight.png`,"
        # "\n\t\tup: `${PATH_SPRITES}/Weapons/Ranged/Izazgrabi/MissileUp.png`,"
        # "\n\t\tfire: {"
        # "\n\t\t\tleft: `${PATH_SPRITES}/Weapons/Ranged/Izazgrabi/FiredLeft.png`,"
        # "\n\t\t\tright: `${PATH_SPRITES}/Weapons/Ranged/Izazgrabi/FiredRight.png`,"
        # "\n\t\t}"
        # "\n\t},"
        # "\n})},".format(x, y, w, h)


class TextPaste:
    def __init__(self, text):
        self.text = text


class PixelObject:
    def __init__(self, file_name, color):
        self.file_name = file_name
        self.texture = PIL.Image.open(file_name)
        self.size = width, height = self.texture.size
        self.color = color
        self.inverted_color = invert_color(color)


class Colors:
    WHITE = [255, 255, 255, 255]
    BLACK = [0, 0, 0, 255]
    PLATFORM = [128, 84, 148, 255]
    PLATFORM2 = [244, 58, 160, 255]
    PLATFORM3 = [211, 18, 241, 255]
    WALL = [51, 24, 231, 255]
    HEALTHORB = [52, 216, 208, 255]
    LIFEORB = [222, 216, 208, 255]
    PLAYER = [27, 233, 42, 255]
    ENEMY = [241, 0, 0, 255]
    BOSS = [120, 0, 0, 255]


def invert_color(color):
    return [255 - color[0], 255 - color[1], 255 - color[2], color[3] - 0]


def filling_pixels(fill_color):
    for k in range(increment):
        for h in range(increment):
            b[i + k][j + h] = fill_color


# ground = PixelObject("ground.png", Colors.PLATFORM)


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
    increment = 50

    global b
    b = a.copy()
    b.setflags(write=1)  # making array writable

    f = open("coordinates.txt", "w")
    while i < len(b) - (increment - 1):
        j = 0
        while j < len(b[i]) - (increment - 1):
            # value = b[i][j] == [0, 0, 0, 255] = why did this work?
            if (np.asarray(Colors.BLACK) == b[i][j]).all():
                fill_color = invert_color(Colors.BLACK)

            elif (np.asarray(Colors.PLATFORM) == b[i][j]).all():
                # f.write("{} - X: {}, Y: {}{}".format("Platform", j, i, "\n"))
                f.write(TextVariables(j, i, 50, 50).platform)
                fill_color = invert_color(Colors.PLATFORM)

            elif (np.asarray(Colors.PLATFORM2) == b[i][j]).all():
                # f.write("{} - X: {}, Y: {}{}".format("PlatformObject", j, i, "\n"))
                f.write(TextVariables(j, i, 50, 50).platform)
                fill_color = invert_color(Colors.PLATFORM)

            elif (np.asarray(Colors.PLATFORM3) == b[i][j]).all():
                # f.write("{} - X: {}, Y: {}{}".format("PlatformObject2", j, i, "\n"))
                f.write(TextVariables(j, i, 50, 50).platform)
                fill_color = invert_color(Colors.PLATFORM)

            elif (np.asarray(Colors.WALL) == b[i][j]).all():
                # f.write("{} - X: {}, Y: {}{}".format("PlatformWall", j, i, "\n"))
                f.write("Platform.generateRectangle({{x: {},{}y: {},{}w: 50, h: 50, "
                        "sprite: {{default: `${{PATH_SPRITES}}/Level 2/Ground_450x100.png`}}}});{}"
                        .format(j, "\t", i, "\t", "\n"))
                fill_color = invert_color(Colors.WALL)

            elif (np.asarray(Colors.PLAYER) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Player", j, i, "\n"))
                fill_color = invert_color(Colors.PLAYER)

            elif (np.asarray(Colors.ENEMY) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Enemy", j, i, "\n"))
                fill_color = invert_color(Colors.ENEMY)

            elif (np.asarray(Colors.BOSS) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Boss", j, i, "\n"))
                fill_color = invert_color(Colors.BOSS)

            elif (np.asarray(Colors.LIFEORB) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Boss", j, i, "\n"))
                fill_color = invert_color(Colors.LIFEORB)

            elif (np.asarray(Colors.HEALTHORB) == b[i][j]).all():
                f.write("{} - X: {}, Y: {}{}".format("Boss", j, i, "\n"))
                fill_color = invert_color(Colors.HEALTHORB)

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
