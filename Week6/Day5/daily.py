# import requests
# import json
# import psycopg2
# import random
#
#
# def get_country(n):
#     url = 'https://restcountries.com/v3.1/all'
#     data = requests.get(url)
#     data = data.json()
#     # countries=[(data)['name']['official'],(data)['flag'],(data)['subregion'],(data)['population']]
#
#     conn_string = "host='localhost' dbname='countries' user= 'postgres' password='5427'"
#     connection = psycopg2.connect(conn_string)
#     cursor = connection.cursor()
#     for i in range(n):
#         print(i + 1)
#         countries = random.choice(data)
#         # countries = countries.replace("'", " ")
#         query = f'''INSERT INTO countries (name,capital,flag,subregion,population) VALUES ('{countries['name']['official'].replace("'", " ")}','{countries['capital'][0].replace("'", " ")}','{countries['flag'].replace("'", " ")}','{countries['subregion'].replace("'", " ")}',{countries['population']});'''
#         query_result = cursor.execute(query)  # Cursor runs the query
#     connection.commit()
#     connection.close()  # Close the connection
#
#
# get_country(11)

