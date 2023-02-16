"""
使用zfill函数对文件名进行补齐，如100.pcd不变，1.pcd修改为001.pcd
"""
import os


def handle_files():
    # 获取旧的文件名
    old_names = os.listdir(path)
    for old_name in old_names:
        if old_name.endswith('.pcd'):  # 获取文件后缀
            new_name = old_name.zfill(7)  # zfill字符串左侧补齐
            os.rename(os.path.join(path, old_name), os.path.join(path, new_name))
            print(old_name, "has been renamed successfully! New name is :", new_name)


if __name__ == '__main__':
    path = './task_data_1'
    handle_files()