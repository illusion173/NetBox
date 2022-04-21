import json
from re import S
import matplotlib.pyplot as plt
import numpy as np

def mainstatScript(userInputFileName):
    with open(userInputFileName, 'r') as JsonFile:
        data = json.load(JsonFile)
    amountofComputers = len(data.keys())
    #print("Amount of computers: {}".format(amountofComputers))
    #[dictlist.extend(k,v) for k,v in data.items()]    
    Occurances = {}
    portStorage = []
    piLabelKeys = []
    piValues = []
    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%\n{:d} open".format(pct, absolute)
    def countCurrencies(storage, value):
        try: 
            storage[value] = storage[value] + 1
        except KeyError as e:
            storage[value] = 1
        return
    for k,v in data.items():
        for port in v['tcp'].keys():
        
            portStorage.append(port)
    #print(portStorage)
    for data in portStorage:
        countCurrencies(Occurances, data)
    #print(Occurances)
    #for k, v in Occurances.items():
    #    print("Key " + k + " has occurred "  + str(v) + " times")
    portNumber = list(Occurances.keys())
    amountOfTimes = list(Occurances.values())
    def bar():
        c = ['red', 'black', 'gray', 'blue', 'green']
        plt.bar(range(len(Occurances)), amountOfTimes, tick_label=portNumber, color=c)
        plt.xlabel('Port Number', fontweight='bold', color = 'blue', fontsize='12', horizontalalignment='center')
        plt.ylabel('Number Amount Open', fontweight='bold', color = 'blue', fontsize='12', horizontalalignment='center')
        plt.suptitle("Ports Open on Network - Bar\n\n")
        plt.savefig('bar.png')
        
    def piChart():
        for k,v in Occurances.items():
            piLabelKeys.append(k)
            piValues.append(v) 
        fig, ax = plt.subplots(figsize=(6, 5), subplot_kw=dict(aspect="equal"))
        wedges, texts, autotexts = ax.pie(piValues, labels= piLabelKeys, autopct=lambda pct: func(pct, piValues),textprops={'fontsize': 11},shadow=True,radius=1)
        plt.setp(autotexts, size=9, weight="bold")
        ax.set_title("Ports Open on Network - Pie\n")
        plt.axis('equal')
        plt.savefig('pichart.png')
        plt.close()
        
    piChart()
    bar()
    return amountofComputers

mainstatScript("NetworkVerboseTest.json")
