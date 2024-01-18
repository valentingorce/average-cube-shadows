from typing import Tuple
from scipy.spatial import ConvexHull
import random


def projection_area(vertices):
    # Calculate the convex hull of the projected vertices
    hull = ConvexHull(vertices)

    # Compute the area of the convex hull
    area = hull.volume  # For 2D projections, volume is equivalent to area

    return area


def random_rotat() -> Tuple[float, float, float]:
    x_rot = random.randint(0, 360)
    y_rot = random.randint(0, 360)
    z_rot = random.randint(0, 360)
    return (x_rot, y_rot, z_rot)
