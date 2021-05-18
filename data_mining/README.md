# BDSE18-Stock

資料合併

個股單一資料表存放於 merge 資料夾中，程式碼請見 dataframe_merge_finish.ipynb。

由於個股單一資料表皆不足 128MB，故預先準備一張所有股票合併為一張的資料表（檔名merge_dataframe.csv），視情況使用。

補充：TaiwanStockShareholding 的爬蟲資料有誤，已重新爬蟲存放於本目錄的 TaiwanStockShareholding 資料夾中

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
