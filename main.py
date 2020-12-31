#DNA testing file
from pathlib import Path
from bio_structs import RNA_Codons
import itertools
import string

dna_str = Path('/Users/rana/PycharmProjects/DNASeq/input_seq.txt').read_text()
dna_str = dna_str.replace('\n', '')
rna_str = dna_str.translate(str.maketrans("ATCG", "AUCG"))

if "AUG" in rna_str:
    prot_start = rna_str.find("AUG")

    # Translation to aminoacids
    protty_prot = [RNA_Codons[rna_str[pos:pos + 3]] for pos in range(prot_start, len(rna_str) - 2, 3)]

true_prot = Path('/Users/rana/PycharmProjects/DNASeq/translation.txt').read_text()
true_prot = true_prot.replace('\n', '')

# Convert protty_prot to string
protty_str = ''.join(map(str, protty_prot))

# Read APOE e4 gene
apoe4 = []
with open('/Users/rana/PycharmProjects/DNASeq/test.txt', 'r') as f:
    for line in itertools.islice(f, 25, 42):
        apoe4.append(line)
apoe4_str = ''.join(map(str, apoe4))
apoe4_str = apoe4_str.replace('\n', '')

# Read APOE e4 gene
apoe2 = []
with open('/Users/rana/PycharmProjects/DNASeq/test.txt', 'r') as f:
    for line in itertools.islice(f, 68, 85):
        apoe2.append(line)
apoe2_str = ''.join(map(str, apoe2))
apoe2_str = apoe2_str.replace('\n', '')

# Read APOE e3 gene
apoe3 = []
with open('/Users/rana/PycharmProjects/DNASeq/test.txt', 'r') as f:
    for line in itertools.islice(f, 47, 63):
        apoe3.append(line)
apoe3_str = ''.join(map(str, apoe3))
apoe3_str = apoe3_str.replace('\n', '')

if apoe2_str in dna_str:
    print("You have the APOE e2 gene.")
    if dna_str.count(apoe2_str) == 2:
        print("You have two APOE e2 genes, the risk of AD is much lower than an average person.")
elif apoe4_str in dna_str:
    print("You have the APOE e4 gene.")
    if dna_str.count(apoe4_str) == 2:
        print("You have 2 APOE e4 genes. The risk of AD is about 5-10 times higher than an average person")
    elif apoe2_str in dna_str:
        print("You have APOE e2 as well, the risk of AD is about 5x higher than an average person")
elif apoe3_str in dna_str:
    print("You have the APOE e3 gene.")
    if dna_str.count(apoe3_str) == 2:
        print("You are an average person. The risk of AD in later ages is neither high nor low.")
    elif apoe4_str in dna_str:
        print("You have the APOE e4 gene as well, your risk of getting AD is about 5x higher than a APOE e3/3 person.")
    elif apoe2_str in dna_str:
        print("You have the APOE e2 gene as well, your risk of getting AD is fairly low.")