f1=open('08.interactome.txt')
num_inter=0
protein_kind=set()
for line in f1:
	num_inter+=1
	list_every_line=line.split(' ')
	protein_kind.add(list_every_line[0])
	protein_kind.add(list_every_line[1])
num_inter=num_inter
num_protein=len(protein_kind)
average_connectivity=num_inter/num_protein
print ('Average connectivity in Synechocystis (species 18)=', average_connectivity)
f1.close()
protein_kind_list=list(protein_kind)
numwithk=[]
internumlist=[]
for protein_name in protein_kind_list:
	internum=0
	for line in f1:
		if line[0:16]==protein_name:
			internum+=1
	internumlist.append(internum)
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
