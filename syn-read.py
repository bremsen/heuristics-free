
import numpy as np
import random as rn

#Generates a random sequence
L = 1000 #length of genome
basis = ['A','G','C','T']
seq = np.random.choice(basis,L)

#Generates k-mers (fixed k) that are randomly sampled from sequence
samples = 100000
read_len = 150
hv = range(300,310,1)

f = open('reads.fasta','w')

for i in range(0,samples):
    k=rn.randint(0,L-read_len)
    temp = seq[hv]
    seq[hv] = np.random.choice(basis,len(hv))
    f.write(">seq%d \n %s \n" % (i, ''.join(seq[k:k+read_len])))
    seq[hv] = temp
f.close()

#write original sequence to file
f = open('seq.txt','w') #open a text file called seq.txt
seqstr = ''.join(seq)
f.write(seqstr)
f.close()
print("Length of sequence: %d" % len(seqstr))
f.close()

