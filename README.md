# 💩 DogPoopAI — GitHub Pages 部署指南

即時狗便便偵測，使用 YOLOv8n + ONNX Runtime Web，完全在瀏覽器本地執行。

## 檔案結構

```
github_pages/
├── index.html                  ← 主頁面（所有程式碼）
├── DogPoopAI_v6_320.onnx       ← 模型檔案（需手動放入）
└── README.md
```

## 部署步驟

### 1. 準備模型檔案

將 `DogPoopAI_v6_320.onnx`（11.6 MB）複製到此資料夾，與 `index.html` 同一層。

### 2. 建立 GitHub Repository

```bash
git init
git add .
git commit -m "Initial deploy"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/DogPoopAI.git
git push -u origin main
```

### 3. 啟用 GitHub Pages

1. 進入 Repository → **Settings** → **Pages**
2. Source 選擇 **Deploy from a branch**
3. Branch 選 `main`，資料夾選 `/ (root)`
4. 點 **Save**，等待約 1–2 分鐘

網站網址：`https://YOUR_USERNAME.github.io/DogPoopAI/`

> ⚠️ **注意**：ONNX 模型檔案 11.6 MB，超過 GitHub 單檔建議上限（50 MB 以內仍可推送，但建議使用 Git LFS）。

### 使用 Git LFS（建議）

```bash
git lfs install
git lfs track "*.onnx"
git add .gitattributes
git add DogPoopAI_v6_320.onnx
git commit -m "Add model via LFS"
git push
```

## 使用方式

1. 用手機 Chrome（Android）或 Safari（iOS）開啟網址
2. 點「開始偵測」，允許相機權限
3. 將鏡頭對準地面，AI 自動框出便便位置

## 技術規格

| 項目 | 內容 |
|------|------|
| 模型 | YOLOv8n，1 class（poop） |
| 輸入 | 320×320 RGB，CHW，float32 |
| 輸出 | (1, 5, 2100)：x, y, w, h, conf |
| 後端 | WebGPU 優先，自動 fallback WASM |
| 信心閾值 | 0.30 |
| NMS IoU | 0.45 |

## 瀏覽器支援

| 瀏覽器 | WebGPU | WASM |
|--------|--------|------|
| Chrome 113+ (Android/Desktop) | ✅ | ✅ |
| Safari 18+ (iOS/macOS) | ✅ | ✅ |
| Firefox | ❌ | ✅ |
| Chrome iOS | ❌ | ✅ |

## 本地測試

需要 HTTPS 或 localhost（getUserMedia 需要安全環境）：

```bash
# Python
python -m http.server 8080

# Node.js
npx serve .
```

開啟 `http://localhost:8080`
