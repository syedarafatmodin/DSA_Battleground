cities = [
    {'name': 'Mumbai', 'areas': {
        'Andheri': [32, 33, 31, 30, 29, 34, 35],
        'Bandra': [31, 32, 30, 30, 31, 33, 34]
    }},
    {'name': 'Delhi', 'areas': {
        'Rohini': [28, 29, 27, 30, 31, 32, 29],
        'Saket': [33, 35, 36, 34, 33, 32, 31]
    }},
    {'name': 'Chennai', 'areas': {
        'T Nagar': [34, 35, 36, 37, 34, 35, 33],
        'Velachery': [32, 31, 33, 34, 32, 30, 31]
    }}
]

result = [
    city['name']
    for city in cities
    if all(sum(temps) / len(temps) > 30 for temps in city['areas'].values())
]

print(result)
