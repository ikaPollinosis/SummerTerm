import random

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


def generate_3d_point_cloud_for_letter(letter, canvas_size=1000, num_points=50000, thickness=150):
    # Create a canvas to draw the letter on
    canvas = Image.new('L', (canvas_size, canvas_size), 0)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("Comic.ttf", 800)  # Increase font size for larger letters

    # Draw the letter on the canvas
    draw.text((canvas_size // 4, 100), letter, 255, font=font)

    # Convert the image to a numpy array and normalize it
    image = np.array(canvas) / 255.0

    # Generate random points within the canvas
    x = np.random.rand(num_points) * canvas_size
    y = np.random.rand(num_points) * canvas_size
    z = (np.random.rand(num_points) - 0.5) * thickness  # Reduce thickness by limiting z range

    # Filter points based on the image intensity
    points = np.vstack((x, y, z)).T
    mask = image[y.astype(int), x.astype(int)] > np.random.rand(num_points)
    points = points[mask]

    # Rotate points randomly
    points = rotate_points_randomly(points)

    return points


def rotate_points_randomly(points):
    # Generate random angles for rotation
    angle_x = np.random.uniform(0, 2 * np.pi)
    angle_y = np.random.uniform(0, 2 * np.pi)
    angle_z = np.random.uniform(0, 2 * np.pi)

    # Create rotation matrices
    R_x = np.array([[1, 0, 0],
                    [0, np.cos(angle_x), -np.sin(angle_x)],
                    [0, np.sin(angle_x), np.cos(angle_x)]])

    R_y = np.array([[np.cos(angle_y), 0, np.sin(angle_y)],
                    [0, 1, 0],
                    [-np.sin(angle_y), 0, np.cos(angle_y)]])

    R_z = np.array([[np.cos(angle_z), -np.sin(angle_z), 0],
                    [np.sin(angle_z), np.cos(angle_z), 0],
                    [0, 0, 1]])

    # Combine rotations into a single matrix
    R = R_x @ R_y @ R_z

    # Apply rotation to points
    rotated_points = points @ R.T

    return rotated_points


def plot_3d_point_cloud(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1)
    plt.show()


def save_point_cloud_to_file(points, filename):
    header = "x\ty\tz"
    np.savetxt(filename, points, delimiter='\t',header=header, comments='')


if __name__ == "__main__":
    letters = "TS"  # Input multiple letters here
    all_points = []
    random.seed(114514)
    # Generate and rotate point cloud for each letter
    for letter in letters:
        points = generate_3d_point_cloud_for_letter(letter)
        all_points.append(points)

    # Combine all points into a single array
    all_points = np.vstack(all_points)

    plot_3d_point_cloud(all_points)
    filename = "data/letters_point_cloud.csv"
    save_point_cloud_to_file(all_points, filename)
    print(f"Point cloud for letters '{letters}' saved to {filename}")
