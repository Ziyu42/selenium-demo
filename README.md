# UI 自動化測試專案

這是一個UI自動化測試專案，是基於Selenium WebDriver、Python和Pytest框架所建構而成。本專案旨在為The Internet Herokuapp網站進行Login/Logout測試。

## 專案功能及特色
- **頁面物件模型(POM)**：將Web Elements、Method封裝在獨立的類別中，提高測試的可維護性及可重用性。
- **Pytest框架**：使用Pytest撰寫和管理測試用例，提供豐富的斷言和測試報告功能。
- **顯示等待**：透過WebDriverWait和Expected Conditions確保元素在操作前就定位，不會因為網頁還沒跑完出現timeout fail就結束測試，提升測試的穩定性。
- **多重定位**：運用By.ID, By.CSS_SELECTOR, By.XPATH等定位器，精準找到網頁元素。
- **測試場景涵蓋**：
  - 使用者登入/登出測試
  - 錯誤訊息驗證

## 環境架設
- Python 3.8或更高版本
- pip(Python 套件管理器)
- Google Chrome瀏覽器
- ChromeDriver(與您的Chrome瀏覽器版本兼容。建議使用 webdriver-manager 套件來自動管理 ChromeDriver)

## 安裝步驟：
1.複製專案
```bash
git clone https://github.com/Ziyu42/selenium-demo.git
cd selenium-demo

2.安裝
```bash
pip install -r requirements.txt

###執行方式
這個專案使用 `pytest` 進行測試。要運行測試，請確保你已經安裝 pytest：

pip install pytest
pytest 
```