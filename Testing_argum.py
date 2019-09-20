import math
import argparse

parser = argparse.ArgumentParser(description='Calculate vol. of Cylinder')
parser.add_argument('-r', '--rad', type=int, help='Radius of Cylinder')
parser.add_argument('-H', '--height', type=int, help='Height of Cylinder')
args = parser.parse_args()


def cylinder_value(radius, height):
    vol = (math.pi) * (radius ** 2) * height
    return vol


if __name__ == '__main__':
    print cylinder_value(args.rad, args.height)
