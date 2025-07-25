# Matplotlib Colormap Viewer

這是一個簡單的 Python 應用程式，用於視覺化 Matplotlib 的色彩映射（colormaps）。您可以使用自己的 2D 陣列數據或內建的範例數據來查看不同 colormap 的效果。

## 功能特點

- 支援載入 `.npy` 和 `.csv` 格式的 2D 陣列數據
- 提供內建的範例數據（sin(x² + y²)）
- 同時展示多種 colormap 效果
- 包含常用的 colormap：
  - viridis, plasma, inferno, magma, cividis
  - Greys, Blues, RdBu, seismic, coolwarm
  - tab10, nipy_spectral

## 使用需求

- Python 3.x
- NumPy
- Matplotlib
- tkinter (通常包含在 Python 標準庫中)

## 安裝依賴

```bash
pip install numpy matplotlib
```

## 使用方法

1. 運行程式：
   ```bash
   python colormap_viewer.py
   ```

2. 選擇數據來源：
   - 輸入 `1`: 從文件載入 2D 陣列數據（.npy 或 .csv）
   - 輸入 `2`: 使用內建的範例數據

3. 如果選擇從文件載入：
   - 會打開檔案選擇對話框
   - 選擇 `.npy` 或 `.csv` 格式的檔案

4. 程式會顯示一個視窗，展示選定數據在不同 colormap 下的視覺化效果

## 數據格式要求

- 數據必須是 2D 陣列
- `.csv` 文件應該是以逗號分隔的數值矩陣
- `.npy` 文件應該包含 2D NumPy 陣列

## 程式結構

- `load_data()`: 載入 .npy 或 .csv 檔案
- `generate_sample_data()`: 生成範例數據
- `plot_colormaps()`: 顯示不同 colormap 的視覺化效果
- `open_file_dialog()`: 開啟檔案選擇對話框
- `show_colormap_gallery()`: 主要的展示功能

## 範例輸出
'''python
import colormap_viewer

# 使用內建範例資料
colormap_viewer.show_colormap_gallery(from_file=False)

# 使用自定義 2D array
Z = colormap_viewer.generate_sample_data(size=200)
colormap_viewer.show_colormap_gallery(from_file=False, data=Z)

# 使用檔案總管選擇資料檔案（.npy or .csv）
colormap_viewer.show_colormap_gallery(from_file=True)
'''
程式會創建一個視窗，展示所選數據在不同 colormap 下的效果，每個 colormap 都包含一個顏色條，方便比較和選擇最適合的視覺化方案。
