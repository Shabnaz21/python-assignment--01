mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here

import random

mobile_specification = mobile_data.get('data')
mobile_rate = mobile_data.get('exchnage_rate')

for mobile in mobile_specification:
    smartphone_name = mobile.get('name')
    price = mobile.get('price')
    usd = float(price.strip(' USD'))
    bdt = round(usd * mobile_rate)
    smartphone_made = mobile.get('made')

    mobile_template = [
        f'{smartphone_name} is now trending in smartphon market but this phone has lack of certain apps and services that are available on other phones. Overall, it\'s costs almost {usd} USD,which is about the same as {bdt} BDT. the {smartphone_name} is a decent phone for the price. This phone made in {smartphone_made}.',

        f'The {smartphone_name} is one of the most popular smartphones on the market and its price reflects that, this phone made in {smartphone_made}. The {smartphone_name} retails for {usd} USD, which is about the same as {bdt} BDT. Making it one of the more expensive smartphones available. Despite its high price tag, the {smartphone_name} is a popular choice for many consumers due to its sleek design, powerful hardware, and robust operating system.'
        
        f'The {smartphone_name} is very good phone this phone made in {smartphone_made} and it\'s costs almost {usd} USD, which is about the same as {bdt} BDT.',

        f'{smartphone_name} phone has some good features, like a large screen and good camera, this phone made in {smartphone_made} but it also has some drawbacks, it\'s costs almost {usd} USD, which is about the same as {bdt} BDT.',
]
    print(random.choice(mobile_template))

