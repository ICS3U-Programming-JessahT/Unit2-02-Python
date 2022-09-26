#!/usr/bin/env python3

# Created By: Jessah
# Date: Sept 26, 2022
# This program calculates the area and perimeter of a rectangle.

import math


def main():
    print("Enter and calculate the area")
    print("and perimeter of a rectangle")

    length = int(input("Enter the length (cm): "))
    width = int(input("Enter the width (cm): "))

    area = length * width
    perimeter = 2 * (length + width)

    print("")
    print("Area = {} cm^2".format(area))
    print("Perimeter = {} cm".format(perimeter))


if __name__ == "__main__":
    main()
