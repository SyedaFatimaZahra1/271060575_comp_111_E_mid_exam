# to add value in dict
a = dict()
a["money"] = 12
a["ting"] = "ping"
a["zingy"] = "shoom"
print(a)
# to print single key
print(a["money"])
purse={'sing':"tatheer" , 'ding':"zahra" , "ping":23 }
print(purse)
# to amke dict in another shape
bag={
    "tathhher" : 1 ,
    "zahra" : 2 ,
    "jaff" : "end"
}
# to find length
print(len(bag))
my_dict = {"fantasy":"1" , "horror":"2" , "mystery":"3"}
print(my_dict)
my_dict["fiction"] = "4"
print(my_dict)
# to print like items() in complex way
for key in my_dict:
    print(key)
for keys in my_dict:
    key1=my_dict[keys]
    print(key1)
print(len(my_dict))
# to check presence
if "fantasy" in my_dict:
    print("pressent")
else:
    print("absent")
# to created nested dict
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(people)
# to access items in nested_dict
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
# to use items() in pretty way
for title, rating in my_dict.items():
    print(f"Book: {title}, Rating: {rating}")
my_dict = {'key1': 'value1', 'key2': 'value2'}
for obj in my_dict.items():
    print(obj)
for obj in my_dict.values():
    print(obj)
for obj in my_dict.keys():
    print(obj)
# to use get()    
wife = {'name': 'Rose', 'age': 33}
# get gives "none" when key not present and you can change it to "lover"
sentence1 = f'My wife name is {wife.get("name")}'
sentence2 = f'She is {wife.get("age")} years old.'
sentence3 = f'She is deeply in love with {wife.get("husband", "herself")}'
print(sentence1)
print(sentence2)
print(sentence3)
# to combine two dicts(1st method)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
merged_dict = dict1
print(merged_dict)
# to use pop()
my_dict = {'a': 1, 'b': 2, 'c': 3}
value_b = my_dict.pop('b')
print(f"Value for 'b': {value_b}")
print(f"Updated dictionary: {my_dict}")
# to use popitem()
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_value_pair = my_dict.popitem()
print(f"Removed key-value pair: {key_value_pair}")
print(f"Updated dictionary: {my_dict}")
# to use del()
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']
print(f"Updated dictionary: {my_dict}")
# to use clear()
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(f"Updated dictionary after clear: {my_dict}")

#to convert two lists into dict
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res_dict = dict(zip(keys, values))
print(res_dict)
# to merge 2 dicts (2nd way)
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}
# solution
print(sampleDict['class']['student']['marks']['history'])
# to get key of minimum value from a dict
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sample_dict ))
# to sort by asending/descending value
my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted by ascending value:", sorted_dict_asc)
print("Sorted by descending value:", sorted_dict_desc)
# to print dict where value is ** of key
my_dict = {'a': 2, 'b': 3, 'c': 4}
squared_dict = {key: value**2 for key, value in my_dict.items()}
print("Original dictionary:", my_dict)
print("Dictionary with values squared:", squared_dict)
# to sum all items in a dict
my_dict = {'a': 5, 'b': 2, 'c': 8}
sum_of_values = sum(my_dict.values())
print("Sum of values:", sum_of_values)
# to multiply all items in a dict
my_dict = {'a': 2, 'b': 3, 'c': 4}
product_of_values = 1
for value in my_dict.values():
    product_of_values *= value
print("Product of values:", product_of_values)




























