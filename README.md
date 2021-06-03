# BDSE18-Stock
### 資策會 BIG DATA 巨量資料分析就業養成班
## BDSE18 第一組:股市大數據
`組員: 李子顥,陳姿伶,陳彥伶,劉文裕,李謀勳`


* **線上發表Yotube連結:**
    * TBD

* **視覺化網頁:**
    * Visit: https://kathleen-ling.github.io/BDSE18_visualization_final
    * Repository: https://github.com/Kathleen-Ling/BDSE18_visualization_final

* **專題介紹:**
    * 在台灣股市茫茫大海的數據中，找到與股價關聯性高的指標
    * 透過程式，縮短與減少重複性工作和人為判斷的時間
    * 探索金融與大數據、AI模型結合的成果經驗
    * 建立理性投資觀念的基礎
    
* **小組工作分配:**
    * 李子顥(組長): 專題架構規劃、資料搜集與處理、視覺化
    * 陳姿伶：資料搜集與處理、網路爬蟲、機器學習與深度學習、資料視覺畫
    * 陳彥伶：資料視覺化與網頁
    * 李謀勳：Hadoop平台架構、資料搜集與處理
    * 劉文裕：機器學習與深度學習、資料處理

* **專題成果:**
    * 資料取得
        * 來源：臺灣證券交易所、Goodinfo股市資訊網、FinMind
        * 時間範圍：2010年01月01日至2021年04月23日
        * 資料種類
            * 每日交易量
            * 法人買賣
            * 個股融資融卷
            * 當日沖銷交易標的及成交量值
            * 個股股利、 PER 、 PBR 資料表
            * 股東結構表
    * 資料清洗：使用Linux 合併表格，使用Pandas 轉換資料格式，如日期格式，並且剃除空值。
    * 數據分析：
        * Python的TALib和台股的日交易資料去建立技術面的特徵點
        * 隨機森林、XGBoost 參數最佳化
        * 隨機森林、XGBoost找出與股價關聯係數高的特徵
        * 利用找出來的特徵去跑LSTM模型預測股價
        * 透過四種不同特徵模型的比較
    * 資料視覺化：透過HTML、D3.js架設數據可視化的網站，提供方便快速的資料閱覽來源
        * 個股
            * 重要特徵
            * 股價預測
        * 台灣50		
            * 產業資訊
            * 模型預測、MSE

* **金融資料使用LSTM心得:**
    * 預測結果可以看出LSTM預測出來的價格趨勢，絕大多數時間跟股價是符合的
    * 不同產業類別、特性的股票，對於預測結果有蠻顯著的不同影響
    * 關鍵反思:
        1.	 **人為因素**：調整特徵、參數的部分是一個非常人為的舉動，訓練出來成果會受到這個人主觀的觀念以及操作的影響，凸顯出訓練模型的人對於金融市場的了解程度的重要性
        2.	**過擬和問題**：在我們訓練LSTM的過程中，發現特定的股票受到了疫情的影響有著意想不到的表現。我們現在訓練出來看起來很棒的結果，放到未來來看可能是一種過擬合的結果，有可能在面對未來意想不到情形下，模型表現得一塌糊塗

* **專題展望:**
    * 探索更多種類的股票指標，ex. 籌碼面的延伸、基本面、期貨、選擇權
    * 根據不同產業類別、不同個股，建立各自的參數挑選、股價預測模型
    * 嘗試不同的機器學習、深度學習模型。找出最佳模型和參數
    * 以預測模型建立股市交易策略
 
