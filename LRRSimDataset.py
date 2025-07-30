import numpy as np
import os
from torch.utils.data import Dataset
import pickle
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import cv2


def convert_pts_local_to_global(pts, ego_post_local2global):
    """
    Convert radar points in local coordinate system into global (world) coordinate system
    Args:
        pts: radar pts [x,y,z] (N, 3)
        ego_post_local2global: transformation matrix local to global (4,4)

    Returns:

    """
    sensor_loc = np.array([2.63, 0, 0.62])  # sensor location on ego
    pts_global = (pts + sensor_loc) @ ego_post_local2global[:3, :3].T + ego_post_local2global[:3, 3]

    return pts_global


def show_radar_scene(data_dict, show_vis_only=True):
    """
    Show radar points with target bboxes in top-view
    Args:
        data_dict: from LRRSimDataset
    """

    radar_pts = data_dict['radar_pts'][:, :3]
    targets_bboxes = data_dict['targets_bboxes']
    target_is_visible = data_dict['target_is_visible']

    fig, ax = plt.subplots(1, 1)
    ax.scatter(radar_pts[:, 0], radar_pts[:, 1], )
    targets_cuboids_local = targets_bboxes
    for t_id in range(targets_cuboids_local.shape[0]):
        target_cuboid = targets_cuboids_local[t_id]
        is_vis = target_is_visible[t_id]
        if show_vis_only and not is_vis:
            continue
        rectangle_target1 = Rectangle(
            (target_cuboid[0] - target_cuboid[3] / 2, target_cuboid[1] - target_cuboid[4] / 2),
            target_cuboid[3], target_cuboid[4], angle=target_cuboid[6],
            rotation_point='center', linewidth=1, edgecolor='m' if is_vis else 'k', facecolor='none')
        ax.add_patch(rectangle_target1)

    ax.grid(True)
    ax.set_xlabel('x[m]')
    ax.set_ylabel('y[m]')
    ax.set_aspect('equal')
    plt.show()




class LRRSimDataset(Dataset):
    def __init__(self, data_path, split='train', load_imgs=False):
        self.data_path = data_path
        self.split = split
        self.load_imgs = load_imgs

        # Get file names
        self.radar_file_list = os.listdir(os.path.join(self.data_path, 'radar_data', self.split))
        if self.load_imgs:
            self.img_file_list = os.listdir(os.path.join(self.data_path, 'image_data', self.split))

    def __len__(self):
        return len(self.radar_file_list)

    def __getitem__(self, idx):

        file_path = os.path.join(self.data_path, 'radar_data', self.split, self.radar_file_list[idx])
        with open(file_path, 'rb') as f:
            data_dict = pickle.load(f)

        if self.load_imgs:
            img = cv2.imread(os.path.join(self.data_path, 'image_data', self.split, self.img_file_list[idx]))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            data_dict['img'] = img

        return data_dict


if __name__ == '__main__':

    DATA_PATH = ""
    SPLIT = 'train'

    dset = LRRSimDataset(data_path=DATA_PATH, split=SPLIT)

    idx = 100
    data_dict = dset[idx]

    show_radar_scene(data_dict)






    quit()

