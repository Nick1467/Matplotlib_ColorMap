import numpy as np
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
import time

# ✅ 預設展示的 colormaps
DEFAULT_COLORMAPS = [
    "viridis", "plasma", "inferno", "magma", "cividis",
    "Greys", "Blues", "RdBu", "seismic", "coolwarm",
    "nipy_spectral", "twilight", "ocean", "jet", "inferno", "magma",
    "cividis", "viridis_r", "RdBu_r", "inferno_r", "Blues_r",
    "viridis", "plasma", "seismic", "coolwarm", "twilight", "ocean", "jet",
    "inferno", "magma", "cividis", "viridis_r",
]

def load_data(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".npy":
        return np.load(filepath)
    elif ext == ".csv":
        return np.loadtxt(filepath, delimiter=",")
    else:
        raise ValueError("Unsupported file format. Please use .npy or .csv")

def generate_sample_data(size=150):
    x = np.linspace(-3, 3, size)
    y = np.linspace(-3, 3, size)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X**2 + Y**2)
    return Z

def plot_colormaps(data, cmap_list=DEFAULT_COLORMAPS):
    n = len(cmap_list)
    cols = 4
    rows = int(np.ceil(n / cols))

    fig, axes = plt.subplots(rows, cols, figsize=(4.5 * cols, 4 * rows))
    axes = axes.flatten()

    for i, cmap in enumerate(cmap_list):
        ax = axes[i]
        im = ax.imshow(data, cmap=cmap)
        ax.set_title(cmap, fontsize=28, fontweight='bold')
        ax.axis("off")
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

    for j in range(i + 1, len(axes)):
        axes[j].axis("off")

    plt.tight_layout()
    plt.show()

def open_file_dialog():
    root = tk.Tk()
    root.attributes('-alpha', 0)  # 透明化
    root.attributes('-topmost', True)  # 永遠置頂
    root.lift()  # 強制置頂
    file_path = filedialog.askopenfilename(
        parent=root,
        title="選擇 2D 陣列資料檔案",
        filetypes=[("NumPy 檔案", "*.npy"), ("CSV 檔案", "*.csv")]
    )
    root.destroy()
    return file_path

def show_colormap_gallery(from_file=True, file_path=None, data=None, colormaps=None):
    if from_file:
        if not file_path:
            print("📁 開啟檔案總管以選擇 .npy 或 .csv")
            time.sleep(0.5)
            file_path = open_file_dialog()
        if not file_path:
            print("❌ 未選取任何檔案。")
            return
        data = load_data(file_path)
    elif data is None:
        print("✅ 使用內建範例資料（sin(x² + y²))）")
        data = generate_sample_data()

    if data.ndim != 2:
        raise ValueError("資料必須是 2D array")

    cmap_list = colormaps if colormaps else DEFAULT_COLORMAPS
    print(f"📐 資料大小：{data.shape}")
    plot_colormaps(data, cmap_list)

# ▶️ CLI 主執行邏輯（保留互動式選單）
if __name__ == "__main__":
    print("選擇資料來源：")
    print("1. 匯入 2D 陣列資料（開啟檔案總管）")
    print("2. 使用內建範例資料（sin(x² + y²))）")
    choice = input("> 輸入 1 或 2： ").strip()

    if choice == "1":
        show_colormap_gallery(from_file=True)
    else:
        show_colormap_gallery(from_file=False)
