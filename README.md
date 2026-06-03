# Face Recognition Attendance

Attendance system using face recognition from a webcam. This repository captures faces from the webcam, matches them against known photos in the `photos/` folder, and writes attendance rows to a dated CSV (e.g. `2026-06-03.csv`).

**Prerequisites**

- Python 3.8+ (3.10 recommended)
- A working webcam
- A terminal / PowerShell or command prompt

**Quickstart**

1. Clone the repository:

```bash
git clone https://github.com/SagarJadhav30/face_Recognition.git
cd "face recogination"
```

2. (Recommended) Create and activate a virtual environment:

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows (cmd):

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Prepare known faces: place JPEG/PNG images inside the `photos/` directory. The default `program.py` looks for these names: `jobs`, `tata`, `sadmona`, `tesla` (extensions: `.jpg` / `.jpeg`).

5. Run the program:

```bash
python program.py
```

Press `q` in the display window to quit. Attendance entries are appended to a CSV file named with the current date (e.g. `2026-06-03.csv`).

**Files**

- [program.py](program.py) — main script that opens the webcam and logs attendance.
- [requirements.txt](requirements.txt) — Python dependencies.
- `photos/` — directory for known-person image files (create if missing).

**Notes & Troubleshooting**

- The project uses `face_recognition`, `dlib`, `opencv-python`, and `numpy`. Installing `dlib` on Windows can be tricky. If you encounter errors installing `dlib` via `pip`, consider using Anaconda/Miniconda and installing `dlib` from conda-forge:

```bash
conda create -n faceenv python=3.10
conda activate faceenv
conda install -c conda-forge dlib
pip install -r requirements.txt
```

- If the webcam cannot be opened, check other applications are not using it and that your camera drivers are installed.
- If you get `No face found` errors for an image, use a clear frontal face photo with good lighting.

**Customization**

- Edit the `known_people` list inside [program.py](program.py) to add/remove people or change image filenames.
- Adjust recognition sensitivity by modifying `face_recognition` calls in the script.

**License**

See `LICENSE.txt` for license terms.

