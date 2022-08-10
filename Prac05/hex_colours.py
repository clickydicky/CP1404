"""
CP1404 Practical
Get colour codes from colour name
"""

COLOUR_CODES = {"Absolute Zero": "	#0048ba", "Amethyst": "#9966cc", "Apricot": "#fbceb1", "Banana Mania": "#fae7b5",
                "Brick Red": "#cb4154", "Bright Green": "#66ff00", "Buff": "#f0dc82", "Cadet Grey": "#91a3b0",
                "Candy Apple Red": "#ff0800", "Carrot Orange": "#ed9121"}

colour_name = input("Enter a colour name(case sensitive): ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
