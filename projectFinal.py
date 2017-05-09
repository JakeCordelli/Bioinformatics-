
#have the user specify the name of the file
print ("Enter the file path of the txt file: ")
filePath = str(input())
#Define the file and location

print (filePath)
file=open(filePath)


#read in a file and turn it into a formatted stirng
def readNFormat(file):
    file=file.read()
    file=file.upper()
    #handle = StringIO(file) 
    #file = SeqIO.parse(handle, "fasta")
    return file

#sequence stores the formatted refSeq file as a string of letters
sequence=readNFormat(file)


#Regular 5'-3' strand
print("The sequence as a string: ", sequence,"\n")

#ReadingFrame1 (5'-3' starting at 0)
print("The sequence starting at 0: 5'-"+sequence+"-3'")

#ReadingFrame2 (5'-3' starting at 1)
print("The sequence starting at 1: 5'-"+sequence[1::]+"-3'")

#ReadingFrame3 (5'-3' starting at 2)
print("The sequence starting at 2: 5'-"+sequence[2::]+"-3'")




#Reverse the sequence, store in reverseSequence
reverseSequence=sequence[::-1]

#ReadingFrame4 (3'-5' starting at 0)
print("The reverse sequence starting at 0: 3'-"+reverseSequence+"-5'")

#ReadingFrame5 (3'-5' starting at 1)
print("The reverse sequence starting at 1: 3'-"+reverseSequence[1::]+"-5'")

#ReadingFrame6 (3'-5' starting at 2)
print("The reverse sequence starting at 2: 3'-"+reverseSequence[2::]+"-5'")



#chunk the string into groups of 3
    
