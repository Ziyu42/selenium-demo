# UI 自動化測試專案

這是一個UI自動化測試專案，是基於Selenium WebDriver、Python和Pytest框架所建構而成。本專案只在為The Internet Herokuapp網站進行Login/Logout測試。

## 專案功能及特色
- **頁面物件模型(POM)**：將Web Elements、Method封裝在獨立的類別中，提高測試的可維護性及可重用性。
- **Pytest框架**：使用Pytest撰寫和管理測試用例，提供豐富的斷言和測試報告功能。
- **顯示等待**：透過WebDriverWait和Expected Conditions確保元素在操作前就定位，不會因為網頁還沒跑完出現timeout fail就結束測試，提升測試的穩定性。
- **多重定位**：運用By.ID, By.CSS_SELECTOR, By.XPATH等定位器，精準找到網頁元素。
-**測試場景涵蓋**：
  - 使用者登入/登出測試
  - 錯誤訊息驗證


## How to run

```bash
pip install -r requirements.txt
pytest tests/
```
