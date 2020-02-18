import numpy as np


class Point:

    def __init__(self, point_name, x, y, z):
        self.coord = np.array([x, y, z])
        self.rotateMatrix = np.array([])
        self.point_name = point_name

    def rotate_point(self, angle1, angle2, angle3):
        angle_list = [angle1, angle2, angle3]
        for i in range(3):
            angle = angle_list[i]
            self.rotateMatrix = np.array([[1, 0, 0],
                                          [0, np.cos(angle), np.sin(angle)],
                                          [0, -(np.sin(angle)), np.cos(angle)]])
            for j in range(i):
                self.rotateMatrix = self.change_matrix()
            self.coord = np.dot(self.coord, self.rotateMatrix)

    def change_matrix(self):
        buf = self.rotateMatrix
        new_matrix = np.array([buf[2], buf[0], buf[1]])
        new_matrix = np.flip(new_matrix, axis=1)
        new_matrix[:, [2, 1]] = new_matrix[:, [1, 2]]
        return new_matrix