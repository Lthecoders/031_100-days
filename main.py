import os
import time
import random

print("\n\n\n----Getting your both interface ready.....\n")
print("please wait....")
time.sleep(5)
os.system("clear")


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
    center = (f"{blue}Queen\n{normal}")
    print(f"{center:^30}")
    print(f"""PREV\v {green} NEXT \v{red} PAUSE {normal} """)

  elif color_1 == "red" and color_2 == "blue" and color_3 == "green":
    red = "\033[31m"
    blue = "\033[34m"
    green = "\033[32m"
    yellow = "\033[34m"
    normal = "\033[0m"
    purple = "\033[35m"
    print(
        f"{green}= {red}={yellow}={normal} Music App {yellow}={red}={green}={normal}\n"
    )
    print("🔥 Radio Gaga 🔥\n")
    center = (f"{yellow}Queen\n{normal}")
    print(f"{center:^30}")
    print(f"PREV\v {green} NEXT \v{normal} PAUSE {red}")
    """
    follow this patter
color 2    color1    color3
color 2    color3    color1

color 3    color3    color2
color 3    color2    color3

"""

  elif color_1 == "green" and color_2 == "red" and color_3 == "blue":
    red = "\033[31m"
    blue = "\033[34m"
    green = "\033[32m"
    yellow = "\033[34m"
    normal = "\033[0m"
    purple = "\033[35m"
    # shuffle this colors print(f"{green}= {red}={yellow}={normal} Music App {yellow}={red}={green}={normal}\n")
    print(
        f"{red}= {yellow}={green}={normal} Music App {green}={yellow}={red}={normal}\n"
    )
    print("🔥 Radio Gaga 🔥\n")
    center = (f"{green}Queen\n{normal}")
    print(f"{center:^30}")
    print(f"PREV\v {normal} NEXT \v{red} PAUSE {green}")

  elif color_1 == "green" and color_2 == "blue" and color_3 == "red":
    red = "\033[31m"
    blue = "\033[34m"
    green = "\033[32m"
    yellow = "\033[34m"
    normal = "\033[0m"
    purple = "\033[35m"
    # shuffle this colors print(f"{green}= {red}={yellow}={normal} Music App {yellow}={red}={green}={normal}\n")
    print(
        f"{green}= {red}={yellow}={normal} Music App {yellow}={green}={red}={normal}\n"
    )
    print("🔥 Radio Gaga 🔥\n")
    center = (f"{red}Queen\n{normal}")
    print(f"{center:^30}")
    print(f"PREV\v {green} NEXT \v{yellow} PAUSE {red}")

  elif color_1 == "blue" and color_2 == "green" and color_3 == "red":
    red = "\033[31m"
    blue = "\033[34m"
    green = "\033[32m"
    yellow = "\033[34m"
    normal = "\033[0m"
    purple = "\033[35m"
    # shuffle this colors print(f"{green}= {red}={yellow}={normal} Music App {yellow}={red}={green}={normal}\n")
    print(
        f"{yellow}= {red}={green}={normal} Music App {green}={red}={yellow}={normal}\n"
    )
    print("🔥 Radio Gaga 🔥\n")
    center = (f"{blue}Queen\n{normal}")
    print(f"{center:^30}")
    print(f"PREV\v {red} NEXT \v{green} PAUSE {yellow}")

  elif color_1 == "blue" and color_2 == "red" and color_3 == "green":
    red = "\033[31m"
    blue = "\033[34m"
    green = "\033[32m"
    yellow = "\033[34m"
    normal = "\033[0m"
    purple = "\033[35m"
    # shuffle this colors print(f"{green}= {red}={yellow}={normal} Music App {yellow}={red}={green}={normal}\n")
    print(
        f"{yellow}= {green}={red}={normal} Music App {red}={green}={yellow}={normal}\n"
    )
    print("🔥 Radio Gaga 🔥\n")
    center = (f"{blue}Queen\n{normal}")
    print(f"{center:^30}")
    print(f"PREV\v {yellow} NEXT \v{green} PAUSE {red}")


print("\n\nInterface 1")
print("-------------\n")
"--------------------------IMPORTANT MESSAGE--------------"
"---------!!!!!YOU CAN PICK COLOR ORDER FROM RED, BLUE AND GREEN IN THE FUNCTION!!!!!---------"
"-----FOR NOW HERE I AM SUING RED GREEN BLLUE you can pick any order from this this 3 color"
"you can pick red, green, blue or blue, red, green or any combination of these 3 colors"
interface_1("red", "green",
            "blue")  #############################################

#---------> interference 2


