# % color 1    color2    color3
# % color 2    color3    color1
# % color 3    color2    color2

"""
color 1    color2    color3
color 1    color3    color2

color 2    color1    color3
color 2    color3    color1

color 3    color3    color2
color 3    color2    color3

"""

# interface_1("red", "green", "blue")

"""
color 1    color2    color3
color 1    color3    color2

color 2    color1    color3
color 2    color3    color1

color 3    color3    color2
color 3    color2    color3

"""
import os
import time
import random


def interface_1(color_1, color_2, color_3):
  if color_1 == "red" and color_2 == "green" and color_3 == "blue":
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    normal = "\033[0m"
    purple = "\033[35m"
    print(
        f"{red}={green}={yellow}={normal} Music App {yellow}={green}={red}={normal}\n\n"
    )
    print("🔥 Radio Gaga 🔥\n")
    center=(f"{blue}Queen\n{normal}")
    print(f"{center:^30}")
    print(f"""PREV\v {green} NEXT \v{red} PAUSE {normal} """)

  elif color_1 == "red" and color_2 == "blue" and color_3 == "green":
    red = "\033[31m"
    blue = "\033[34m"
    green = "\033[32m"
    yellow = "\033[34m"
    normal = "\033[0m"
    purple = "\033[35m"
    print(f"{green}= {red}={yellow}={normal} Music App {yellow}={red}={green}={normal}\n")
    print("🔥 Radio Gaga 🔥\n")
    center=(f"{yellow}Queen\n{normal}")
    print(f"{center:^30}")
    print(f"PREV\v {green} NEXT \v{normal} PAUSE {red}")

  elif color_1 == "green" and color_2 == "red" and color_3 == "red":
    red = "\033[31m"
    blue = "\033[34m"
    green = "\033[32m"
    yellow = "\033[34m"
    normal = "\033[0m"
    purple = "\033[35m"





