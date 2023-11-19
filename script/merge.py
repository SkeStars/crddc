import os
import shutil
import argparse

# 创建命令行参数解析器
parser = argparse.ArgumentParser()
parser.add_argument('--result1', help='Directory 1')
parser.add_argument('--result2', help='Directory 2')
parser.add_argument('--output', help='Output directory')
args = parser.parse_args()

# 获取两个目录中的文件名
files1 = set(os.listdir(args.dir1))
files2 = set(os.listdir(args.dir2))

# 找出两个目录中都存在的文件
common_files = files1.intersection(files2)

# 对于每个共享的文件
for filename in common_files:
    file1 = os.path.join(args.dir1, filename)
    file2 = os.path.join(args.dir2, filename)

    # 计算每个文件的行数
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = len(f1.readlines())
        lines2 = len(f2.readlines())

    # 判断哪个文件的行数最多，并将其复制到输出目录
    if lines1 > lines2:
        shutil.copy(file1, args.output)
    else:
        shutil.copy(file2, args.output)