x = [ [5,2,3], [10,8,9] ]
print(x)
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(students)
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(sports_directory)
sports_directory['soccer'][0]='Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
print(z)
z[0]['y']=30
print(z)

def iterateDictionary(some_list):
    for i in some_list:
        print("first_name - ", i['first_name'] + ", last_name - ", i['last_name'])
        
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        if key_name in i.keys():
            print(i[key_name])

def printInfo(some_dict):
    myKeys = list(some_dict)
    for i in myKeys:
        print(len(some_dict[i]), i.upper())
        for j in some_dict[i]:
            print(j)
        print('\n')
        

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


#iterateDictionary(students)

myNames = ['first_name','last_name']
for i in myNames:
    key_name = i
    #iterateDictionary2(key_name, students)
    print('\n')
    
printInfo(dojo)