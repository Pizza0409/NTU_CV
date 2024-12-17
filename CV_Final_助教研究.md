# CV Final 助教研究

## 備註
中文部分皆為 ChatGPT 產生

### 1. **Innovative Velocity Estimation in Ego Vehicles**

**研究方法：**

- 結合光流技術和深度學習構建兩階段模型。
- 使用 Comma2K19 和 KITTI 數據集進行訓練和測試。

**研究步驟：**

1. 數據預處理：調整視頻尺寸、應用框大小和步長篩選視頻幀。
2. 階段一：分類模型（Conv1D，Dropout 等）進行速度區間分類。
3. 階段二：回歸模型估算每對幀的精確速度值。
4. 使用高斯濾波器平滑速度曲線以減少抖動。
5. 測試模型在 KITTI 數據集上的泛化性能。

**研究結果：**

- 在 Comma2K19 測試集上，平均 RMSE 為 0.994 m/s，顯著優於傳統方法。
- 高斯濾波進一步將 RMSE 減少 34.7%。

![image.png](image.png)

![image.png](image%201.png)

---

### 2. **3D BGA Reconstruction**

**研究方法：**

- 利用 NeRF（Neural Radiance Fields）進行場景建模。
- 噪聲處理方法包括高斯模糊和同態濾波。
- 使用多層感知器（MLP）進行場景密度預測。

**研究步驟：**

1. 應用高斯模糊與同態濾波進行噪聲清理。
2. 將 X 光圖像用於 NeRF 模型的訓練。
3. 生成 3D 圖像並進行體素密度計算。
4. 移除異常點並對數據進行標準化。

**研究結果：**

- 成功獲得內部結構的 3D 模型，峰值信噪比（PSNR）為 26.56。

![image.png](image%202.png)

![image.png](image%203.png)

---

### 3. **Calculating Acetabular Anteversion Angle Using Neural Networks**

**研究方法：**

- 利用神經網路（TensorFlow）直接從 X 光圖像預測髖臼前傾角度。
- 圖像數據增強和訓練分組策略。

**研究步驟：**

1. 生成虛擬 X 光圖像（12,417 張），並分為訓練組（11,366 張）和驗證組（1,051 張）。
2. 安裝 TensorFlow、OpenCV 等影像處理套件。
3. 開發和訓練 CNN 模型。
4. 調整超參數（層數、學習率、batch size）。
5. 使用最佳模型評估驗證數據，計算角度誤差。

**研究結果：**

- 模型能準確預測髖臼的前傾和傾斜角度，並提供可靠數據以支持手術規劃。

![image.png](image%204.png)

---

### 4. **LiRecognition: Real-time Pet Behavior Recognition on Embedded System**

**研究方法**

- **Stable Diffusion XL-Lightning (SDXL-Lightning)** 與 **LoRA** (Low-Rank Adaptation) 用於合成高品質數據。
- **YOLOv7-tiny** 模型結構進行行為辨識。
- **Torch Pruning** 技術優化模型大小與速度，適配 Realtek AMB82-mini 平台。

**研究步驟**

1. 利用 SDXL-Lightning 與 LoRA 生成合成圖像數據集，補充訓練數據不足的問題。
2. 將數據集輸入 YOLOv7-tiny 模型進行訓練。
3. 使用 Torch Pruning 減少模型參數量，提升推理速度。
4. 在 Realtek AMB82-mini 平台上進行部署與測試。

**研究結果**

- 提高了貓行為辨識的準確性與效率（例如 mAP 從原數據的 0.798 提升到改良數據的 0.895）。
- 通過剪枝後，模型參數和運算量大幅減少，幀率 (FPS) 幾乎翻倍。

![1DF5CFB0-1A03-4F99-8640-A3CAE540050F.JPG](1DF5CFB0-1A03-4F99-8640-A3CAE540050F.jpg)

---

### 5. **Segmentation of Tooth Crack on Dental CT-Scan Images**

**研究方法**

- 採用 **Convolutional-Transformer Network**，結合 **Boundary Awareness Module (BAM)** 和 **Dilated Residual Block (DRB)**，提升牙齒裂縫邊界的分割準確度。
- **MobileViT Block** 用於減少參數，提升模型效率。

**研究步驟**

1. 收集 850 張牙科 CT 圖像，標記裂縫位置以生成 Ground Truth 二進制掩模。
2. 使用 Tao 等人提出的 Convolutional-Transformer Network，針對標記數據進行模型訓練。
3. 調整分割閾值以去除噪聲並改進分割精度。
4. 將每層的預測結果組合成 3D 視覺化呈現牙齒裂縫位置。

**研究結果**

- 提供牙齒裂縫的 3D 視覺化圖像，顯著提升診斷的準確性與效率。
- 模型能有效輔助牙科醫生檢測裂縫，並有潛力整合進臨床工作流程中。

![image.png](image%205.png)

---

### 6. **3D Object Detection and Collision Prediction Using LIDAR**

**研究方法：**

- 使用 Ouster LIDAR 獲取點雲數據。
- 採用 CenterPoint 模型進行 3D 物體檢測和追蹤。
- 使用 SimpleTrack 進行多目標追蹤。

**研究步驟：**

1. 利用 LIDAR 獲取數據，生成 3D 點雲。
2. 使用 CenterPoint 檢測物體並繪製邊界框。
3. 利用 SimpleTrack 計算物體速度並預測碰撞機率。
4. 二次處理（Refinement）透過 MLP 進行檢測框的細化。

**研究結果：**

- 能夠有效預測碰撞機率，並標註可能發生碰撞的區域。

![image.png](image%206.png)

---

---

### 7. **Pet Camera Video Streaming on Cloud**

**研究方法**

- 使用 **ChatGPT** 生成動作清單，**Stable Diffusion** 生成可愛寵物行為的數據集圖像。
- 使用 **YOLOv7** 訓練目標檢測模型。
- 建立基於 **AWS** 的雲端伺服器與 API 以接收來自寵物攝像機的檔案。

**研究步驟**

1. 透過 ChatGPT 輸出可愛行為列表，並用 Stable Diffusion 製作合成影像。
2. 整合實際照片與合成影像作為 YOLOv7 模型的訓練數據集。
3. 部署 AWS 伺服器，搭建 API 接收與處理來自邊緣裝置（如 NVIDIA Jetson Nano 和 Realtek AMB82）的檔案。
4. 將寵物攝像機拍攝的短片上傳至雲端以進行檢測與分類。

**研究結果**

- 成功在邊緣裝置上檢測到貓的可愛行為，雲端系統功能正在開發中。

![image.png](image%207.png)

---