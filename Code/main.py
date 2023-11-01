from data_loader import load_dataset
from data_analysis import analyze_data
from visualize_data import visualization

if __name__ == '__main__':
    data = [['C:/Users/Dell/Documents/NM AI Project/Python Scripts/Measure Energy Consumption/MEC_dataset/AEP_hourly.csv','02-01-2017'],
                  ['C:/Users/Dell/Documents/NM AI Project/Python Scripts/Measure Energy Consumption/MEC_dataset/COMED_hourly.csv','08-01-2017'],
                  ['C:/Users/Dell/Documents/NM AI Project/Python Scripts/Measure Energy Consumption/MEC_dataset/DAYTON_hourly.csv','10-01-16'],
                  ['C:/Users/Dell/Documents/NM AI Project/Python Scripts/Measure Energy Consumption/MEC_dataset/DEOK_hourly.csv','06-01-17'],
                  ['C:/Users/Dell/Documents/NM AI Project/Python Scripts/Measure Energy Consumption/MEC_dataset/DOM_hourly.csv','01-01-17'],
                  ['C:/Users/Dell/Documents/NM AI Project/Python Scripts/Measure Energy Consumption/MEC_dataset/DUQ_hourly.csv','06-01-16'],
                  ['C:/Users/Dell/Documents/NM AI Project/Python Scripts/Measure Energy Consumption/MEC_dataset/EKPC_hourly.csv','08-01-17'],
                  ['C:/Users/Dell/Documents/NM AI Project/Python Scripts/Measure Energy Consumption/MEC_dataset/FE_hourly.csv','02-01-17'],
                  ['C:/Users/Dell/Documents/NM AI Project/Python Scripts/Measure Energy Consumption/MEC_dataset/NI_hourly.csv''07-01-09']]

    print("1.AEP\n2.COMED\n3.DAYTON\n4.DEOK\n5.DOM\n6.DUQ\n7.EKPC\n8.FE\n9.NI\n")
    n = int(input())
    if(n in range(1,10)):
        visualization(data[n-1][0],data[n-1][1])
        analyze_data(n-1, data[n-1][0])
    else:
        print("Invalid Input!")
