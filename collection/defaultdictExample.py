from collections import defaultdict

""" Default Dictionary """

details = {'123': {"harini": "python trainee"}, '456': {"monisha": "python trainee"},
           '789': {"siva": "frontend trainee"}, '1011':("sairabegum", "data analyst"),
           '1213':{"sairabegum", "data_scientist"}}
new_default_dict = defaultdict(dict)
for ids,  value in details:
    new_default_dict[ids] = value

print(new_default_dict)
print(new_default_dict['123'])

new_default_dict1 = defaultdict(dict)
new_default_dict1['jsd']

print(new_default_dict1)