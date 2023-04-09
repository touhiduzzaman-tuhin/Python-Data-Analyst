# find your food item from chinese, italian, bangladesh food

chinese = ['fried_rice', 'chicken_roll', 'porn_item']
bangladesh = ['puri', 'samusa', 'beguni', 'piyazu', 'biriyani']
indian = ['pani_puri', 'ruit', 'alur_dom']

food = input('Enter Your Food Name : ')

if (food in chinese):
    print('Chinese Food')
elif (food in bangladesh):
    print('Bangladeshi Food')
elif (food in indian):
    print('Indian Food')
else:
    print('Other Type Food')