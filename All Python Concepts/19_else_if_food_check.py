# find your food item from chinese, italian, bangladesh food

chinese = ['fried-rice', 'nuodles', 'momo']
italian = ['pizza', 'pasta', 'mushroom']
bangladeshi = ['puri', 'samusa', 'ruti', 'beguni']

food = input('Enter Your food name : ')

if food in chinese:
    print('Chinese Food')
elif food in bangladeshi:
    print('Bangladeshi Food')
elif food in italian:
    print('Italian Food')
else:
    print('Out of list item')