* **Repository 資料夾介紹:**
  * **Slides** 放有Hadoop架構報告
  * **Crawl** 爬蟲用資料夾
      * **Crawl_update_c.elegansdata** 放有主要爬蟲檔案，臺灣證券交易所、Goodinfo股市資訊網、FinMind
      * **Crawl_How** 根據上方檔案修改，加入爬蟲中斷點的設計，可以從尚未爬取的股票代碼繼續爬蟲
  * **Data_mining** 資料合併，將不同資料欄位csv整合成同一張csv
  * **ML&DL_WenYu** 機器學習與深度學習，有RF、XGBoost進行特徵篩選，LSTM股價預測
  * **Keras** Keras 資料夾中使用之前在做鐵達尼號資料集做過的模型，比較各個模型的結果，此資料就沒有 20 日分割，直接以收盤價做預測，輸出 png 檔供視覺化修改
      1. LSTM_KERAS.ipynb：使用前 20 日的資料預測下一天的資料。使用 KERAS 以及 LSTM 預測。輸出預測收盤價以及真實收盤價的 csv 檔以及初步輸出 png 檔供視覺化修改
      2. Feature_KERAS_LSTM.ipynb：使用前 20 日，Tablib 的資料預測下一天的資料。使用 KERAS 以及 LSTM 預測。輸出預測收盤價以及真實收盤價的 csv 檔以及初步輸出 png 檔供視覺化修改
  * **Multiple** 特徵比較
  * **Visual** 台股累積成交量、成交價量+圖片
  * **Pending** 原先專題想加入Google Trends部分的程式碼
  `Credit: 陳識安`
  
  ---

下面為資料表格說明：

