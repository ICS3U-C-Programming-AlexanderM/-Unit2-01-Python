#!/usr/bin/env python3

# Created by: alex
# Created on: sep. 22, 2023
# This program calculates and displays the area and perimeter of a
# circle with radius 78 mm.
import math


def main():
    print("For a circle that has a radius")
    print("of 78 mm:")
    print("")
    print("Area = {} mm^2".format(math.pi * 78**2))
    print("Perimeter = {} mm".format(2 * math.pi * 78))


if __name__ == "__main__":
    main()
