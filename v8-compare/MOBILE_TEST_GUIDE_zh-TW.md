# DogPoopAI v7 vs v8 epoch8 手機比較測試

日期：2026-06-11

## 目的

比較：

- v7 stable，Candidate threshold 0.30
- v8 Exp2 epoch8 candidate，Candidate threshold 0.35

測試重點：

- 真便便能否產生 Candidate
- Virtual Camera 2 能否 Confirmed
- 空場景或干擾物是否造成錯誤 Candidate / False Confirm
- 2x / 3x / 5x Search Zoom 的差異
- 主推理與 VCam second pass 延遲

## 測試前

1. 使用相同手機、相同相機方向與相同光線。
2. Power Save 保持 ON。
3. 每次比較都使用相同距離和相同拍攝角度。
4. 確認頁面 Build 顯示 `v8-compare-r1`。
5. 選擇模型後，確認頂部 Active Model 和 Threshold：
   - v7 stable：30%
   - v8 epoch8 candidate：35%

## 建議測試矩陣

每個模型測：

- Search Zoom：2x、3x、5x
- 距離：30、50、100、150、200 cm
- Ground Truth：
  - Poop present
  - No poop

最低完整測試量：

```text
2 models × 3 zooms × 5 distances = 30 positive samples
```

Negative 場景建議至少加入：

- 草地
- 枯葉
- 石頭
- 泥土
- 陰影
- 深色小物件

## 每一筆怎樣測

1. 選擇 Model。
2. 確認 Threshold 顯示正確。
3. 選擇 Search Zoom。
4. 將手機固定在指定距離。
5. 等待 3 至 5 秒，讓 Top Raw、Candidate 和 VCam 穩定。
6. 在 Mobile Comparison Test Records 輸入：
   - Distance
   - Ground Truth
   - Scene ID
   - Trial
   - Notes
7. 按 `Record Sample`。
8. 改下一個 zoom 或 model，重複相同步驟。

## 自動記錄內容

每次按 Record Sample 會記錄：

- Model / model label
- Candidate threshold
- Search Zoom
- Distance
- Ground Truth
- Top Raw Conf
- Top Raw Area
- Main smoothed confidence
- Candidate frames
- Main result / robot state
- VCam result
- VCam second raw / smoothed confidence
- Confirmed frames
- Main inference latency
- VCam inference latency
- FPS
- Power Save 狀態
- Scene ID / Trial / Notes

## Outcome 意思

| Outcome | 意思 |
|---|---|
| TP_CONFIRMED | 有真便便，而且 VCam 成功確認 |
| CANDIDATE_ONLY | 有真便便，只到 Candidate / Target Locked，未確認 |
| MISS | 有真便便，但沒有 Candidate |
| FALSE_CONFIRM | 沒有便便，但 VCam 錯誤確認 |
| FALSE_CANDIDATE | 沒有便便，但出現 Candidate |
| CORRECT_CLEAR | 沒有便便，而且沒有 Candidate / Confirm |

## 匯出

完成一輪測試後：

1. 按 `Download CSV`。
2. iPhone 會下載或開啟分享選單。
3. 將 CSV 保存到 Files / iCloud Drive。
4. 不要先按 Clear Records。
5. 確認 CSV 已保存後，才開始下一個測試批次。

記錄會保存在瀏覽器 localStorage。清除 Safari 網站資料可能會刪除記錄，所以每輪完成後應立即下載 CSV。

## 公平比較原則

- 不要用不同光線比較兩個模型。
- 不要只測模型成功的角度。
- 同一 Scene ID 應使用相同距離、zoom 和手機位置。
- 模型切換後等待 3 至 5 秒再記錄。
- 5x 是 Experimental，必須另外記錄視野太窄造成的漏檢。
- False Candidate 和 False Confirm 必須分開計算。

## 通過條件建議

v8 epoch8 適合升級正式版，需要同時滿足：

- 真便便 Confirmed rate 明顯高於 v7。
- False Confirm 不高於可接受範圍。
- 2x / 3x 下框位置沒有偏移。
- VCam latency 不令手機明顯卡死。
- Power Save ON 時仍可穩定完成確認。

正式 `C:\DogPoopAI\index.html` 暫時不要修改。先完成手機比較並分析 CSV。
