import random

import pandas as pd
import numpy as np

random.seed(114514)
# 读取点云文件
file_path = 'data/normalized_letters_point_cloud.csv'
point_cloud = pd.read_csv(file_path, sep='\t')

# 指定采样后的点数量
num_samples = 3000  # 你可以根据需要修改这个数量

# 随机采样
sampled_point_cloud = point_cloud.sample(n=num_samples, random_state=42)

# 保存采样后的点云文件
output_file_path = 'data/sampled_point_cloud.csv'
sampled_point_cloud.to_csv(output_file_path, sep='\t', index=False)

print(f"采样后的点云文件已保存至: {output_file_path}")
