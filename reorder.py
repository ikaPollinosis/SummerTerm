import numpy as np
import pandas as pd
from scipy.spatial import distance, ConvexHull

def load_point_cloud(file_path):
    # 读取TSV文件并加载点云数据
    df = pd.read_csv(file_path, sep='\t')
    points = df[['x', 'y', 'z']].values
    return points, df

def find_nearest_point(current_point, points, visited):
    # 找到当前点的最近未访问点
    min_dist = float('inf')
    nearest_point_index = -1
    for i, point in enumerate(points):
        if not visited[i]:
            dist = distance.euclidean(current_point, point)
            if dist < min_dist:
                min_dist = dist
                nearest_point_index = i
    return nearest_point_index

def find_boundary_point(points):
    # 计算凸包并返回其中一个点作为边界点
    hull = ConvexHull(points)
    boundary_point_index = hull.vertices[0]  # 选择凸包上的第一个点
    return boundary_point_index

def sort_point_cloud(points):
    # 从边界点开始进行遍历并排序
    sorted_points = []
    visited = [False] * len(points)
    current_index = find_boundary_point(points)
    while len(sorted_points) < len(points):
        current_point = points[current_index]
        sorted_points.append(current_point)
        visited[current_index] = True
        next_index = find_nearest_point(current_point, points, visited)
        current_index = next_index
    return np.array(sorted_points)

def save_sorted_points(file_path, sorted_points, df):
    # 保存排序后的点云数据到新的TSV文件
    sorted_df = pd.DataFrame(sorted_points, columns=['x', 'y', 'z'])
    sorted_df.to_csv(file_path, sep='\t', index=False)

def main(input_file, output_file):
    points, df = load_point_cloud(input_file)
    sorted_points = sort_point_cloud(points)
    save_sorted_points(output_file, sorted_points, df)

if __name__ == '__main__':
    input_file = 'data/sampled_point_cloud.csv'  # 输入文件路径
    output_file = 'data/reordered_sampled_point_cloud.csv'  # 输出文件路径
    main(input_file, output_file)
