import os
import numpy as np
import open3d as o3d
import time

root_path = "./task_data_1/"

files = os.listdir(root_path)
files.sort()

vis = o3d.visualization.Visualizer()
vis.create_window()
pointcloud = o3d.geometry.PointCloud()
to_reset = True
vis.add_geometry(pointcloud)
for f in files[:]:
    if int(f[0:3]) >= 484:
        print("file >>> ", f)
        print("=============下面是图片=============")
        pcd = o3d.io.read_point_cloud(root_path + f)   # 此处读取的pcd文件,也可读取其他格式的
        pcd = np.asarray(pcd.points).reshape((-1, 3))
        pointcloud.points = o3d.utility.Vector3dVector(pcd)  # 如果使用numpy数组可省略上两行
        vis.update_geometry(pointcloud)
        if to_reset:
            vis.reset_view_point(True)
            to_reset = False
        vis.poll_events()
        vis.update_renderer()
        time.sleep(5)