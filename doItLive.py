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
print("Transcribed Sequence: ", transcribedSequence,"\n")

#ReadingFrame1 (5'-3' starting at 0)
frame1Transcribed=transcribedSequence
print("The sequence transcribed at 0: 5'-"+frame1Transcribed+"-3'")

#ReadingFrame2 (5'-3' starting at 1)
frame2Transcribed=transcribedSequence[1::]
print("The sequence transcribed at 1: 5'-"+frame2Transcribed+"-3'")

#ReadingFrame3 (5'-3' starting at 2)
frame3Transcribed=transcribedSequence[2::]
print("The sequence transcribed at 2: 5'-"+frame3Transcribed+"-3'")




#Reverse the sequence, store in reverseSequence
reverseSequence=transcribedSequence[::-1]

#ReadingFrame4 (3'-5' starting at 0)
frame4Transcribed=reverseSequence
print("The reverse sequence transcribed at 0: 3'-"+frame4Transcribed+"-5'")

#ReadingFrame5 (3'-5' starting at 1)
frame5Transcribed=reverseSequence[1::]
print("The reverse sequence transcribed at 1: 3'-"+frame5Transcribed+"-5'")

#ReadingFrame6 (3'-5' starting at 2)
frame6Transcribed=reverseSequence[2::]
print("The reverse sequence transcribed at 2: 3'-"+frame6Transcribed+"-5'")

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
    proteinsequence = ''
    cds = str(sequence[:3])
    for n in range(0,len(cds),3):
        if cds[n:n+3] in codontable:
            proteinsequence = proteinsequence+codontable[cds[n:n+3]]
            return proteinsequence


#List the amino acids produced given each readding frame:
#Frame 1
aminoAcidsFrame1=translate_dna(frame1Transcribed)
print ('Amino Acids produced at frame 1: ', aminoAcidsFrame1)

#Frame 2
aminoAcidsFrame2=translate_dna(frame2Transcribed)
print ('Amino Acids produced at frame 2: ', aminoAcidsFrame2)

#Frame 3
aminoAcidsFrame3=translate_dna(frame3Transcribed)
print ('Amino Acids produced at frame 3: ', aminoAcidsFrame3)

#Frame 4
aminoAcidsFrame4=translate_dna(frame4Transcribed)
print ('Amino Acids produced at frame 4: ', aminoAcidsFrame4)

#Frame 5
aminoAcidsFrame5=translate_dna(frame5Transcribed)
print ('Amino Acids produced at frame 5: ', aminoAcidsFrame5)

#Frame 6
aminoAcidsFrame6=translate_dna(frame6Transcribed)
print ('Amino Acids produced at frame 6: ', aminoAcidsFrame6)



#chunk the string into groups of 3
  