# keep going the process of shuffling the colors
def interface_2(color_1, color_2, color_3):
  red = "\033[31m"
  green = "\033[32m"
  yellow = "\033[33m"
  blue = "\033[34m"
  normal = "\033[0m"
  purple = "\033[35m"
  if color_1 == "red" and color_2 == "green" and color_3 == "blue":
    print("                    WELCOME TO")
    print(f"{blue}               ----  ARMBOOK  ----{normal}\n")
    allin1 = (f"{yellow}Definitely not a rip off of\n")
    allin2 = (f"{yellow}a certain other social\n")
    allin3 = (f"{yellow}networking site.{normal}\n")
    print(f"{allin1:>55}")
    print(f"{allin2:>55}")
    print(f"{allin3:>60}")
    allinx = (f"{red}Honest.{normal}")
    alline4 = (f"{normal}Username: ")
    alline5 = (f"{normal}Password: ")
    print(f"{allinx:^58}\n")
    print(f"{alline4:^55}")
    print(f"{alline5:^55}")

  elif color_1 == "red" and color_2 == "blue" and color_3 == "green":
    # shuffle the colors
    print("                    WELCOME TO")
    print(f"{green}               ----  ARMBOOK  ----{normal}\n")
    allin1 = (f"{purple}Definitely not a rip off of\n")
    allin2 = (f"{purple}a certain other social\n")
    allin3 = (f"{purple}networking site.{normal}\n")
    print(f"{allin1:>55}")
    print(f"{allin2:>55}")
    print(f"{allin3:>60}")
    allinx = (f"{blue}Honest.{normal}")
    alline4 = (f"{normal}Username: ")
    alline5 = (f"{normal}Password: ")
    print(f"{allinx:^58}\n")
    print(f"{alline4:^55}")
    print(f"{alline5:^55}")

  elif color_1 == "green" and color_2 == "red" and color_3 == "blue":
    # shuffle the colors
    print("                    WELCOME TO")
    print(f"{blue}               ----  ARMBOOK  ----{normal}\n")
    allin1 = (f"{red}Definitely not a rip off of\n")
    allin2 = (f"{red}a certain other social\n")
    allin3 = (f"{red}networking site.{normal}\n")
    print(f"{allin1:>55}")
    print(f"{allin2:>55}")
    print(f"{allin3:>60}")
    allinx = (f"{green}Honest.{normal}")
    alline4 = (f"{normal}Username: ")
    alline5 = (f"{normal}Password: ")
    print(f"{allinx:^58}\n")
    print(f"{alline4:^55}")
    print(f"{alline5:^55}")

  elif color_1 == "green" and color_2 == "blue" and color_3 == "red":
    # shuffle the colors
    print("                    WELCOME TO")
    print(f"{red}               ----  ARMBOOK  ----{normal}\n")
    allin1 = (f"{blue}Definitely not a rip off of\n")
    allin2 = (f"{blue}a certain other social\n")
    allin3 = (f"{blue}networking site.{normal}\n")
    print(f"{allin1:>55}")
    print(f"{allin2:>55}")
    print(f"{allin3:>60}")
    allinx = (f"{green}Honest.{normal}")
    alline4 = (f"{normal}Username: ")
    alline5 = (f"{normal}Password: ")
    print(f"{allinx:^58}\n")
    print(f"{alline4:^55}")
    print(f"{alline5:^55}")

  elif color_1 == "blue" and color_2 == "green" and color_3 == "red":
    # shuffle the colors
    print("                    WELCOME TO")
    print(f"{red}               ----  ARMBOOK  ----{normal}\n")
    allin1 = (f"{green}Definitely not a rip off of\n")
    allin2 = (f"{green}a certain other social\n")
    allin3 = (f"{green}networking site.{normal}\n")
    print(f"{allin1:>55}")
    print(f"{allin2:>55}")
    print(f"{allin3:>60}")
    allinx = (f"{blue}Honest.{normal}")
    alline4 = (f"{normal}Username: ")
    alline5 = (f"{normal}Password: ")
    print(f"{allinx:^58}\n")
    print(f"{alline4:^55}")
    print(f"{alline5:^55}")

  elif color_1 == "blue" and color_2 == "red" and color_3 == "green":
    # shuffle the colors
    print("                    WELCOME TO")
    print(f"{green}               ----  ARMBOOK  ----{normal}\n")
    allin1 = (f"{red}Definitely not a rip off of\n")
    allin2 = (f"{red}a certain other social\n")
    allin3 = (f"{red}networking site.{normal}\n")
    print(f"{allin1:>55}")
    print(f"{allin2:>55}")
    print(f"{allin3:>60}")
    allinx = (f"{blue}Honest.{normal}")
    alline4 = (f"{normal}Username: ")
    alline5 = (f"{normal}Password: ")
    print(f"{allinx:^58}\n")
    print(f"{alline4:^55}")
    print(f"{alline5:^55}")


print(
    "\n\n\n\n------x--------x--------x--------x--------x--------x--------x--------x--------x--------x--------x--------x--------x--------x--------x--------x"
)
print("\n\nInterface 2")
print("-------------\n")
"--------------------------IMPORTANT MESSAGE--------------"
"---------!!!!!YOU CAN PICK COLOR ORDER FROM RED, BLUE AND GREEN IN THE FUNCTION!!!!!---------"
"-----FOR NOW HERE I AM SUING GREEN RED BLLUE you can pick any order from this this 3 color"
"you can pick red, green, blue or blue, red, green or any combination of these 3 colors"

interface_2(
    "green", "red",
    "blue")  #############################################################
