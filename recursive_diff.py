#!/usr/bin/python
# encoding=utf8

def recursive_diff(data, temp_data, tabs = ""):
    # Set debug to True to see summary output of operations
    debug = False
    
    if debug:
        tabs = tabs + "\t\t"
    
    new_data = {}
    
    for k in data.keys():

        if debug:
            print tabs+"data["+k+"] = ", data[k]
            print tabs+"temp_data["+k+"] = ", temp_data[k]
            print "\n"

        if type(data[k]) == type({}):
            if debug:
                print tabs+"\tdata["+k+"] == dict::"
                print tabs+"\tcomparing....\n"

            # Return only objects that have changed
            # then load those into the new_data dict in thisa scope.
            # The new_data dict entries will always be un-initialized here in the logic

            if k not in temp_data:
                temp_data[k] = {}

            temp = recursive_diff(data[k], temp_data[k], tabs)  

            if temp:
                if debug:
                    print tabs+"\t\tLoading new dict data into new_data: "
                    print tabs+"\t\tNew Data Before: ", new_data
                    print tabs+"\t\tTemp Before: ", temp
                new_data[k] = {}
                new_data[k] = temp

                if debug:
                    print "\n"
                    print tabs+"\t\tNew Data after: ", new_data
                    print tabs+"\t\tnew_data[",k,"]: ", new_data[k]
                
            #else:
            #    print tabs+"\t\tNo new dict data returned"

        else:
            if debug:
                print tabs+"\tdata["+k+"] != dict"
            

            if k in temp_data:
                if data[k] != temp_data[k]:
                    new_data[k] = data[k]
                    if debug:
                        print tabs+"\t\tUpdated new_data: ", new_data
            else:
                new_data[k] = data[k]


        if debug:
            print "\n"
    if debug:
        print tabs+"Returning new_data dict: ", new_data
    
    return new_data



# Existing Dict of data
b = {'thing1':'22','thing2': {'1': '?', '2': '+'}, 'thing3': {'users': '1', 'cpu': '.1', "note":"You should not see the thing3 dict at all"}, "notInFirstDict":"You should not see this"}


# Now you have a second dict, and some values may or may not be different.
a = {'thing1':'99','thing2': {'1': '+', '2': '-',}, 'thing3': {'users': '1', 'cpu': '.1', "note":"You should not see the thing3 dict at all"}, "notInSecondDict":"You should see this", "listTest":[1,2,3,4,5,6,7,8,9, "You should see this"]}

# Now lets return the things from dict a that differe from what is in dict b
# Entries in dict b that do not exist in dict a and just ignored. So dict b could have anything in it
# But you are really only concerned with the things in dict that are not the same as dict b.
# So we return a new dict containing the data that has changed from the data in dict b.
print "\n\n"

print "Dict B: ", b, "\n"

print "Dict A: ", a, "\n"

print "Difference: ", recursive_diff(a,b)

print "\n\n"

# Expected Output: 

#Dict B:      {'thing2': {'1': '?', '2': '+'}, 'thing3': {'note': 'You should not see the thing3 dict at all', 'users': '1', 'cpu': '.1'}, 'thing1': '22', 'notInFirstDict': 'You should not see this'} 
#Dict A:      {'thing2': {'1': '+', '2': '-'}, 'thing3': {'note': 'You should not see the thing3 dict at all', 'users': '1', 'cpu': '.1'}, 'thing1': '99', 'listTest': [1, 2, 3, 4, 5, 6, 7, 8, 9, 'You should see this'], 'notInSecondDict': 'You should see this'} 
#Difference:  {'thing2': {'1': '+', '2': '-'}, 'notInSecondDict': 'You should see this', 'thing1': '99', 'listTest': [1, 2, 3, 4, 5, 6, 7, 8, 9, 'You should see this']}