| 類別                                   | 欄位名稱                             | 對照名稱                 | 說明                        |
|--------------------------------------|----------------------------------|----------------------|---------------------------|
| index                                | index                            | 索引                   | 共有 4078037 列，58欄（不含index） |
| 個股基本資料                               | stock_id                         | 股票代碼（primary_key)    |                           |
| 個股基本資料                               | stock_name                       | 公司名稱（primary_key)    |                           |
| 個股基本資料                               | ISIN_Code                        | 國際證券辨識號碼(ISIN Code)  |                           |
| 個股基本資料                               | Listing_date                     | 上市日                  | datetime64                |
| 個股基本資料                               | Listing_category                 | 市場別                  |                           |
| 個股基本資料                               | Industry_category                | 產業別                  |                           |
| 個股基本資料                               | CFICode                          | CFICode              |                           |
| Finmind_daily 日交易                    | date                             | 交易日期                 | datetime64                |
| Finmind_daily 日交易                    | Volume                           | 成交量                  |                           |
| Finmind_daily 日交易                    | Volume_Cash                      | 成交金額                 |                           |
| Finmind_daily 日交易                    | Open                             | 開盤價                  |                           |
| Finmind_daily 日交易                    | High                             | 最高價                  |                           |
| Finmind_daily 日交易                    | Low                              | 最低價                  |                           |
| Finmind_daily 日交易                    | Close                            | 收盤價                  |                           |
| Finmind_daily 日交易                    | Change                           | 漲跌幅（會有正負號）           |                           |
| Finmind_daily 日交易                    | Order                            | 交易筆數                 |                           |
| TaiwanStockPER 個股股利、PER、PBR資料表       | dividend_yield                   | 殖利率                  |                           |
| TaiwanStockPER 個股股利、PER、PBR資料表       | PER                              | 本益比                  |                           |
| TaiwanStockPER 個股股利、PER、PBR資料表       | PBR                              | 股價淨值比                |                           |
| InsitutionalInvestorsBuySell 法人買賣    | Dealer_buy                       | 自營商_買進               |                           |
| InsitutionalInvestorsBuySell 法人買賣    | Dealer_Hedging_buy               | 自營商避險_買進             |                           |
| InsitutionalInvestorsBuySell 法人買賣    | Dealer_self_buy                  | 自營商_買進               | 歸類跟 Dealer_buy 相同         |
| InsitutionalInvestorsBuySell 法人買賣    | Foreign_Dealer_Self_buy          | 外資自營商_買進             |                           |
| InsitutionalInvestorsBuySell 法人買賣    | Foreign_Investor_buy             | 外資_買進                |                           |
| InsitutionalInvestorsBuySell 法人買賣    | Investment_Trust_buy             | 投信_買進                |                           |
| InsitutionalInvestorsBuySell 法人買賣    | Dealer_sell                      | 自營商_買進               |                           |
| InsitutionalInvestorsBuySell 法人買賣    | Dealer_Hedging_sell              | 自營商避險_賣出             |                           |
| InsitutionalInvestorsBuySell 法人買賣    | Dealer_self_sell                 | 自營商_買進               | 歸類跟 Dealer_buy 相同         |
| InsitutionalInvestorsBuySell 法人買賣    | Foreign_Dealer_Self_sell         | 外資自營商_賣出             |                           |
| InsitutionalInvestorsBuySell 法人買賣    | Foreign_Investor_sell            | 外資_賣出                |                           |
| InsitutionalInvestorsBuySell 法人買賣    | Investment_Trust_sell            | 投信_賣出                |                           |
| TaiwanStockShareHolding 股東結構表（外資持股表） | ForeignInvestmentRemainingShares | 外資尚可投資股數             |                           |
| TaiwanStockShareHolding 股東結構表（外資持股表） | ForeignInvestmentShares          | 外資持有股數               |                           |
| TaiwanStockShareHolding 股東結構表（外資持股表） | ForeignInvestmentRemainRatio     | 外資尚可投資比例             |                           |
| TaiwanStockShareHolding 股東結構表（外資持股表） | ForeignInvestmentSharesRatio     | 外資持股比例               |                           |
| TaiwanStockShareHolding 股東結構表（外資持股表） | ForeignInvestmentUpperLimitRatio | 外資投資上限               |                           |
| TaiwanStockShareHolding 股東結構表（外資持股表） | ChineseInvestmentUpperLimitRatio | 陸資投資上限               |                           |
| TaiwanStockShareHolding 股東結構表（外資持股表） | NumberOfSharesIssued             | 發行股數                 |                           |
| TaiwanStockShareHolding 股東結構表（外資持股表） | RecentlyDeclareDate              | 最近一次異動申報日期           | datetime64                |
| TaiwanStockShareHolding 股東結構表（外資持股表） | StockShareholding_note           | StockShareholding_備註 |                           |
| PurchaseShortSale 個股融資融卷             | MarginPurchaseBuy                | 融資買進                 |                           |
| PurchaseShortSale 個股融資融卷             | MarginPurchaseCashRepayment      | 融資現金償還               |                           |
| PurchaseShortSale 個股融資融卷             | MarginPurchaseLimit              | 融資限額                 |                           |
| PurchaseShortSale 個股融資融卷             | MarginPurchaseSell               | 融資賣出                 |                           |
| PurchaseShortSale 個股融資融卷             | MarginPurchaseTodayBalance       | 融資今日餘額               |                           |
| PurchaseShortSale 個股融資融卷             | MarginPurchaseYesterdayBalance   | 融資昨日餘額               |                           |
| PurchaseShortSale 個股融資融卷             | OffsetLoanAndShort               | 資券互抵                 |                           |
| PurchaseShortSale 個股融資融卷             | ShortSaleBuy                     | 融券買進                 |                           |
| PurchaseShortSale 個股融資融卷             | ShortSaleCashRepayment           | 融券償還                 |                           |
| PurchaseShortSale 個股融資融卷             | ShortSaleLimit                   | 融券限額                 |                           |
| PurchaseShortSale 個股融資融卷             | ShortSaleSell                    | 融券賣出                 |                           |
| PurchaseShortSale 個股融資融卷             | ShortSaleTodayBalance            | 融券今日餘額               |                           |
| PurchaseShortSale 個股融資融卷             | ShortSaleYesterdayBalance        | 融券昨日餘額               |                           |
| PurchaseShortSale 個股融資融卷             | Note                             | 註記，這欄會有空值，資料處理時可drop |                           |
| TaiwanStockDayTrading 當日沖銷交易標的及成交量值  | BuyAfterSale                     | 可否當沖                 |                           |
| TaiwanStockDayTrading 當日沖銷交易標的及成交量值  | Trading_Volume                   | 成交量                  |                           |
| TaiwanStockDayTrading 當日沖銷交易標的及成交量值  | BuyAmount                        | 買進金額                 |                           |
| TaiwanStockDayTrading 當日沖銷交易標的及成交量值  | SellAmount                       | 賣出金額                 |                           |
