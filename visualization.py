import numpy as np
import open3d as o3d

def load_point_cloud_from_file(filename):
    # Load point cloud data from a TSV file
    points = np.loadtxt(filename, delimiter='\t', skiprows=1)  # skiprows=1 to skip the header
    return points

def visualize_point_cloud(points):
    # Create an Open3D point cloud object
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)

    # Visualize the point cloud
    o3d.visualization.draw_geometries([point_cloud])

if __name__ == "__main__":
    filename = "data/letters_point_cloud.csv"  # Path to your point cloud TSV file
    points = load_point_cloud_from_file(filename)
    visualize_point_cloud(points)
