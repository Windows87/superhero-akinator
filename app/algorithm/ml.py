import pandas

from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

def convertStringTest(params, values):
    newParams = params[:]

    for i in range(len(params)):
        if(type(values[i]) == str):
            newParams[i] = 'is_' + values[i]
            values[i] = 1
            
    return [newParams, values] 

def convertStringData(params, newParams, values, test):
    assign = {}

    for i in range(len(newParams)):
        if(not newParams[i] in params):
            assign[newParams[i]] = 0

    values = values.assign(**assign)

    for i in range(len(values)):
        for i2 in range(len(params)):
            if(type(test[i2]) == str):
                values['is_' + newParams[i2]][i] = 1 if value[params[i2]][i] == test[i2] else 0
    
    return values

def ml(params, test_x):
    data = pandas.read_csv('all.csv')

    newParams, new_test_x = convertStringTest(params, test_x)
    data = convertStringData(params, newParams, data, test_x)

    data_x = data[newParams]
    data_y = data[['Unnamed: 0']]

    test_x = [test_x]

    scaler = StandardScaler()
    scaler.fit(data_x)

    train_x = scaler.transform(data_x)
    test_x = scaler.transform(test_x)

    model = LinearSVC()
    model.fit(train_x, data_y.values.ravel())

    prevision = model.predict(test_x)

    data = pandas.read_csv('all.csv')

    return data[prevision[0]:prevision[0] + 1]

# Example:
#print(ml(['intelligence', 'power', 'gender', 'is_tall', 'publisher'], [2, 1, 0, 1, 'Marvel Comics']))