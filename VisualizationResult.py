import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

def load_data(file_path):
    data = pd.ExcelFile(file_path)
    sheet_1 = data.parse('0.2')
    sheet_2 = data.parse('0.4')
    sheet_3 = data.parse('0.6')
    sheet_4 = data.parse('0.8')
    sheet_5 = data.parse('1.0')
    return [sheet_1, sheet_2, sheet_3, sheet_4, sheet_5]


import matplotlib.pyplot as plt

def plot_rmsd(dataframes, labels):
    plt.figure(figsize=(10, 6))
    for df, label in zip(dataframes, labels):
        plt.plot(df['ncell 模拟细胞数'], df['RMSD'], marker='o', label=f'{label} noise level')
    plt.xlabel('Number of simulated cells (ncell)')
    plt.ylabel('RMSD')
    plt.title('RMSD vs. Number of Simulated Cells (gaussian noise, resol=3)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_spearman(dataframes, labels):
    plt.figure(figsize=(10, 6))
    for df, label in zip(dataframes, labels):
        plt.plot(df['ncell 模拟细胞数'], df['Spearman相关系数'], marker='o', linestyle='--', label=f'{label} points')
    plt.xlabel('Number of simulated cells (ncell)')
    plt.ylabel('Spearman Correlation Coefficient')
    plt.title('Spearman Correlation vs. Number of Simulated Cells (gaussian noise, resol=3)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_resources(dataframes, labels):
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax2 = ax1.twinx()
    for df, label in zip(dataframes, labels):
        ax1.plot(df['ncell 模拟细胞数'], df['时间(s)'], marker='s', label=f'Time {label} points')
        #ax2 = ax1.twinx()
        ax2.plot(df['ncell 模拟细胞数'], df['消耗内存(MB)'], marker='^', linestyle=':', label=f'Memory {label} points')

    ax1.set_xlabel('Number of Simulated Cells (ncell)')
    ax1.set_ylabel('Time (s)')
    ax2.set_ylabel('Memory Consumption (MB)')
    ax1.set_title('Resource Consumption vs. Number of Simulated Cells')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax1.grid(True)
    plt.show()


def heatmap_rmsd_spearman(dataframes, labels):
    plt.figure(figsize=(14, 7))
    for i, (df, label) in enumerate(zip(dataframes, labels), 1):
        plt.subplot(1, len(dataframes), i)
        heatmap_data = df.pivot(index="ncell 模拟细胞数", columns="RMSD", values="Spearman相关系数")
        sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title(f'{label} points')
        plt.xlabel('RMSD')
        plt.ylabel('Number of Simulated Cells')
    plt.tight_layout()
    plt.show()

def plot_3d(dataframes, labels):
    fig = plt.figure(figsize=(18, 6))
    for i, (df, label) in enumerate(zip(dataframes, labels), 1):
        ax = fig.add_subplot(1, len(dataframes), i, projection='3d')
        sc = ax.scatter(df['RMSD'], df['Spearman相关系数'], df['ncell 模拟细胞数'], c=df['ncell 模拟细胞数'], cmap='viridis')
        ax.set_xlabel('RMSD')
        ax.set_ylabel('Spearman Correlation')
        ax.set_zlabel('Number of Simulated Cells')
        plt.title(f'{label} points')
    plt.colorbar(sc)
    plt.show()


def boxplot_comparison(dataframes, labels, column):
    plt.figure(figsize=(10, 6))
    data = [df[column] for df in dataframes]
    plt.boxplot(data, labels=[f'{label} points' for label in labels])
    plt.title(f'{column} Distribution by Sample Points')
    plt.ylabel(column)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    file_path = 'data/gaussian_res3.xlsx'
    dataframes = load_data(file_path)
    labels = [0.2, 0.4, 0.6, 0.8, 1.0]
    #plot_resources(dataframes, labels)
    #heatmap_rmsd_spearman(dataframes, labels)
    #plot_3d(dataframes, labels)
    plot_rmsd(dataframes, labels)
    plot_spearman(dataframes, labels)