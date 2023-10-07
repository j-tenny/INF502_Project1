import random

def generate(len):
    bases = ['A', 'G', 'T', 'C']
    sequence = ''.join(random.choice(bases) for _ in range(len))
    return sequence

def save_seq(sequence, filename):
    with open(filename, 'w') as file:
        file.write(sequence)


len = int(input("Enter the length of the DNA sequences: "))

seq1 = generate(len)
seq2 = generate(len)

file1 = "sequence1.txt"
file2 = "sequence2.txt"

save_seq(seq1, file1)
save_seq(seq2, file2)

print("The DNA sequences have been generated and saved into the text files.")