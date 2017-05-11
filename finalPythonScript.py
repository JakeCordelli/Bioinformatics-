from sys import argv


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

transcribedSequence = ''
for char in sequence:
   if char == "A":
       transcribedSequence=transcribedSequence+'U'
   elif char == "T":
       transcribedSequence=transcribedSequence+'A'
       Type = "DNA"
   elif char == "C":
       transcribedSequence=transcribedSequence+'G'
   elif char == "G":
       transcribedSequence=transcribedSequence+'C'
   else:
       transcribedSequence=transcribedSequence+'-'

#Regular 5'-3' strand
print("The sequence as a string: ", sequence)



codontable = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
    'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
}

def translate_dna(sequence):
    aminoAcidList=[]
    for i in range (0, len(sequence), 3):
        cds = str(sequence[:i])

    for i in range(0,len(cds), 3 ):
        if cds[i:i+3] in codontable:
            aminoAcidList.append(codontable[cds[i:i+3]])

    str1 = ''.join(aminoAcidList)
    return (str1)

#List the amino acids produced given each readding frame:

#Frame 1
#ReadingFrame1 (5'-3' starting at 0)
frame1Transcribed=transcribedSequence
print("\n\nFrame 1 transcribed: \n5'-"+frame1Transcribed+"-3'")
aminoAcidsFrame1=translate_dna(frame1Transcribed)
print ('\nFrame 1 translated: \n', aminoAcidsFrame1, '\n')

#Frame 2
#ReadingFrame2 (5'-3' starting at 1)
frame2Transcribed=transcribedSequence[1::]
print("\n\nFrame 2 transcribed: \n5'-"+frame2Transcribed+"-3'")
aminoAcidsFrame2=translate_dna(frame2Transcribed)
print ('\nFrame 2 translated: \n', aminoAcidsFrame2, '\n')

#Frame 3
#ReadingFrame3 (5'-3' starting at 2)
frame3Transcribed=transcribedSequence[2::]
print("\n\nFrame 3 transcribed: \n5'-"+frame3Transcribed+"-3'")
aminoAcidsFrame3=translate_dna(frame3Transcribed)
print ('\nFrame 3 translated: \n', aminoAcidsFrame3, '\n')

#Reverse the sequence, store in reverseSequence
reverseSequence=transcribedSequence[::-1]

#Frame 4
#ReadingFrame4 (3'-5' starting at 0)
frame4Transcribed=reverseSequence
print("\n\nFrame 4 transcribed: \n3'-"+frame4Transcribed+"-5'")
aminoAcidsFrame4=translate_dna(frame4Transcribed)
print ('\nFrame 4 translated: \n', aminoAcidsFrame4, '\n')

#Frame 5
#ReadingFrame5 (3'-5' starting at 1)
frame5Transcribed=reverseSequence[1::]
print("\n\nFrame 5 transcribed: \n3'-"+frame5Transcribed+"-5'")
aminoAcidsFrame5=translate_dna(frame5Transcribed)
print ('\nFrame 5 translated: \n', aminoAcidsFrame5, '\n')


#Frame 6
#ReadingFrame6 (3'-5' starting at 2)
frame6Transcribed=reverseSequence[2::]
print("\n\nFrame 6 transcribed: \n3'-"+frame6Transcribed+"-5'")
aminoAcidsFrame6=translate_dna(frame6Transcribed)
print ('\nFrame 6 translated: \n', aminoAcidsFrame6, '\n')
