#Matrix
#Matrix
# matrix=  [
#     ['7','i','3'],
#     ['T','s','i'],
#     ['h','%','x'],
#     ['i',' ','#'],
#     ['s','M',' '],
#     ['$','a',' '],
#     ['#','t','%'],
#     ['^','r','!']]
# def matrix_decode(matrix):
#     data = []
#     data2 = []
#     data3 = []
#     for i in matrix:
#         if i[0].isalpha():
#             data.append(i[0][0])
#         if i[1].isalpha():
#             data2.append(i[1][0])
#         if ' ' in i[1]:
#             data2.append(' ')
#         if i[2].isalpha():
#             data3.append(i[2][0])
#     str1 = ' '.join(data)
#     str2 = ' '.join(data2)
#     str3 = ' '.join(data3)
#
#     print(str1, '', str2, str3)
# matrix_decode(matrix)

# #corrected#
# import string
# alphabet_lower = list(string.ascii_lowercase)
# alphabet_upper = list(string.ascii_uppercase)
# matrix = [
#     ['7', 'i', '3'],
#     ['T', 's', 'i'],
#     ['h', '%', 'x'],
#     ['i', ' ', '#'],
#     ['s', 'M', ' '],
#     ['$', 'a', ' '],
#     ['#', 't', '%'],
#     ['^', 'r', '!']]


# def decodematrix(matrix, items_per_list):
#     decoded_words = ''
#     i = 0
#     while i < items_per_list:
#         for char in matrix:
#             try:
#                 if char[i] in alphabet_lower or char[i] in alphabet_upper:
#                     decoded_words += char[i]
#                 else:
#                     if decoded_words[-1] == ' ' or char[i] == ' ':
#                         pass
#                     elif type(char[i]) is int:
#                         pass
#                     else:
#                         decoded_words += ' '
#             except:
#                     pass
#         i += 1
#     return decoded_words
# print(decodematrix(matrix, 3))
