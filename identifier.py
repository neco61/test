seq1 = input(str('sequentie 1: '))
seq2 = input(str('sequentie 2: '))

match = 0

if len(seq1) >= len(seq2):
    for i in range(0, len(seq2)):
        if seq2 [i] == seq1 [i]:
                match += 1

elif len(seq1) <= len(seq2):
    
    for i in range(0, len(seq1)):
        if seq1 [i] == seq2 [i]:
            match += 1
                

print(match, "nucleotiden komen overeen")

lengte1 = len(seq1)
lengte2 = len(seq2)

identity = (match / lengte1 *100)
print(identity, "% identic")
