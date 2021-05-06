from pytrends.request import TrendReq
import pandas as pd
import time
import random
keyword = "2603"
local = "TW"
start_year ="2018-1-1"
end_year ="2021-4-1"

def set_time(year,day,mounth ):
    time_start = f"{year}-{day}-{mounth}"
    time_start = time.strptime(time_start, "%Y-%d-%m")
    time_start = time.strftime("%Y-%d-%m", time_start)
    return time_start
start_year =start_year.split("-")
end_year = end_year.split("-")

#%%
time_start = set_time(start_year[0],start_year[1],start_year[2])
time_end = set_time(end_year[0],end_year[1],end_year[2])


pytrend = TrendReq(hl='en-' + local, tz=360)
pytrend.build_payload(kw_list=[keyword], cat=0, timeframe=f'{time_start} {time_end}', geo=local, gprop='')
year_month = pytrend.interest_over_time()
year_month = pd.DataFrame(year_month)


count = 0
df = []
for i in range(int(start_year[0]),int(end_year[0])+1):
    m = 1
    while m <= 12:
        if i == 2021 and m == 4:
            break
        mounth_end = pd.date_range(start=set_time(i, m, 1), periods=1, freq='M')
        mounth_end = str(mounth_end[0]).strip().replace("00:00:00", "").replace(" ","")

        time.sleep(random.randint(1,3))
        pytrend.build_payload(kw_list=[keyword], cat=0, timeframe=f'{set_time(i, m, 1)} {mounth_end}', geo=local, gprop='')

        day = pd.DataFrame(pytrend.interest_over_time())
        month = year_month.iloc[count, 0]
        day_sum = day[keyword].sum()
        day = (day[keyword] / day_sum)*month
        day = pd.DataFrame(day)
        print(day)
        df.append(day)
        m +=1

#%%
df2 = pd.concat(df)
print(df2)
#%%
import matplotlib.pyplot as plt

df2.plot()
plt.show()



