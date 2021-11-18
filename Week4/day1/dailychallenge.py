#Build Up A String
string = input("Enter a String: ")
if len(string) < 10:
    print("string not long enough")
elif len(string) > 10:
    print("string too long")
else:
    print(f"{string[0]} \n{string[-1]}")
    # print(string[0] + string[len(string)-1])
    result = ""
    for c in string:
        result += c
        print(result)

import random

str_list = list(result)

random.shuffle(str_list)

''.join(str_list)
