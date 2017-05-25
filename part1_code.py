f1=open('interactome.all.txt')
o5=open('30.interactome.txt','w')
for line in f1:
	if line[0:4]=='4932':
		o5.write(line)
f1.close()
o5.close()

f2=open('08.interactome.txt')
index=0
for line in f2:
	index+=1	
	if index<20:
		print (line[0:16])

f2=open('08.interactome.txt')
for line in f2:
	if line[12:16]=='0002':
		print (line)
##line[12:16]=='0001' line[29:33]=='0002'

###freq-degree & average connectivity
f1=open('08.interactome.txt')
num_inter=0
protein_kind=set()
allproteinlist=[]
numeinterlist=[]
for line in f1:
	num_inter+=1
	list_every_line=line.split(' ')
	protein_kind.add(list_every_line[0])
	allproteinlist.append(list_every_line[0])
	#protein_kind.add(list_every_line[1])
num_inter=num_inter/2
protein_kind_list=list(protein_kind)
#print (protein_kind, allproteinlist)
for protein1 in protein_kind_list:
	numeachinter=0
	for protein2 in allproteinlist:
		if protein1==protein2:
			numeachinter+=1
	numeinterlist.append(numeachinter)
#print (numeinterlist)
num_protein=len(protein_kind)
average_connectivity=num_inter/num_protein
print ('Average connectivity in Saccharomyces cerevisiae (species 30)=', average_connectivity)

nodegree=set(numeinterlist)
nodegree=list(nodegree)
freq=[]
for i1 in nodegree:
	count=0
	for i2 in numeinterlist:
		if i2==i1:
			count+=1
	freq.append(count)
for i3 in freq:
	i3=i3/len(numeinterlist)
#print (nodegree)
#print (freq)
import numpy as np
import matplotlib.pyplot as plt
x=np.log10(nodegree,dtype='float64')
y=np.log10(freq,dtype='float64')
plt.scatter(x, y, color='orange')
plt.xlabel('k')
plt.ylabel('P(k)')
plt.title('Saccharomyces cerevisiae')
plt.show()

f1.close()
##Bacteroides thetaiotaomicron, Dictyoglomus turgidum, Escherichia coli, Synechocystis, Saccharomyces cerevisiae


###not working code......
f1=open('08.interactome.txt')
protein_kind_list=list(protein_kind)
numwithk=[]
internumlist=[]
for protein_name in protein_kind_list:
	#print (protein_name)
	#internum=0
	for line in f1:
		line=line.split(' ')
		#print (line[0])
		if line[0]==protein_name:
			print (line[0])
			#internum+=1
	#print (internum)
	internumlist.append(internum)
print (internumlist)
nodegree=set(internumlist)
nodegree=list(nodegree)
freq=[]
for i1 in nodegree:
	count=0
	for i2 in internumlist:
		if i2==i1:
			count+=1
	freq.append(count)
for i3 in freq:
	i3=i3/len(internumlist)
print (nodegree)
print (freq)
