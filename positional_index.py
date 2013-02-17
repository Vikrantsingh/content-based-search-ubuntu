"""
	Creating a positional index	
"""


"""
Structure of positionalIndex

positionalIndex = {

				   term1 : [no_Of_Doc,{ 
				   						docID1:[ occurance, [ position1, postion2] ], 
				   						
				   						docID2:[ occurance, [ position1, postion2] ] 
				   					  } 
				   		   ], 

				   term2 : [no_Of_Doc,{ 
				   						docID1:[ occurance, [ position1, postion2] ], 
				   						
				   						docID2:[ occurance, [ position1, postion2] ] 
				   					  } 
				   		   ], 
				   
				  } 

"""


positionalIndex = {} #it is a dictionary with key as term and value as list of document

#------------------------------------

#function to add term in positional index
def addToIndex(positionalIndex,term,docID,Position):
	
	if term in positionalIndex.keys():
			if not docID in positionalIndex[term][1].keys():
				#if not present add entry of new docID
				positionalIndex[term][1][docID] = [0,[]] 
				#increment no_of_doc counter
				positionalIndex[term][0] += 1 
			#Append postion of term
			#positionalIndex[term][1][docID][1] += [Position]
			positionalIndex[term][1][docID][1] += [encode(positionalIndex,term,docID,Position)]
			#increment no_of_occurance counter
			positionalIndex[term][1][docID][0] += 1 
	else:
			#create a new entry for term
			positionalIndex[term] = [0,{}]
			#increment no_of_doc counter
			positionalIndex[term][0] += 1
			#initialize
			positionalIndex[term][1][docID] = [0,[]] 
			#set no_of_occurance counter and postion
			#positionalIndex[term][1][docID] = [1,[Position]]
			positionalIndex[term][1][docID] = [1,[encode(positionalIndex,term,docID,Position)]]

	return


#------------------------------------

def encode(positionalIndex,term,docID,position):
		
	if positionalIndex[term][1][docID][0] == 0 :
		#if first element then set d_flag same as position
		d_gap = position						
	else:
		#get d_gap of 
		predessorPostion = decode(positionalIndex,term,docID,positionalIndex[term][1][docID][0]) 
		#d_gap = position - positionalIndex[term][1][docID][1][predessorPostion-1]		
		d_gap = position - predessorPostion			
	return d_gap

def decode(positionalIndex,term,docID,arrayIndex):
	
	position = 0
	if arrayIndex==0 :
		position = positionalIndex[term][1][docID][1][0]			
	else:
		for i in range (arrayIndex):

			position += positionalIndex[term][1][docID][1][i]
				
	return position

#------------------------------------


#Read file names

doc={} #store document name
index = 0 #store number of documents
files = open('files.txt','r')
for afile in files:
	#print len(afile)
	doc[index]=afile[0:len(afile)-1]
	index += 1


#Parse file one by one tokenize and add to index

for index in doc.keys():

	wordsListTemp=[] #to store word from currently reading file
	helloFile = open(doc[index],'r');
	for line in helloFile:
		wordsListTemp += line.split(); 
	wordsListTempLength = len(wordsListTemp)
			
	for j in range(wordsListTempLength):
		word = wordsListTemp[j]
		#add to index send term,docID,position
		addToIndex(positionalIndex,word,index,j)
				
	print wordsListTemp

print '------------*---'

print positionalIndex

