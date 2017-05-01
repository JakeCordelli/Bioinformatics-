#Jake Cordelli
#Bioinformatics: Project 2

#prompt the user to enter in a DNA sequence
print ("Enter a genetic sequence (DNA): ")
sequence = str(raw_input())
sequence=sequence.upper()



#If character is invalid, create a prompt for it
tainted = None
clean = None
taintedSequence=sequence

for ch in sequence:
    if ch != 'A' and ch != 'T' and ch != 'C' and ch!= 'G':
        taintedSequence=taintedSequence.replace(ch, '-')
        tainted=True          
    else:
        tainted=False
        clean=True

            
if tainted :
    clean=False
    print("There is/are impurities in the sequence!")
    print "The length of the tainted sequence is: " ,len(taintedSequence)
    print("The tainted sequence is: 5'-"+taintedSequence+"-3'")
    print("The reverse: 3'-"+taintedSequence[::-1]+"-5'")

    #Finding the complement
    taintedComplement = ""
    for i in range(0, len(taintedSequence)):
        if taintedSequence[i] == "T":
            taintedComplement += "A"

        if taintedSequence[i] == "A":
            taintedComplement += "T"

        if taintedSequence[i] == "G":
            taintedComplement += "C"

        if taintedSequence[i] == "C":
            taintedComplement += "G"

        if taintedSequence[i]=="-":
            taintedComplement += "-"

    print ("The complement sequence: 5'-"+taintedComplement+"-3'")
    print ("The reverse complement: 3'-"+taintedComplement[::-1]+"-5'")
 

if clean :
    tainted=False
    print("There are no impurities in the sequence")
    print "The length of the sequence is:" ,len(sequence)
    print("The valid sequence you entered is: 5'-"+sequence+"-3'")
    print("The reverse: 3'-"+sequence[::-1]+"-5'")

    #Finding the complement
    complement = ""
    for i in range(0, len(sequence)):
        if sequence[i] == "T":
            complement += "A"

        if sequence[i] == "A":
            complement += "T"

        if sequence[i] == "G":
            complement += "C"

        if sequence[i] == "C":
            complement += "G"
            
    print ("The complement sequence: 5'-"+complement+"-3'")
    print ("The reverse complement: 3'-"+complement[::-1]+"-5'")



#Part D: Taking in an RNA sequence
#prompt the user to enter in an RNA sequence
    print
print ("Enter a genetic sequence (RNA): ")
RNASequence = str(raw_input())
RNASequence=RNASequence.upper()
cleanRNA=None
RNAtainted=None
taintedRNASequence=None
for ch in RNASequence:
    if ch != 'A' and ch != 'U' and ch != 'C' and ch!= 'G':
        taintedRNASequence=taintedRNASequence.replace(ch, '-')
        RNAtainted=True        
    else:
        cleanRNA=True



if RNAtainted :
    clean=False
    print("There is/are impurities in the sequence!")
    print "The length of the tainted sequence is: " ,len(taintedRNASequence)
    print("The tainted sequence is: 5'-"+taintedRNASequence+"-3'")
    print("The reverse: 3'-"+taintedRNASequence[::-1]+"-5'")

    #Finding the complement
    taintedComplement = ""
    for i in range(0, len(taintedRNASequence)):
        if taintedRNASequence[i] == "U":
            taintedRNAComplement += "A"

        if taintedRNASequence[i] == "A":
            taintedRNAComplement += "U"

        if taintedRNASequence[i] == "G":
            taintedRNAComplement += "C"

        if taintedRNASequence[i] == "C":
            taintedRNAComplement += "G"

        if taintedRNASequence[i]=="-":
            taintedRNAComplement += "-"

    print ("The complement sequence: 5'-"+taintedRNAComplement+"-3'")
    print ("The reverse complement: 3'-"+taintedRNAComplement[::-1]+"-5'")

if cleanRNA :
    RNAtainted=False
    print("There are no impurities in the sequence")
    print "The length of the sequence is:" ,len(RNASequence)
    print("The valid sequence you entered is: 5'-"+RNASequence+"-3'")
    print("The reverse: 3'-"+RNASequence[::-1]+"-5'")

    #Finding the complement
    RNAcomplement = ""
    for i in range(0, len(RNASequence)):
        if RNASequence[i] == "U":
            RNAcomplement += "A"

        if RNASequence[i] == "A":
            RNAcomplement += "U"

        if RNASequence[i] == "G":
            RNAcomplement += "C"

        if RNASequence[i] == "C":
            RNAcomplement += "G"
            
    print ("The complement sequence: 5'-"+RNAcomplement+"-3'")
    print ("The reverse complement: 3'-"+RNAcomplement[::-1]+"-5'")
    

