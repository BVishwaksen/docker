import os
import socket
IPAddr=socket.gethostbyname(socket.gethostname())
num_of_words = 0
word_dict = {}
file_words = {}
dirPath = '/home/data/'
resDir = '/home/output/'
fileList = os.listdir(dirPath)
textFiles = []
for f in fileList:
    if f.endswith(".txt"):
        textFiles.append(f)
for textFile in ['IF.txt','Limerick.txt']:
    temp = open(dirPath+textFile,"r")
    content = temp.read()
    words_in_file = content.split()
    file_words[textFile] = len(words_in_file)
    num_of_words = num_of_words + len(words_in_file)
    temp.close()
if_file = open(dirPath+'IF.txt',"r")
if_file_content = if_file.read()
words_in_if_file = if_file_content.split()
for if_word in words_in_if_file:
    if if_word in word_dict:
        word_dict[if_word] = word_dict[if_word] + 1
    else:
        word_dict[if_word] = 1
sorted_words = dict(sorted(word_dict.items(), key=lambda item: item[1],reverse=True))

res_file = open(resDir+'result.txt','w')
res_file.write("\n")
res_file.write("List of all text files in the given directory are "+",".join(textFiles)+"\n")
res_file.write("\n")
res_file.write("Total number of words in IF.txt "+str(file_words['IF.txt'])+"\n")
res_file.write("\n")
res_file.write("Total number of words in Limerick.txt "+str(file_words['Limerick.txt'])+"\n")
res_file.write("\n")
res_file.write("Grand Total of the words in IF.txt and Limeric.txt is "+str(num_of_words)+"\n")
res_file.write("\n")
res_file.write("Top Three words in IF.txt are "+"\n")
for i in range(0,3):
    res_file.write(list(sorted_words)[i]+" with count "+str(list(sorted_words.values())[i])+"\n")
res_file.write("\n")
res_file.write("IP Address of my machine is "+str(IPAddr)+"\n")
res_file.write("\n")
res_file.close()

res = open(resDir+'result.txt','r')
res_data = res.read()
print(res_data)