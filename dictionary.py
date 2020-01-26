employee = {
    'name':'Anil',
    'company':'huawei',
    'role':'STL',
    'age':31,
    'team':['neeraj', 'shobhit', 'anusha'],
    'manager': {
        'report':'Dinesh',
        'Line':'Nagaraj'
    }
}

def listDictProps(dictionary):
    for prop,val in dictionary.items():
        if type(val) is dict:
            listDictProps(val)
        else:
             print(prop,':',val)
       

#listDictProps(employee)
