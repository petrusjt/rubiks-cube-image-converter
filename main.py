from PIL import Image
from sys import argv, exit
from math import inf

if len(argv) != 5:
    print(f"""
Usage:
python {__file__} <input image file> <width> <height> <output file name>
    """)
    exit(0)

colours = {
    "YELLOW" : (242, 198,  45),
    "WHITE"  : (255, 255, 255),
    "ORANGE" : (202, 101,   0),
    "RED"    : (132,   0,   0),
    "GREEN"  : (  0, 128,   0),
    "BLUE"   : (  0,  64, 128)
}

colour_square_sums = {key : value[0]**2 + value[1]**2 + value[2]**2 for key, value in colours.items()}

with Image.open(argv[1]) as img, open(argv[4].split(".")[0] + ".txt", "w") as file:
    img = img.resize((int(argv[2]), int(argv[3])))
    print(img.width, img.height)
    for x in range(img.width):
        if x % 3 == 0:
            file.write("\n")

        for y in range(img.height):
            if y % 3 == 0:
                file.write(" ")

            r, g, b = img.getpixel((x, y))
            pixel_square_sum = r**2 + g**2 + b**2

            min = inf
            closest_item = None
            for key, value in colour_square_sums.items():
                if abs(value - pixel_square_sum) < min:
                    min = abs(value - pixel_square_sum)
                    closest_item = key
            
            img.putpixel((x,y), colours[closest_item])
            
            file.write(closest_item[0])
            
        file.write("\n")
        
            
    img.save(argv[4])
