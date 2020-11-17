import yfinance as yf
import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from math import floor



class Stock:

    def __init__(self, stockName, period,):
        self.stockName = stockName
        self.period = period
        self.history = yf.Ticker(stockName).history(period=self.period)
        self.date = self.history.index
        self.price = self.history["Close"]
        self.high = self.history["High"]
        self.low = self.history["Low"]
        self.volume = self.history["Volume"]
        self.vsma30 = self.volume.rolling(window=30).mean()
        self.day = [*range(len(self.history["Close"]))]
        #self.rsi = [100-(100/(1+(gain/loss))) for gain, loss in zip(self.avgGain(), self.avgLoss())]
        self.keylist = []
        self.buylist = []
        self.selllist = []
        self.lastlowlist = []
        self.open = self.history["Open"]



    def sma(self, days):
        return self.price.rolling(window=days).mean()


    def avgGain(self):

        avgGain = 15*[np.nan]
        templist = []

        for i in range(15, len(self.day)):
            count = 0
            totalgain = 0

            for j in range(i-14, i):
                if self.price[j] > self.price[j-1]:
                    count += 1
                    templist.append((self.price[j]-self.price[j-1])/self.price[j-1])
                else:
                    templist.append(np.nan)

            for j in range(len(templist)):
                if not np.isnan(templist[j]):
                    totalgain += templist[j]

            avgGain.append(totalgain/count)

        return avgGain


    def avgLoss(self):

        avgLoss = 15*[np.nan]
        templist = []

        for i in range(15, len(self.day)):
            count = 0
            totalloss = 0

            for j in range(i - 14, i):
                if self.price[j] < self.price[j-1]:
                    count += 1
                    templist.append((self.price[j] - self.price[j - 1]) / self.price[j - 1])
                else:
                    templist.append(np.nan)

            for j in range(len(templist)):
                if not np.isnan(templist[j]):
                    totalloss += templist[j]

            avgLoss.append(totalloss/count)

        avgLoss = [abs(n) for n in avgLoss]

        return avgLoss


    def smaAlgo(self, days):

        self.buylist = days*[np.nan]
        self.selllist = days*[np.nan]

        for j in range(days, len(self.day)):

            if self.price[j] > self.sma(days)[j]:
                if self.price[j-1] > self.sma(days)[j-1]:
                    self.buylist.append(np.nan)
                    self.selllist.append(np.nan)
                else:
                    self.buylist.append(self.price[j])
                    self.selllist.append(np.nan)

            elif self.price[j] < self.sma(days)[j]:
                if self.price[j-1] < self.sma(days)[j-1]:
                    self.buylist.append(np.nan)
                    self.selllist.append(np.nan)
                else:
                    self.buylist.append(np.nan)
                    self.selllist.append(self.price[j])


    def keyPointAlgo(self):
        self.keylist = [np.nan]
        for i in range(1, len(self.day)):
            if i == self.day:
                break
            if self.high[i] > self.high[i-1] and self.price[i] < self.low[i-1] and self.volume[i] > 1.5*self.volume[i-1]:
                self.keylist.append(self.price[i])
            else:
                self.keylist.append(np.nan)


    def simulate(self, capital, smadays):
        hold = False
        skip = False
        count = 0
        self.smaAlgo(smadays)
        for i in range(len(self.day)-1, -1, -1):
            if not np.isnan(self.buylist[i]):
                skip = True
                lastbuypoint = i
                break
            if not np.isnan(self.selllist[i]):
                skip = False
                break
        for i in range(len(self.day)):
            if skip and i == lastbuypoint:
                break
            if not np.isnan(self.buylist[i]):
                amount = floor(capital/self.buylist[i])
                capital -= self.buylist[i]*amount
                count += 1
                hold = True
            if not np.isnan(self.selllist[i]) and hold:
                capital += self.selllist[i]*amount
                count += 1
                hold = False
        return capital, count

    def keyPointAlgo2(self):
        self.keylist2 = [np.nan]
        for i in range(1, len(self.day)):
            if i == self.day:
                break
            if self.high[i] > self.price[i - 1] and self.low[i] < self.low[i - 1] and self.volume[i] > (2 *self.volume[i - 1]):
                self.keylist2.append(self.price[i])
            else:
                self.keylist2.append(np.nan)

    def keyPointAlgo3(self):
        self.keylist3 = [np.nan]
        for i in range(1, len(self.day)):
            if i == self.day:
                break
            if self.high[i] < self.high[i - 1] and self.low[i] < self.low[i - 1] and self.volume[i] > 2*self.volume[i-1] and self.open[i] < self.open[i-1] and self.open[i] > self.price[i]:
                self.keylist3.append(self.price[i])
            else:
                self.keylist3.append(np.nan)

    """def percentr(self):
        high = float()
        low = float()
        for i in range(self.date[i-14],self.date[i]):
            if self.high[i-1]<self.high[i]:
                high == self.high[i]
            if self.low[i-1]>self.low[i]:
                low == self.low[i]"""



def corr(price1, price2):
    corr = pearsonr(price1, price2)
    return corr

