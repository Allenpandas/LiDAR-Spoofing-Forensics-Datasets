# LiDAR-Spoofing-Forensics-Datasets

Despite the controversy among autonomous vehicle (AV) companies in terms of whether to incorporate the expensive LiDAR sensors in the AV design, the majority of high-autonomy AVs nowadays are equipped with LiDARs. Due to the high-accuracy that LiDAR sensors provide, LiDAR data (represented as point clouds) is used in various tasks in the AD system, including obstacle detection and localization. For example, in LiDAR localization, the LiDARs point cloud will be matched in a pre-built point cloud map to find the best matching position. However, researchers recently found that
LiDAR is vulnerable to external laser interferences. which can be exploited by attackers to iniect new points or modify/remove existing points in the point cloud. Such attacks are named as LiDAR spoofing attacks and have been a serious threat to AD localization and detection accuracy.

## 1-blackout
**Team task:** In this challenge, you are provided with a trace of LiDAR point cloud data (PCD) frames recorded during a LiDAR spoofing attack. Please find the indices of the PCD files that are spoofed by the attacker. It is known that the attacker caused a strong blinding effect on the spoofed LiDAR point cloud frames, which might cause the frames to have noisy point clouds within a close range. Please note that there are in total 3 PCD files got spoofed.

## 2-shift
**Team task:** In this challenge, you are provided with a trace of LiDAR point cloud data (PCD) frames recorded during a LiDAR spoofing attack. Please find the indices of the PCD files that are spoofed by the attacker. It is known that the attacker carefully injected a one-meter offset to one of the axes in point cloud data. Note that the attacked axis is the same in the spoofed frames. Please note that there are in total 3 PCD files got spoofed.

## 3-noise
**Team task:** In this challenge, you are provided with a trace of LiDAR point cloud data (PCD) frames and their corresponding localization results recorded during a LiDAR spoofing attack. Please find the indices of the PCD files that are spoofed by the attacker. Please find the indices of the PCD files that are spoofed by the attacker. It is known that the attacker carefully injected noise-level perturbations to the points in the point cloud data. Please note that there are in total 3 PCD files got spoofed.
