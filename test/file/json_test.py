import json



cous = {1: 'Linux', 2: 'Git', 3: 'Vim'} 
 
file1 = ('1.json')
with open (file1,'w') as f:
    json.dump(cous,f)


with open (file1,'r') as f:
    data = json.load(f)
    print (data)
