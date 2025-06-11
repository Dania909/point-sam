import numpy as np
import open3d as o3d
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file_name", type=str)
args, _ = parser.parse_known_args()

data = np.load(f"./demo/results/{args.file_name}",allow_pickle=True).item()
coord = data['xyz']
rgb = data['rgb']-np.array([0.5,0.5,0.5])
mask = data['mask']
print(mask.shape)
print(np.where(mask[0]==True)[0].shape)
mask0 = mask[0].astype(bool)
colors = np.zeros_like(coord)  # Shape: (N, 3)
colors[mask0] = [0, 0, 0]      # Red for True
colors[~mask0] = [0, 0, 1]     # Blue for False
points = np.hstack((coord,rgb))
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(coord)
point_cloud.colors = o3d.utility.Vector3dVector(colors)
o3d.visualization.draw_geometries([point_cloud])
