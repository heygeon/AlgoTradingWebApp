def idea(stock):

    import matplotlib.pyplot as plt
    import numpy as np

    #stock.keyPointAlgo()


    # Percent R indicator
    temph = []
    templ = []
    hh = []
    ll= []
    high = float()
    low = float()
    perR_list = []
    date = []
    overb = []
    overs = []
    buy = []
    sell = []
    overbdate =[]
    oversdate = []


    for i in range(len(stock.high)):
        if i < 13:
            temph.append(stock.high[i])
            templ.append(stock.low[i])
            ll.append(np.nan)
            hh.append(np.nan)
        if i ==13:
            temph.append(stock.high[i])
            templ.append(stock.low[i])
            ll.append(min(templ))
            hh.append(max(temph))
        if i >13:
            temph.remove(temph[0])
            templ.remove(templ[0])
            temph.append(stock.high[i])
            templ.append(stock.low[i])
            ll.append(min(templ))
            hh.append(max(temph))


    for i in range(len(hh)):
        if i >=13:
            perR = ((hh[i]-stock.price[i])/(hh[i]-ll[i]))*-100
            perR_list.append(perR)
        else:
            perR_list.append(np.nan)

    #tabel ={"%R":perR_list,"Date":stock.date}
    #tb = pd.DataFrame(tabel)

    for i in range(len(stock.price)):

        if perR_list[i] > -10 :

            overb.append(stock.price[i])
            overbdate.append(stock.day[i])
            oversdate.append(np.nan)
            overs.append(np.nan)

        elif perR_list[i] < -90:

            overs.append(stock.price[i])
            oversdate.append(stock.day[i])
            overbdate.append(np.nan)
            overb.append(np.nan)
        else:
            overb.append(np.nan)
            overbdate.append(np.nan)
            oversdate.append(np.nan)
            overs.append(np.nan)
    t = 0
    tempw = []
    smalist = []
    top = []
    bottom = []
    for i in range(len(stock.sma(3))):
        if i == len(stock.sma(3))-1:
            smalist.append((np.nan))
            break
        if stock.sma(3)[i]>stock.sma(3)[i-2] and stock.sma(3)[i]>stock.sma(3)[i+1]:
            smalist.append(stock.sma(3)[i])
        else:
            smalist.append((np.nan))

    fig = plt.figure()
    plt.style.use('classic')
    plt.plot(stock.day, stock.price, label = stock.stockName)
    plt.plot(stock.day, smalist, label = "wave",marker="^", color="black")
    plt.plot(stock.day, stock.sma(3), label = "SMA3", color="orange")
    plt.plot(stock.day, stock.sma(5), label= "SMA6", color="purple")
    #plt.plot(stock.day, top, label = "top",marker="^", color="black")
    #plt.plot(stock.day, bottom, label = "bottom",marker="^", color="black")
    plt.plot(stock.day, overb,label="sell",  marker="o", color="red")
    plt.plot(stock.day, overs, label= "buy", marker="o", color="green")
    plt.title(stock.stockName.upper())
    plt.xlabel("Day")
    plt.ylabel("Adj Close Price USD($)")
    plt.legend(loc="upper left")

    return fig