#Statistics Script NO TOUCHY PLEASE
#strictly for data creation
import json
import matplotlib.pyplot as plt

with open('NetworkVerbose.json', 'r') as JsonFile:
    data = json.load(JsonFile)

    
NumberOfActiveDevices = len(data)
print(NumberOfActiveDevices)













print("IP", ":", data["45.33.32.156"]["TCP"])

    




