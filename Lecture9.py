#!/usr/bin/python3

#1.Program to take a DNA sequence and calculate A+T content
#Written by s1914244 on 23 Oct 2019
from __future__ import division
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
at_content = (a_count + t_count) / length
print("AT content is " + str(at_content))


#2.Program to take a DNA sequence and complement it
#Written by s1914244 on 23 Oct 2019
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replacement1=my_dna.replace("A","t")
print("The complement sequence is", my_dna.replace('A', 't').replace('T','a').replace('G','c').replace('C','g').upper())


#3.Program to take a DNA sequence cut by EcoRI and work out fragment sizes
my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
site="GAATTC"
print("Lengths of",site,"cleaved fragments are",(my_dna.find(site) + 1),"and",len(my_dna) -(my_dna.find(site)+1),"bases")

#4.Splicing out introns
my_dna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCT ATCATCGATCGATATCGATGCATCGACTACTAT"
# Remember that we start counting from zero. Positions are inclusive at the start and exclusive at the end
exon1=my_dna[0:63]
exon2=my_dna[90:]
print("###Exons joined###\n"+exon1+exon2)
# To calculate the coding percentage, we just have to take the length of the exons, divide by the length of the sequence, and multiply by 100
coding_length = len(exon1 + exon2)
total_length = len(my_dna)
print("### Coding percentage (rounded) ###\n" + str(int((coding_length / total_length) * 100)))


# To print out the upper/lower case version, we need to take the middle bit i.e. the intron and convert it to lower case, then join the bits back together
# We already specified the exons
exon1 = my_dna[0:63]
exon2 = my_dna[90:]
intron = my_dna[63:90]
print("### Exon intron exon ###\n" + exon1 + intron.lower() + exon2)




