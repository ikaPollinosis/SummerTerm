import pandas as pd

# 读取上传的TSV文件
file_path = 'data/letters_point_cloud.csv'
point_cloud = pd.read_csv(file_path, delimiter='\t')

# 归一化处理
def normalize(df):
    return (df - df.min()) / (df.max() - df.min())

normalized_point_cloud = point_cloud.copy()
normalized_point_cloud[['x', 'y', 'z']] = normalize(point_cloud[['x', 'y', 'z']])

# 保存归一化后的数据
normalized_file_path = 'data/normalized_letters_point_cloud.csv'
normalized_point_cloud.to_csv(normalized_file_path, index=False, sep='\t')

normalized_point_cloud.head(), normalized_file_path
