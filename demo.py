import os
import subprocess
import sys

import cytocraft
import pkg_resources

if not os.path.exists("compare"):
    os.makedirs("compare")
if not os.path.exists("data"):
    os.makedirs("data")



# 生成点云文件
print("生成点云文件中...")
exec(open('generateData.py',encoding='utf-8').read())


# 归一化
print("对点云进行归一化中...")
exec(open('normalize.py',encoding='utf-8').read())


# 下采样
print("对点云进行下采样中...")
exec(open('sampling.py',encoding='utf-8').read())



# 对点云进行排序
print("对点云进行排序中...")
exec (open('reorder.py',encoding='utf-8').read())


# 运行模拟
print("重建运行中...")

# 假设你的库名为 'example_module'
library_name = 'cytocraft'
script_name = 'simulation.py'

# 使用 pkg_resources 来定位脚本的路径
script_path = pkg_resources.resource_filename(library_name, script_name)

# 定义参数
GenomeStructure = "data/reordered_sampled_point_cloud.csv"  # 修改
Ngene = 3000
Ncell = 240
rateCap = 1
rateDrop = 0
resolution = 4
Ngene_for_rotation_derivation = 10
noise = 0
mode = "continous"
outpath = "compare/results"
csv = "compare/output.csv"

current_virtualenv_python = sys.executable

# 构造命令
command = [
    current_virtualenv_python, script_path,
    str(GenomeStructure),
    str(Ngene),
    str(Ncell),
    str(rateCap),
    str(rateDrop),
    str(resolution),
    str(Ngene_for_rotation_derivation),
    str(noise),
    str(mode),
    str(outpath),
    str(csv)
]

# 使用 subprocess 运行命令
result = subprocess.run(command, capture_output=True, text=True)

# 打印脚本的输出
print(result.stdout)
print(result.stderr)
