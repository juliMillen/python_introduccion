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

