# python-dict-recursive-diff
Recursively compares 2 Python Dicts. returns dict. Maintains original structure of first dict, and returns a dict with only the keys and values that differ in the second dif.


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

