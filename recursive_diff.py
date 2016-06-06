#!/usr/bin/python
# encoding=utf8

def recursive_diff(data, temp_data, tabs = ""):
    new_data = {}
    for k in data.keys():
        if type(data[k]) == type({}):
            if k not in temp_data:
                temp_data[k] = {}
            temp = recursive_diff(data[k], temp_data[k], tabs)  
            if temp:
                new_data[k] = {}
                new_data[k] = temp
        else:
            if k in temp_data:
                if data[k] != temp_data[k]:
                    new_data[k] = data[k]
            else:
                new_data[k] = data[k]
    return new_data
