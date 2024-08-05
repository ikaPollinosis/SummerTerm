import subprocess
import time
import psutil
import os
from threading import Thread


def monitor_memory(process, memory_info):
    while process.is_running():
        memory_info.append(process.memory_info().rss)
        time.sleep(0.1)


def run_simulation(Ncell, log_file_path, python_interpreter):
    # 定义参数
    GenomeStructure = "C:\\Users\\ika\\PycharmProjects\\Summer\\data\\reordered_sampled_point_cloud.csv"      #修改
    Ngene = 3000        # 修改
    rateCap = 1
    rateDrop = 0
    resolution = 3     # 修改
    Ngene_for_rotation_derivation = 10
    noise = 0    # 修改
    mode = "continous"
    outpath = "C:\\Users\\ika\\PycharmProjects\\Summer\\compare\\reordered_sampled_point_cloud\\"       #修改
    csv = "compare\\reordered_sampled_point_cloud.csv"     #修改

    # 构造命令
    command = [
        python_interpreter, ".venv/Lib/site-packages/cytocraft/simulation.py",
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

    # 记录开始时间
    start_time = time.time()

    # 启动子进程运行命令
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    time.sleep(20)
    # 监控内存使用情况
    memory_info = []
    print(os.getpid())
    print(process.pid)
    children = psutil.Process(process.pid).children()
    if children:
        print(children[0].pid)
    monitor_thread = Thread(target=monitor_memory, args=(psutil.Process(children[0].pid), memory_info))
    monitor_thread.start()

    # 等待子进程完成
    output, error = process.communicate()
    monitor_thread.join()

    # 记录结束时间
    end_time = time.time()

    # 计算运行时长和最大内存使用量
    duration = end_time - start_time
    max_memory_used = max(memory_info) / (1024 * 1024)  # 转换为MB

    # 将信息写入日志文件
    with open(log_file_path, "a") as log_file:
        log_file.write(f"Running with Ncell={Ncell}\n")
        log_file.write(f"Duration: {duration} seconds\n")
        log_file.write(f"Max memory used: {max_memory_used} MB\n")
        log_file.write("Output:\n")
        log_file.write(output + "\n")
        log_file.write("Errors:\n")
        log_file.write(error + "\n")
        log_file.write("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    Ncell_values = [80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560]
    log_file_path = "C:\\Users\\ika\\PycharmProjects\\Summer\\compare\\logs\\letter_sample_method_3000_res3_log.txt"    #修改

    for Ncell in Ncell_values:
        python_interpreter = "C:\\Users\\ika\\PycharmProjects\\Summer\\.venv\\Scripts\\python.exe"
        run_simulation(Ncell, log_file_path,python_interpreter)
