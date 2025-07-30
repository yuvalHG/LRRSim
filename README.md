# LRR-Sim: Long-Range Radar Simulation Dataset

**LRR-Sim** is the first publicly available long-range radar dataset with annotated 3D point clouds extending **up to 300 meters**,
filling a critical gap in radar research for highway and high-speed scenarios.
It includes ~18K training and ~3K testing frames across 50 simulated highway scenes, with a total of ~160K annotated vehicles - including ~28K vehicles beyond 175m, where conventional sensors struggle.
Scenes were created using the [CARLA simulator](https://carla.org/) for realistic world modeling and highway maps, with a high-fidelity radar simulation applied on top to generate 77GHz MIMO radar point clouds. All objects within ±55° azimuth and ±20° elevation are annotated with accurate 3D bounding boxes.

---

## 🧠 Key Features

- 📡 **Realistic radar simulated dataset** with range-Doppler-azimuth-elevation spectra.
- 🚗 **Highway scenes** with diverse vehicles (car, van, truck).
- 📏 **Range up to 300m** - the longest detection range among public radar datasets.
- 🎯 **Precise 3D annotations** for all vehicles within the radar field-of-view.
- ⚙️ **Radar parameters** based on high-end automotive sensors.
- 📦 Comes with a **Python Dataset class** for easy integration into ML pipelines.

---

## 🔗 Download

You can download the dataset using the links below:

- 📥 [Download Radar Data](https://drive.google.com/file/d/1GfleL16_BphZgkUhrAINRygR93EriuBH/view?usp=drive_link) (105 MB)
- 📥 [Download Image Data](https://drive.google.com/file/d/1IN3FxWx6Mt109fMKnwGZsGtCJ4gTwRiQ/view?usp=sharing) (13.5 GB)


---

## 📁 Dataset Structure

Each scenario contains radar data collected at **20 FPS** for **30 seconds**, saved as individual frames:

```commandline
lrrsim/
├── image_data/
│ ├── train/
│ │ ├── 00000.jpg
│ │ ├── 00001.jpg
│ │ └── ...
│ ├── test/
│ │ ├── 00000.jpg
│ │ ├── 00000.jpg
│ │ └── ...
├── radar_data/
│ ├── train/
│ │ ├── 00000.pkl
│ │ ├── 00001.pkl
│ │ └── ...
│ ├── test/
│ │ ├── 00000.pkl
│ │ ├── 00001.pkl
│ │ └── ...
```
Each radar file `xxxxx.pkl` file contains a dictionary:

- `radar_pts` (N × 8): Radar point cloud [x, y, z, doppler, intensity, frame_idx]
- `ego_vel` (3,): The ego velocity
- `T_ego_local2global` (4,4): convert from ego local coordinates to global coordinates
- `timestamp` : frame timestamp in sec
- `targets_bboxes` (K,7): GT bboxes [cx, cy, cz, ex, ey, ez, yaw(deg)]
- `targets_vel` (K,3): Target vehicles GT velocities
- `target_ids` (K,): Target vehicles unique ID
- `target_is_visible` (K,): Flag indicating if target vehicle is visible to sensor
- `img`: front camera image (optional)

---

## 📐 Radar Sensor Configuration

| Parameter                | Value           |
|--------------------------|-----------------|
| **Max Range**            | 300m            |
| **Range Resolution**     | 0.15m           |
| **Azimuth FOV**          | ±55°            |
| **Azimuth Resolution**   | 1.2°            |
| **Elevation FOV**        | ±20°            |
| **Elevation Resolution** | 2°              |
| **Doppler Range**        | \[−80, +30] m/s |
| **Doppler Resolution**   | 0.13 m/s        |



---

## 🔧 Requirements

  - torch
  - numpy
  - opencv-python
  - matplotlib >= 3.6



---

## 🧰 Usage Example

```commandline
from lrrsim import LRRSimDataset

DATA_PATH = "path/to/LRRSimDatase"
SPLIT = 'train' # 'test'

dset = LRRSimDataset(data_path=DATA_PATH, split=SPLIT, load_imgs=False)

idx = 0
data_dict = dset[idx]

show_radar_scene(data_dict)

```

---
## 📊 Dataset Statistics
🛣 50 highway driving scenarios (42 train / 8 test)

⏱ Approximately 30s each at 20 FPS (18172 frames for train, 3363 frames for test)

🚘 ~160K vehicle instances, ~28K beyond 175m

📦 Vehicle types include cars, trucks, and vans, with an average of 7.3 vehicles per frame

---


## 📜 Citation
If you use LRR-Sim in your research, please cite:


```bibtex
@inproceedings{doppdrive2025,
  title={DoppDrive: Doppler-Driven Temporal Aggregation for Improved Radar Object Detection},
  author={Yuval Haitman and Oded Bialer},
  booktitle={ICCV},
  year={2025}
}
```
