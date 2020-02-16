TEST_NAME_DATA = [
    ['Anil', 'Anil', 'Anil'],
    ['Anil Kumar', 'Anil', 'Kumar'],
    ['Anil Kumar S', 'Anil', 'Kumar S'],
    ['S Anil Kumar', 'Anil', 'Kumar S'],
    ['Anil K S', 'Anil', 'K S'],
    ['K S Anil', 'Anil', 'K S'],
    ['K S A', '', ''],
    ['Anil K', 'Anil', 'K'],
    ['K Anil', 'Anil', 'K'],
    ['K S Anil Kumar', 'Anil', 'Kumar K S'],
    ['Anil Kumar Kumar', 'Anil', 'Kumar Kumar'],
    ['Anil Kumar1 Kumar2 Kumar3 Kumar4', 'Anil' , 'Kumar1 Kumar2 Kumar4'],
    ['A K S Anil Kumar1 Kumar2 Kumar3 Kumar4 Kumar5', 'Anil','Kumar1 Kumar5 A K S'],
    ['A K Anil C S', 'Anil', 'C S A K'],
    ['A K Anil C Kumar', 'Anil', 'C Kumar A K'],
    ['A K Anil C', 'Anil', 'C A K'],
    [None, '', ''],
    ['', '', ''],
    [' ', '', ''],
]




def adjust_length(name, length_limit):
    name_length = len(name)
    ret_name = name
    if name_length > length_limit:
        word_list = name.split()
        word_count = len(word_list)
        count = 1
        last_found = False
        delete_indexes = []
        for word in  word_list[::-1]:
            if last_found is False:
                if len(word) > 1:
                    last_word = ' '.join(word_list[-count:])
                    last_found = True
            else:
                delete_indexes.append(count)
                if name_length - (len(word) + 1) <= length_limit:
                    break
                name_length = name_length - (len(word) + 1)
                
            count += 1

        for index in delete_indexes:
            word_list[word_count-index] = ''
        word_list = [val for val in word_list if val]
        print(word_list)

        ret_name = ' '.join(word_list)

    return ret_name



def split_name(full_name):
    fname = ''
    lname = ''
    if full_name is not None and len(full_name.strip()) > 0:
        full_name = full_name.strip()
        words_list = full_name.split()

        if len(words_list) == 1:
            fname = words_list[0]
            lname = words_list[0]
        elif len(words_list) == 2:
            if len(words_list[0]) == 1:
                fname = words_list[1]
                lname = words_list[0]
            else:
                fname = words_list[0]
                lname = words_list[1]
        else:
            count = 1
            initials = []
            for word in words_list:    
                if len(word) == 1:
                    initials.append(word)
                else:
                    fname =  word
                    lname = ' '.join(words_list[count:] + initials)
                    break
                count += 1

    fname = adjust_length(fname, 20)
    lname = adjust_length(lname, 20)

    return fname , lname

def test_name_splitting():
    test_result = []
    for test_data in TEST_NAME_DATA:
        full_name = test_data[0]
        expected_fname = test_data[1]
        expected_lname = test_data[2]
        
        fname , lname = split_name(full_name)
        
        result = [full_name]
        result.append('pass' if(fname == expected_fname) else 'fail')
        result.append('pass' if(lname == expected_lname) else 'fail')
        result.append([fname, expected_fname])
        result.append([lname, expected_lname])

        test_result.append(result)
        print(result)

    


test_name_splitting()


