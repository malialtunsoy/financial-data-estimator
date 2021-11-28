from dataManager import dataManager

IBM_DAILY = "IBM_DAILY"
PHYSICAL_CURRENCY = "PHYSICAL_CURRENCY"
IBM_5MIN = "IBM_5MIN"
BTC_DAILY = "BTC_DAILY"
ETH_DAILY = "ETH_DAILY"

class estimator:
    def __init__(self):
        self.datas = {}
    def setDatas(self):
        self.datas[PHYSICAL_CURRENCY] = dataManager("physical_currency_list.csv")
        self.datas[BTC_DAILY] = dataManager("currency_daily_BTC_CNY.csv")
        self.datas[ETH_DAILY] = dataManager("currency_daily_ETH_USD.csv")
        self.datas[IBM_5MIN] = dataManager("intraday_5min_IBM.csv")
        self.datas[IBM_DAILY] = dataManager("daily_IBM.csv")

e = estimator()
e.setDatas()
e.datas[IBM_DAILY].printData()