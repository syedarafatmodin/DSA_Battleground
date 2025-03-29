from typing import List, Dict

def find_consistent_customers(surveys: List[Dict]) -> List[str]:
    consistent_customers = []

    for survey in surveys:
        responses = survey["responses"].values()
        if len(responses) >= 3 and len(set(responses)) == 1:
            consistent_customers.append(survey["name"])

    return consistent_customers

#test Case
surveys = [
    {'name': 'Amit', 'responses': {'Q1': 5, 'Q2': 5, 'Q3': 5}},
    {'name': 'Priya', 'responses': {'Q1': 4, 'Q2': 4, 'Q3': 5}},
    {'name': 'Sahil', 'responses': {'Q1': 3, 'Q2': 3, 'Q3': 3, 'Q4': 3}},
    {'name': 'Riya', 'responses': {'Q1': 1, 'Q2': 2}},
    {'name': 'Karan', 'responses': {'Q1': 5, 'Q2': 5, 'Q3': 5, 'Q4': 4}}
]

print(find_consistent_customers(surveys))
