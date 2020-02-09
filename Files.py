#read it
#Demonstrates reading from a text file.

print("opening and closing the file")
txtFile=open("text.txt","r")
txtFile.close()


print("\nReading characters from the file.")
txtFile=open("text.txt","r")
print(txtFile.read(1))
print(txtFile.read(5))
txtFile.close()

print("\nReading the entire file at once")
txtFile=open("text.txt","r")
wholeTxt=txtFile.read()
print(wholeTxt)
txtFile.close()


print("\nReading characters from a line")
txtFile=open("text.txt","r")
print(txtFile.readline(1))
print(txtFile.readline(5))
txtFile.close()


print("\nRead one line at a time")
txtFile=open("text.txt","r")
print(txtFile.readline())
print(txtFile.readline())
print(txtFile.readline())
txtFile.close()


print()
#reading the entire file into a list
txtFile=open("text.txt","r")
lines=txtFile.readlines()
#print list
print(lines)
#
print(len(lines))
for line in lines:
    print(line)
txtFile.close()

print()
#loop through the file line by line

txtFile=open("text.txt","r")
for line in txtFile:
    print(line)
txtFile.close()


# WRITE TO A TEXT FILE

#create a text file with write() method

txtFile=open("write.txt","w")
txtFile.write("line 1\n")
txtFile.write("This is line 2\n")
txtFile.write("This is line 3\n")
txtFile.close()


#writing a list of strings to a file
print()
txtFile=open("write.txt","w")
lines=["line 1\n",
       "this is line 2\n",
       "this is line 3"]






