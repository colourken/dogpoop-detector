# Label Studio 環境設定指南
## DogPoopAI 專用 — 每次使用前閱讀

---

## 環境需求
- Python 3.10
- label-studio（已安裝）
- 工作目錄：`C:\DogPoopAI\`

---

## 每次使用步驟

### Step 1：啟動 CORS Image Server
開一個 **CMD 視窗**，跑：
```cmd
cd C:\DogPoopAI\scripts
python cors_server.py
```
看到 `✅ CORS Server running at http://localhost:8081` 保持開著不要關。

### Step 2：啟動 Label Studio
開**另一個 CMD 視窗**，跑：
```cmd
label-studio start
```
瀏覽器自動開啟 `http://localhost:8080`

### Step 3：建立新 Project
1. **Create Project** → 輸入名稱
2. **Labeling Setup** → Object Detection with Bounding Boxes
3. 加入 Label：`poop`
4. 儲存

### Step 4：生成 JSON（如有 YOLO labels）
```cmd
cd C:\DogPoopAI\scripts
python yolo_to_labelstudio.py
```
修改腳本內的路徑：
- `IMAGES_DIR` → 照片資料夾
- `LABELS_DIR` → YOLO .txt 資料夾
- `OUTPUT_JSON` → 輸出 JSON 位置

### Step 5：Import 到 Label Studio
- 進入 Project → **Import**
- 拖入 `output_labelstudio.json`
- 圖片應該正常顯示（透過 http://localhost:8081）

### Step 6：標注完成後 Export
- **Export** → 選 **YOLO with Images**
- 解壓到對應資料夾

---

## 常見問題

### 圖片顯示不出來
原因：cors_server.py 沒有跑，或跑在錯誤的資料夾。
解決：確認 Step 1 的 cors_server.py 有在跑，而且 JSON 裡的路徑是 `http://localhost:8081/xxx.jpg`

### label-studio 指令找不到
```cmd
pip install label-studio
```

### JSON 路徑格式
正確：`http://localhost:8081/IMG_20201112_112608192.jpg`
錯誤：`C:\DogPoopAI\...` 或 `/data/local-files/...`

---

## 腳本位置
| 腳本 | 用途 |
|------|------|
| `cors_server.py` | CORS 圖片伺服器（必須先跑）|
| `yolo_to_labelstudio.py` | YOLO labels 轉 Label Studio JSON |
| `merge_datasets.py` | 合併資料集 |
| `predict_preview.py` | YOLO 預測預覽 |
| `sort_by_confidence.py` | 按信心值分類 |

---

## 注意事項
- Label Studio 和 cors_server.py 必須同時開著
- 每次開新 session 都要重新跑兩個視窗
- Export 後記得用 merge_datasets.py 合併到訓練資料集
