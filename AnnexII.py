###freq-degree & average connectivity
f1=open('18.interactome.txt')
num_inter=0
protein_kind=set()
allproteinlist=[]
numeinterlist=[]
for line in f1:
	num_inter+=1
	list_every_line=line.split(' ')
	protein_kind.add(list_every_line[0])
	allproteinlist.append(list_every_line[0])
num_inter=num_inter/2
protein_kind_list=list(protein_kind)

for protein1 in protein_kind_list:
	numeachinter=0
	for protein2 in allproteinlist:
		if protein1==protein2:
			numeachinter+=1
	numeinterlist.append(numeachinter)
num_protein=len(protein_kind)
average_connectivity=num_inter/num_protein
print ('Average connectivity in Synechocystis (species 18)=', average_connectivity)

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
