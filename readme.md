# 完整流程的demo脚本
首先安装依赖库，对环境进行配置
```shell
pip install -r requirements.txt
```

在环境配置完成后，运行目录下的`demo.py`脚本，可以完成整个流程的演示。
```shell
python demo.py
```
生成的点云数据保存在`data`目录下，重建结果保存在`compare/results/`目录下。


# 模块介绍


## generateData.py
该部分是三维点云的生成脚本，根据指定的字符串生成对应字母的点云文件，并保存data目录下的.csv文件中。

## sampling.py
该模块按照指定的数量将点云数据进行降采样处理。

## normalize.py
该模块对点云数据进行归一化处理。

## reorder.py
该模块对点云数据进行遍历，并按照遍历顺序进行重排序。

## visualization.py
该模块使用Open3D库，对点云数据进行三维可视化。

## run.py
该模块是重建的批量运行脚本，使用给定的参数列表，调用CytoCraft库进行不同参数下的批量重建， 同时监测资源的消耗情况。结果保存在compare目录下。（需要修改才能运行）
# 详细运行流程
### 1. 环境配置
本程序运行在Python3.10.1环境下
```shell
Python 3.10.1
```
同时，需要安装以下依赖库：
```shell
anndata==0.10.8
cytocraft==0.0.8
matplotlib==3.7.2
numpy==1.23.5
open3d==0.18.0
pandas==2.2.2
Pillow==10.4.0
plotly==5.22.0
psutil==5.9.8
scipy==1.14.0
seaborn==0.13.2
Shapely==2.0.5
```
文件目录下提供了`requirements.txt`文件，可以使用以下命令安装依赖库：
```shell
pip install -r requirements.txt
```

### 2. 生成点云数据
运行`generateData.py`脚本，生成点云数据。可以通过修改`generateData.py`脚本中的`text`变量，来生成不同的点云数据。
```shell
python generateData.py
```

### 3. 归一化
运行`normalize.py`脚本，对点云数据进行归一化处理。
```shell
python normalize.py
```

### 4. 降采样
运行`sampling.py`脚本，对点云数据进行降采样处理。
```shell
python sampling.py
```

### 5. 重排序
运行`reorder.py`脚本，对点云数据进行重排序。
```shell
python reorder.py
```

### 6. 可视化
运行`visualization.py`脚本，对点云数据进行三维可视化。
```shell
python visualization.py
```

### 7. 重建
运行`run.py`脚本，对点云数据进行批量重建。
```shell
python run.py
```
**以上流程除配置环境外，其他步骤都可以通过`demo.sh`脚本一键完成。**
