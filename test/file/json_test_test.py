import json

list1 =  [{
    'user_id': 1000,
    'name': 'Shiyan',
    'pass': 10,
    'study_time': 50,
},
{
    'user_id': 2000,
    'name': 'Lou',
    'pass': 15,
    'study_time': 171,
}]


with open('1.json','w') as f:
    for i in list1:
        json.dump(i,f)