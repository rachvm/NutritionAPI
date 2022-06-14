import csv
import requests


# takes user input and requests from api
appId = '#####'
appKey = '####'
ingredient = input('Enter an Ingredient')
x = requests.get('https://api.edamam.com/api/nutrition-data?app_id={}&app_key={}&'
                 'ingr={}'.format(appId, appKey, ingredient))

# printing specific data from api
nutrition = x.json()
totalNutrients = (nutrition['totalNutrients'])

#print(nutrition['totalWeight'])

# creates the CSV file
header = ['Ingredient', 'Weight', 'Calories', 'Carbs', 'Protein', 'Fat', 'Fibre','Calcium', 'Iron']
data = [ingredient, (nutrition['totalWeight']), (totalNutrients['ENERC_KCAL']['quantity']),
        (totalNutrients['CHOCDF']['quantity']), (totalNutrients['PROCNT']['quantity']),
        (totalNutrients['FAT']['quantity']), (totalNutrients['FIBTG']['quantity']),
        (totalNutrients['CA']['quantity']), (totalNutrients['FE']['quantity'])]

toWriteOrAppend = input('would you like to create a new csv file? y/n ')

# allows user to decide whether to create a new csv file or add to the existing file
if toWriteOrAppend == 'y':
    with open('nutritionData.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

    print('Completed')

elif toWriteOrAppend == 'n':
    with open('nutritionData.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    print('Completed')

else:
    print('Incorrect input, please try again')

