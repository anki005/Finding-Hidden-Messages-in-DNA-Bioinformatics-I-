# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

Pattern = "CTTGATCAT"
file = open(r"C:\Users\ankit\Downloads\Vibrio_cholerae.txt")
Genome = file.readline()
r = PatternMatching(Pattern, Genome)

for i in r:
    print(i, end=" ")
