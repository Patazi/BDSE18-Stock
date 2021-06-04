# 爬蟲程式名稱及其產生的欄位index及說明一覽

### 證交所單股每日交易量資料只有2010年1月4日後的
### 股東持股分級表資料只有2017年後的
### 除權息日程表只有2008年後的，有的股票本身沒有這份資料就不會產生csv檔，也不會爬下東西。沒有除權息資料的股票請見 DividendResult_empty_list.csv 一覽表。
### 融資融券表有的股票本身沒有這份資料就不會產生csv檔，也不會爬下東西。沒有融資融券資料的股票請見 PurchaseShortSale_empty_list.csv 一覽表。

產生表格對照：
1. 上市上櫃台股清單-stock_list.csv
2. 單股每日交易-{股票代碼}_daily.csv
3. 法人買賣表-{股票代碼}_InstitutionalInvestorsBuySell.csv
4. 股東持股分級表-{股票代碼}_HoldingSharesPer.csv
5. 融資融劵表-{股票代碼}_PurchaseShortSale.csv
6. 除權息日程表-{股票代碼}_DividendResult.csv

| 程式名稱及其產生的欄位index                                                                         | 欄位名稱                           | 原始資料型態        | 期望轉換成的資料格式       | 欄位說明                                                                                                                                                                                                                                                                                                |
| :---------------------------------------------------------------------------------------- | :------------------------------ | :------------- | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| generate\_stocklist<br>（產生上市上櫃台股清單）                                                          | **Column**                        | **Origin\_Dtype** | **Desired\_Dtype**   | **說明**                                                                                                                                                                                                                                                                                                  |
| 0                                                                                        | stock\_id                      | int64         | object           | 股票代碼（primary\_key)                                                                                                                                                                                                                                                                                  |
| 1                                                                                        | stock\_name                    | object        | object           | 公司名稱（primary\_key)                                                                                                                                                                                                                                                                                  |
| 2                                                                                        | ISIN\_Code                     | object        | object           | 國際證券辨識號碼(ISIN Code)                                                                                                                                                                                                                                                                                 |
| 3                                                                                        | Listing\_date                  | object        | datetime64\[ns\] | 上市日                                                                                                                                                                                                                                                                                                 |
| 4                                                                                        | Listing\_category              | object        | object           | 市場別                                                                                                                                                                                                                                                                                                 |
| 5                                                                                        | Industry\_category             | object        | object           | 產業別                                                                                                                                                                                                                                                                                                 |
| 6                                                                                        | CFICode                        | object        | object           | CFICode                                                                                                                                                                                                                                                                                             |
| twse\_daily\_multiple\_stock<br>（證交所單股每日交易量）<br>OTC\_twse\_daily\_multiple\_stock<br>（單股每日交易量)| **Column**                         | **Origin\_Dtype** | **Desired\_Dtype**   | **說明**                                                                                                                                                                                                                                                                                                  |
| 0                                                                                        | stock\_id                      | int64         | object           | 股票代碼（primary\_key)                                                                                                                                                                                                                                                                                  |
| 1                                                                                        | stock\_name                    | object        | object           | 公司名稱（primary\_key)                                                                                                                                                                                                                                                                                  |
| 2                                                                                        | date                           | object        | datetime64\[ns\] | 交易日期                                                                                                                                                                                                                                                                                                |
| 3                                                                                        | Volume                         | float64       | float64          | 成交量                                                                                                                                                                                                                                                                                                 |
| 4                                                                                        | Volume\_Cash                   | float64       | float64          | 成交金額                                                                                                                                                                                                                                                                                                |
| 5                                                                                        | Open                           | float64       | float64          | 開盤價                                                                                                                                                                                                                                                                                                 |
| 6                                                                                        | High                           | float64       | float64          | 最高價                                                                                                                                                                                                                                                                                                 |
| 7                                                                                        | Low                            | float64       | float64          | 最低價                                                                                                                                                                                                                                                                                                 |
| 8                                                                                        | Close                          | float64       | float64          | 收盤價                                                                                                                                                                                                                                                                                                 |
| 9                                                                                        | Change                         | float64       | float64          | 漲跌幅（會有正負號）                                                                                                                                                                                                                                                                                          |
| 10                                                                                       | Order                          | float64       | float64          | 交易筆數                                                                                                                                                                                                                                                                                                |
| TaiwanStockInstitutionalInvestorsBuySell<br>（法人買賣表） | **Column**                         | **Origin\_Dtype** | **Desired\_Dtype**   | **說明**                                                                                                                                                                                                                                                                                                  |
| 0                                                                                        | stock\_id                      | int64         | object           | 股票代碼（primary\_key)                                                                                                                                                                                                                                                                                  |
| 1                                                                                        | stock\_name                    | object        | object           | 公司名稱（primary\_key)                                                                                                                                                                                                                                                                                  |
| 2                                                                                        | date                           | object        | datetime64\[ns\] | 日期                                                                                                                                                                                                                                                                                                  |
| 3                                                                                        | buy                            | float64       | float64          | 買進                                                                                                                                                                                                                                                                                                  |
| 4                                                                                        | name                           | object        | object           | 類別，分為：<br>Dealer<br>Foreign\_Investor<br>Investment\_Trust<br>以上三種類別                                                                                                                                                                                                                                |
| 5                                                                                        | sell                           | float64       | float64          | 賣出                                                                                                                                                                                                                                                                                                  |
| TaiwanStockHoldingSharesPer<br>（股東持股分級表）                         | **Column**                         | **Origin\_Dtype** | **Desired\_Dtype**   | **說明**                                                                                                                                                                                                                                                                                                  |
| 0                                                                                        | stock\_id                      | int64         | object           | 股票代碼（primary\_key)                                                                                                                                                                                                                                                                                  |
| 1                                                                                        | stock\_name                    | object        | object           | 公司名稱（primary\_key)                                                                                                                                                                                                                                                                                  |
| 2                                                                                        | date                           | object        | datetime64\[ns\] | 日期                                                                                                                                                                                                                                                                                                  |
| 3                                                                                        | HoldingSharesLevel             | object        | object           | 持股分級，分為：<br>1-999<br>1,000-5,000<br>5,001-10,000<br>10,001-15,000<br>15,001-20,000<br>20,001-30,000<br>30,001-40,000<br>40,001-50,000<br>50,001-100,000<br>100,001-200,000<br>200,001-400,000<br>400,001-600,000<br>600,001-800,000<br>800,001-1,000,000<br>more than 1,000,001<br>total<br>以上16個層級 |
| 4                                                                                        | people                         | float64       | float64          | 人數                                                                                                                                                                                                                                                                                                  |
| 5                                                                                        | percent                        | float64       | float64          | 比例                                                                                                                                                                                                                                                                                                  |
| 6                                                                                        | unit                           | float64       | float64          | 股數                                                                                                                                                                                                                                                                                                  |
| TaiwanStockMarginPurchaseShortSale<br>（融資融劵表）             | **Column**                         | **Origin\_Dtype** | **Desired\_Dtype**   | **說明**                                                                                                                                                                                                                                                                                                  |
| 0                                                                                        | stock\_id                      | int64         | object           | 股票代碼（primary\_key)                                                                                                                                                                                                                                                                                  |
| 1                                                                                        | stock\_name                    | object        | object           | 公司名稱（primary\_key)                                                                                                                                                                                                                                                                                  |
| 2                                                                                        | date                           | object        | datetime64\[ns\] | 日期                                                                                                                                                                                                                                                                                                  |
| 3                                                                                        | MarginPurchaseBuy              | float64       | float64          | 融資買進                                                                                                                                                                                                                                                                                                |
| 4                                                                                        | MarginPurchaseCashRepayment    | float64       | float64          | 融資現金償還                                                                                                                                                                                                                                                                                              |
| 5                                                                                        | MarginPurchaseLimit            | float64       | float64          | 融資限額                                                                                                                                                                                                                                                                                                |
| 6                                                                                        | MarginPurchaseSell             | float64       | float64          | 融資賣出                                                                                                                                                                                                                                                                                                |
| 7                                                                                        | MarginPurchaseTodayBalance     | float64       | float64          | 融資今日餘額                                                                                                                                                                                                                                                                                              |
| 8                                                                                        | MarginPurchaseYesterdayBalance | float64       | float64          | 融資昨日餘額                                                                                                                                                                                                                                                                                              |
| 9                                                                                        | OffsetLoanAndShort             | float64       | float64          | 資券互抵                                                                                                                                                                                                                                                                                                |
| 10                                                                                       | ShortSaleBuy                   | float64       | float64          | 融券買進                                                                                                                                                                                                                                                                                                |
| 11                                                                                       | ShortSaleCashRepayment         | float64       | float64          | 融券償還                                                                                                                                                                                                                                                                                                |
| 12                                                                                       | ShortSaleLimit                 | float64       | float64          | 融券限額                                                                                                                                                                                                                                                                                                |
| 13                                                                                       | ShortSaleSell                  | float64       | float64          | 融券賣出                                                                                                                                                                                                                                                                                                |
| 14                                                                                       | ShortSaleTodayBalance          | float64       | float64          | 融券今日餘額                                                                                                                                                                                                                                                                                              |
| 15                                                                                       | ShortSaleYesterdayBalance      | float64       | float64          | 融券昨日餘額                                                                                                                                                                                                                                                                                              |
| 16                                                                                       | Note                           | object        | object           | 註記，這欄會有空值，資料處理時可drop                                                                                                                                                                                                                                                                                |
| TaiwanStockDividendResult（除權息日程表）（若這項資料該股票本來就無資料，就不會爬下東西，也不會有該csv檔） | **Column**                      | **Origin\_Dtype** | **Desired\_Dtype**   | **說明**                                                    |
| 0                                                                   | stock\_id                   | int64         | object           | 股票代碼                                                  |
| 1                                                                   | stock\_name                 | object        | object           | 公司名稱                                                  |
| 2                                                                   | date                        | object        | datetime64\[ns\] | 日期                                                    |
| 3                                                                   | before\_price               | float64       | float64          | 除權息前收盤價                                               |
| 4                                                                   | after\_price                | float64       | float64          | 除權息後收盤價                                               |
| 5                                                                   | stock\_and\_cache\_dividend | float64       | float64          | 權息值                                                   |
| 6                                                                   | stock\_or\_cache\_dividend  | object        | object           | 權or息，共有：<br>權息<br>權<br>息<br>除權<br>除息<br>除權息<br>以上六種格式 |
| 7                                                                   | max\_price                  | float64       | float64          | 漲停價格                                                  |
| 8                                                                   | min\_price                  | float64       | float64          | 跌停價格                                                  |
| 9                                                                   | open\_price                 | float64       | float64          | 開盤價                                                   |
| 10                                                                  | reference\_price            | float64       | float64          | 減除股利參考價                                               |