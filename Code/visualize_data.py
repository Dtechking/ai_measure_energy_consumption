import matplotlib.pyplot as plt
from data_loader import load_dataset

def visualization(file,date):
    
    df = load_dataset(file)
    train_data = df.loc[df.index < date]
    test_data = df.loc[df.index >= date]
    fig, ax = plt.subplots(figsize = (35,20))
    train_data.plot(ax = ax, label = 'Training Data')
    test_data.plot(ax = ax, label = 'Training Data')
    #df.plot(figsize=(35,20))
    plt.show()
