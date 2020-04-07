import pandas

from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

from app.info import questionWithComplete

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

    print(len(params))
    print(test)

    for i in range(len(values)):
        for i2 in range(len(params)):
            if params[i2] in questionWithComplete:
                values[newParams[i2]][i] = 1 if values[params[i2]][i] == newParams[i2][3:] else 0
    
    return values

def ml(params, newParams, test_x):
    data = pandas.read_csv('all.csv')

    data = convertStringData(params, newParams, data, test_x)

    train_x = data[newParams]
    data_y = data[['Unnamed: 0']]

    test_x = [test_x]

    print(train_x)
    #print(test_x)

    model = LinearSVC()
    model.fit(train_x, data_y.values.ravel())

    prevision = model.predict(test_x)

    data = pandas.read_csv('all.csv')

    return data[prevision[0]:prevision[0] + 1]

# Example:
#print(ml(['intelligence', 'power', 'gender', 'is_tall', 'publisher'], ['intelligence', 'power', 'gender', 'is_tall', 'is_Marvel Comics'], [2, 1, 0, 1, 1]))