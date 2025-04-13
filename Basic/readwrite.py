file = open('test.txt')

# read all contains of the file
#print(file.read())

#read n number of character by passing parameter
#print(file.read(4))
#print(file.read(5))

#print(file.readline())
#(file.readline())

# print line by line using readline()

#line = file.readline()
#while line !="":
 #   print(line)
  #  line = file.readline()

 # Is there another way



for line in file.readlines():
    print(line)

file.close()