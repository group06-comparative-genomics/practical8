import gzip
f=gzip.open('protein.links.v10.txt.gz','rb')
o=open('/home/u2209/Desktop/interactome.all.txt','wb')
for line in f:
	o.write(line)
f.close()
o.close()

f1=open('/home/u2209/Desktop/interactome.all.txt')
o1=open('03.interactome.txt','w')
o2=open('08.interactome.txt','w')
o3=open('09.interactome.txt','w')
o4=open('18.interactome.txt','w')
for line in f1:
	if line[0:6]=='226186':
		o1.write(line)
	if line[0:6]=='515635':
		o2.write(line)
	if line[0:4]=='1148':
		o4.write(line)
	if line[0:6]=='362663':
		o3.write(line)
f1.close()
o1.close()
o2.close()
o3.close()
o4.close()
