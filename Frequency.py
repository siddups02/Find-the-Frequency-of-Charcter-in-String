# Consider we have a string with characters and we want the frequency of each characters in the string

str = 'sgerh45y4hdgfbds'

dict = {}  #Empty dictionary that will contain each key as character and then frequency as value for the Key 
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1 #if the key is already present add plus one to the value of the key
        else:
            dict[n] = 1  # if the key is not present create the key with value 1
            
print(dict)
