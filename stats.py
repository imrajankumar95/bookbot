def word_count(text):
    num_of_words = len(text.split())
    #print(f"Found {num_of_words} total words")
    #print(num_of_words)
    return num_of_words

def char_count(text):
    lower_case_char = text.lower()
    char_dict = {}
    for char in lower_case_char:
        if char in char_dict:
            char_dict[char] += 1
            #print(char_dict)
        else:
            char_dict[char] = 1       
    return char_dict

def sort_on(dict_items):
    return dict_items["num"]

def sort_dict(dict):
    sort_list = []
    
    for item in dict.items():
        hlp_dict = {}
        hlp_dict["char"] = item[0]
        hlp_dict["num"] = item[1]
        sort_list.append(hlp_dict)
    
    sort_list.sort(reverse=True, key=sort_on)
    #print(sort_list)
    return sort_list

        
    
#sort_dict({"d":4, "z": 10})        
        
    
        


#print(f"{char_count("aaaaabbbbcccdde")}")