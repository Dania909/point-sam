import numpy as np
import open3d as o3d

def load_ply(filename):
    with open(filename, "r") as rf:
        while True:
            try:
                line = rf.readline()
            except:
                raise NotImplementedError
            if "end_header" in line:
                break
            if "element vertex" in line:
                arr = line.split()
                num_of_points = int(arr[2])

        # print("%d points in ply file" %num_of_points)
        points = np.zeros([num_of_points, 6])
        for i in range(points.shape[0]):
            point = rf.readline().split()
            assert len(point) == 6
            points[i][0] = float(point[0])
            points[i][1] = float(point[1])
            points[i][2] = float(point[2])
            points[i][3] = float(point[3])
            points[i][4] = float(point[4])
            points[i][5] = float(point[5])
    rf.close()
    del rf
    return points
    
    
def load_pointcloud_with_color(npy_path):
    """
    Loads a point cloud from a .npy file and ensures it has RGB color.
    
    Parameters:
        npy_path (str): Path to the .npy file containing the point cloud.
    
    Returns:
        np.ndarray: Nx6 array where each row is [x, y, z, r, g, b], 
        if the point cloud doesn't have color, white color(255,255,255) is added.
    """
    points = np.load(npy_path)

    if points.shape[1] >= 6:
        return points[:, :6]  # Assume the first 6 columns are [x, y, z, r, g, b]
    else:
        # Generate white RGB color for each point
        num_points = points.shape[0]
        white_rgb = np.ones((num_points, 3)) * 255  # RGB in 0–255 range
        return np.hstack((points[:, :3], white_rgb))
