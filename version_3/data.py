import pandas as pd
import pickle

def get_data():
    with open('data.pickle','rb') as fp:
        return pickle.load(fp)

    data = pd.read_csv("ecomm.csv",encoding='iso-8859-1')
    data = data.dropna()
    data.InvoiceDate = pd.to_datetime(data.InvoiceDate)
    with open('data.pickle','wb') as fp:
        pickle.dump(data,fp)
    return data


data = get_data()

data.UnitPrice = data.UnitPrice*100
data = data[(data.InvoiceDate >= '2011-01-01') & (data.InvoiceDate <= '2011-06-30') & (data.UnitPrice > 0) & (data.UnitPrice <= 1000)]

start_date = data.InvoiceDate.min()
end_date = data.InvoiceDate.max()

