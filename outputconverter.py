#Author: Erfan Hosseini

import utm

v = []
v_conv = []
e = []
it = 0
temp = []
tempf = []
with open("data_uic_edges.txt", 'r') as f1:
	print("reading the file")
	a = f1.readlines()
	a = [elm for elm in a if elm != "\n"]
	for line in a:
		if line not in v:
			v.insert(it,line)
			it += 1
f1.close()
print("converting")
for i in range(it):
	temp = v[i][:-1].split(",")
	tempf.append(float(temp[1]))
	tempf.append(float(temp[0]))
	v_conv.insert(i,str(utm.from_latlon(tempf[0],tempf[1])[0]) + "," + str(utm.from_latlon(tempf[0],tempf[1])[1]) + "\n")
	tempf = []

with open("chicago_vertices.txt", 'a') as f2:
	print("writing the vertices")
	for i in range(it):
		f2.write(str(i+1)+","+v_conv[i])
f2.close()
for j in range(len(a)//2):
	e.insert(j,str(v.index(a[(2*j)])+1)+","+str(v.index(a[(2*j)+1])+1)+"\n")
with open("chicago_edges.txt", 'a') as f3:
	print("writing the edges")
	for k in range(len(e)):
		f3.write(str(k+1) + "," + e[k])
f3.close()
