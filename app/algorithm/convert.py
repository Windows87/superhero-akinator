import pandas

pandas.options.mode.chained_assignment = None

data = pandas.read_json('https://raw.githubusercontent.com/akabab/superhero-api/master/api/all.json')

data = data.drop(columns = ['slug'])

data = data.assign(intelligence=0, strength=0, power=0, combat=0, speed=0, gender=0, is_tall=0, is_short=0, is_weight=0, is_light=0, is_bald=0, eye_color=0, publisher=0, place_of_birth=0, image=0)

for i in range(len(data)):
    #item = data[i]
    powerstats = ['intelligence', 'strength', 'power', 'speed', 'combat']
    
    # LOW = 0
    # MEDIUM = 1
    # HIGH = 1
    for i2 in range(len(powerstats)):
        powerstat = powerstats[i2]
        data[powerstat][i] = 0 if data.powerstats[i][powerstat] <= 40 else 1 if data.powerstats[i][powerstat] <= 80 else 2
    
    # MALE = 0
    # FEMALE = 1
    data['gender'][i] = 1 if data.appearance[i]['gender'] == 'Male' else 0

    # YES = 1
    # NO = 0
    # NOT DEFINED = -1
    cm = -1
    lb = -1

    if(data.appearance[i]['height'][0] != 'Shaker Heights, Ohio'):
        mt = float(data.appearance[i]['height'][1].replace(' meters', '')) if 'meters' in data.appearance[i]['height'][1] else -1
        cm = mt * 100 if mt != -1 else int(data.appearance[i]['height'][1].replace(' cm', ''))
        lb = int(data.appearance[i]['weight'][0].replace(' lb', '').replace('-', '0'))

    data['is_tall'][i] = 1 if cm >= 180 else -1 if cm == 0 else 0
    data['is_short'][i] = 1 if cm < 170 else -1 if cm == 0 else 0
    data['is_weight'][i] = 1 if lb >= 440 else -1 if lb == 0 else 0
    data['is_light'][i] = 1 if lb <= 154 else -1 if lb == 0 else 0
    data['is_bald'][i] = 1 if data.appearance[i]['hairColor'] == 'No Hair' else 0

    data['eye_color'][i] = data.appearance[i]['eyeColor']
    data['publisher'][i] = data.biography[i]['publisher']
    data['place_of_birth'][i] = data.biography[i]['placeOfBirth']

    data['image'][i] = data.images[i]['lg']

data = data.drop(columns = ['powerstats', 'appearance', 'biography', 'work', 'connections', 'images'])

data.to_csv(r'all.csv')