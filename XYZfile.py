import numpy as np
from Point import Point


class XYZfile:
    def __init__(self, filename):
        self.file = open(filename+'.xyz', 'r')
        self.size = int(self.file.readline())
        self.comment = self.file.readline()
        self.points = []
        self.angles = []

    def get_points(self):
        for i in range(self.size):
            line = self.file.readline().split()
            x = np.float64(line[1])
            y = np.float64(line[2])
            z = np.float64(line[3])
            new_point = Point(line[0], x, y, z)
            self.points.append(new_point)

    def get_angles(self, angles):
        self.angles = angles.split()
        for i in range(3):
            self.angles[i] = int(self.angles[i])*np.pi/180

    def rotate45degrees(self):
        for i in range(self.size):
            self.points[i].rotate_point(np.pi / 4, np.pi / 4, np.pi / 4)

    def rotate_points(self):
        for i in range(self.size):
            self.points[i].rotate_point(self.angles[0], self.angles[1], self.angles[2])

    def save_xyz_file(self, new_name):
        self.file.close()
        self.file = open(new_name+'.xyz', 'w')
        self.file.write(str(self.size))
        self.file.write('\n')
        self.file.write(self.comment)
        for i in range(self.size):
            x = str(self.points[i].coord[0])
            y = str(self.points[i].coord[1])
            z = str(self.points[i].coord[2])
            self.file.write(self.points[i].point_name + ' ' + x + ' ' + y + ' ' + z + '\n')