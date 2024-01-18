import numpy as np


class Cube:
    def __init__(self, side_length):
        self.side_length = side_length
        # Define the initial cube vertices
        self.vertices = np.array(
            [
                [0, 0, 0],
                [0, side_length, 0],
                [side_length, side_length, 0],
                [side_length, 0, 0],
                [0, 0, side_length],
                [0, side_length, side_length],
                [side_length, side_length, side_length],
                [side_length, 0, side_length],
            ]
        )

    def rotate(self, angle, axis):
        # Convert angle to radians
        angle_rad = np.radians(angle)

        # Define rotation matrix based on the given axis
        if axis == "x":
            rotation_matrix = np.array(
                [
                    [1, 0, 0],
                    [0, np.cos(angle_rad), -np.sin(angle_rad)],
                    [0, np.sin(angle_rad), np.cos(angle_rad)],
                ]
            )
        elif axis == "y":
            rotation_matrix = np.array(
                [
                    [np.cos(angle_rad), 0, np.sin(angle_rad)],
                    [0, 1, 0],
                    [-np.sin(angle_rad), 0, np.cos(angle_rad)],
                ]
            )
        elif axis == "z":
            rotation_matrix = np.array(
                [
                    [np.cos(angle_rad), -np.sin(angle_rad), 0],
                    [np.sin(angle_rad), np.cos(angle_rad), 0],
                    [0, 0, 1],
                ]
            )
        else:
            raise ValueError("Invalid axis. Use 'x', 'y', or 'z'.")

        # Apply rotation to all vertices
        self.vertices = np.dot(self.vertices, rotation_matrix)

    def project(self, plane):
        # Project vertices onto the specified plane
        if plane == "xy":
            return self.vertices[:, :2]  # Project onto the xy plane
        elif plane == "yz":
            return self.vertices[:, 1:]  # Project onto the yz plane
        elif plane == "xz":
            return np.column_stack(
                (self.vertices[:, 0], self.vertices[:, 2])
            )  # Project onto the xz plane
        else:
            raise ValueError("Invalid plane. Use 'xy', 'yz', or 'xz'.")
