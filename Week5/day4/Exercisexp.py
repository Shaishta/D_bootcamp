#Exercise 1 – Random Sentence Generator
import random
def get_word_from_file(file):
    with open(file, 'r') as f:
        sentence = f.readlines()
        return sentence

def get_random_sentence(length):
    words_list = get_word_from_file("sowpods.txt")
    words = []
    for x in range(length):
        x = random.choice(words_list)
        words.append(x[:-2])
        return "  ".join(words).lower()

def main():
    """this program will accept integer values between 2 and 20"""
    number_words = int(input("Please enter how long do you want your sentence to be(Please enter between 2 and 20):  "))
    try:
        if 2 <= number_words <= 20:
            return get_random_sentence(number_words)
        else:
            return 'Your number is not between 2 and 20'
    except:
        return'not a number'
print(main.__doc__)
print(main())

#Exercise 2: Working With JSON
#
# import json
# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payable":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
#
# sample_dict = json.loads(sampleJson)
# print(sample_dict["company"]["employee"]["payable"]["salary"])
# sample_dict["company"]["employee"]['birth_date'] = 2000/11/11
# print(sample_dict["company"]["employee"])
#
# sample_file = "samplefile.json"
# with open('sample_json','w') as f:
#     json.dump(sample_dict,f,indent=4)
#
#


