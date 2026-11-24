from colorgram import extract, Color


def extract_colours(image: str, num_of_colors: int) -> list[tuple[int, int, int]]:
    colors: list[Color] = extract(image, num_of_colors)
    return [(int(color.rgb.r), int(color.rgb.g), int(color.rgb.b)) for color in colors]


IMAGE_URL = "Damien Hirst Dot Painting.jpg"

COLORS = [
    (28, 102, 184),
    (231, 144, 86),
    (177, 48, 94),
    (246, 223, 92),
    (242, 77, 42),
    (147, 73, 46),
    (6, 177, 220),
    (227, 67, 110),
    (189, 12, 39),
    (240, 113, 162),
    (27, 136, 84),
    (118, 41, 29),
    (100, 178, 227),
    (5, 60, 145),
    (171, 145, 20),
    (46, 189, 146),
    (113, 190, 118),
    (80, 37, 26),
    (143, 222, 169),
    (105, 96, 194),
    (250, 163, 148),
    (220, 234, 1),
    (68, 79, 33),
    (73, 34, 59),
    (22, 43, 97),
    (37, 86, 57),
    (116, 213, 242),
    (233, 166, 184),
    (173, 184, 221),
    (38, 65, 51),
    (251, 6, 35),
]

if __name__ == "__main__":
    print(extract_colours(IMAGE_URL, 183))
