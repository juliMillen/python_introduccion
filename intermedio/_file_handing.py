## File Handling ##

# .txt file

txt_file = open("intermedio/my_file.txt","r+") # Leer y Escribir
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)

#txt_file.write("\nSoy de hincha de Velez")
print(txt_file.readline())

txt_file.close()

## .json file

import json 

json_file = open("intermedio/my_file.json","w+")
json_test =  {
    "name":"Julian"
              ,"surname":"Millen"
              ,"age":24,
              "language":"Python"}

json.dump(json_test,json_file, indent = 4)

json_file.close()

with open("intermedio/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


json_dict = json.load(open("intermedio/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict['name'])


# .csv file
import csv
csv_file = open("intermedio/my_file.csv","w+")

json_test =  {
    "name":"Julian"
              ,"surname":"Millen"
              ,"age":24,
              "language":"Python"}

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","age","language"])
csv_writer.writerow(["Julian","Millen","24","Python"])

json_file.close()

# xlsx file para utilizarlo debe instalarse el modulo

# .xml file
#import xml
