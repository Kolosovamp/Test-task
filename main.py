from XYZfile import XYZfile
import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?')
    parser.add_argument('angle1', nargs='?')
    parser.add_argument('angle2', nargs='?')
    parser.add_argument('angle3', nargs='?')
    return parser


parser = create_parser()
anglespace = parser.parse_args()
angles = ''
if anglespace.filename:
    file = XYZfile(anglespace.filename)
    file.get_points()
    file.rotate45degrees()
    file.save_xyz_file(anglespace.filename+'_v2')
    if anglespace.angle1 and anglespace.angle2 and anglespace.angle3:
        angles += anglespace.angle1 + ' ' + anglespace.angle2 + ' ' + anglespace.angle3
        file.get_angles(angles)
        file.rotate_points()
        file.save_xyz_file(anglespace.filename+'_v3')
    file.file.close()
else:
    print('Missing file name')
    sys.exit()


