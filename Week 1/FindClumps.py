
def FindClumps(Text, k, L, t):
    Pattern = []
    n = len(Text)
    for i in range(n-L+1):
        window = Text[i:i+L]
        freqMap = FrequencyTable(window, k)
        for key in freqMap:
            if freqMap[key] >= t:
                Pattern.append(key)
    Pattern = list(set(Pattern))
    return Pattern

def FrequencyTable(Text, k):
    freqMap = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freqMap[Pattern]=0
    for i in range(n-k+1):
        Pattern = Text[i:i+k]    
        freqMap[Pattern]= freqMap[Pattern]+1
    return freqMap


Text = "TGAGAGAAGTCCTTTACACCGTATCCGGCTAGGCATGTAGAGGCATGTAGGCAGGCATGTAGCATGTAGTAGCCAGGCATGTAGTGATATTTGGAAGCCATGCCGAGGCATGTAGGGACCCCGATTTAGCGTTGCACTTGACCTCAGGACCTAGTTTCTCAAGCTACATCACAACGCGTCGCGTCGCGTCCGGCTGACAACGCGTCGGCCGTACAACGCGTCCAACGCGTCATACAACGCGTCCCCAGAGCCCTTTAACGATAGTTAGCCTTTAACTAGTTCGGGACCCTTTAACGAACCTTTAACGACCTTTAACGATTAACTATAACTAGTTCAACTAGTTCTGGTGGTGGGTCCGAGGTGGGTCCGTGGGTCCGCCGACTCACCGACACCGATGTGGTGGGTCCGCGGGTGGGTCCGGCGACCCCGTGTCACCGACCGGTGTTTGTGGATACAAACAAAGGATGTCAGACCAACTAGTGCAAAGATATAGGGTGCAAGCAGTAGCGGTGATCGATGCGAGGTCTACGGCAAACTTTGACGTTTCGTGCAACAATGTATCTGTTTGTCATGACAGTCAATCTGTTCGCAGCAGTAGTGGGTTATTGGCTGGGGATGTCCCGGGGGGGGATCGACGCGGGGGGGGACGGGGGGGGAGGGAAGATTTCTGCCGAAGTTGCCTGTTCGGGGGGGGAATTGGCCTCGGGGGGGGAGTGTATGTGTCGCAGAGGCTCACCGATCGGTATTGGCATCGCTGTATGACGTAGTCGGGTAAACTAGTAAGTTAAACTAGTATAGTAAACTAGTAATAAACTAGTACATATATAAACTTAAACTAGTACTTCGTAACTAAACTAGTACTATCTTCATGCTACAAAGCTACTCTACTCAGAACTCTAGATCTTCGACCTGAGGGGCCAGAGGGTGTCGCAAGTTCAAAGCGGCAATGGGGCTTAGCCGTGTATCTCATCTCGTATCTCCGTGTATCCTAAGAAAACACGTGCTAAGAAAACCTCCGTGTATCTCTACAAGTGCCTAAGAAAACCTAAGAAAACAAAACCGAGCAGGTTTCTCTAAGAAAACCGGAGGATTCGTTTATGAAGGAATTATGAAGGCGCTTCCGCTTTGAAGACGCTTTGAAGGAAGGACTCGCTTTGAAGGGGCGCTTTGACGCTTTGAAGAGTAACAGGCACAGACTGCTTGATCTTTTCATAGTGTGGTAAATAATCTTGAGAACAAGAGCACTAGTCTTCTCAATCTAGACTGCTCCCGTTGTAGCTTTTGCAACCTCGTAAACCTCTTAGAGGCAACCTATGTCCTATCAATACTCGGTGATCATTGACCTCACAGGGAGTGATTGAAGCCCCAAGTAAGCGATGAAGCTGGTAATCTTTGAAGCCGCAGTACATAGCCGTGATACGCATTGATTCTGGCGCATCCGCTAGCGCTAGGACCGGCACATCCATCCGCTAGCCCAAAAGCCCCTGCAAGAGTCATCCGCCATCCGCTAGATCCGCTAGTTGTGATCCTCGTCTCACGATTCCACGAGGATAACGATTCCACCCACACCTTTCCGCTACAAACGATTCCACGACAAAAAAAACGATTCCACGTCCGACGATTCCACGGGTACGTACGAAGACGCTTTAAAAGATCGTTCGTACGTTCGGCGACCGGTTCCACTATGCAATCGTTCCACGGGTATGCAATCGCACTATGCAATCGCCACGTATGCAATCGGCTATGCAATCGCAGTTCACTTTATGCAATCGCGGCGACCTGGAGTTGTTACAAACAGGCGCGAACTTCGGCAATGTATATTAAATCGTAATCACGGGCTATAAGCGTAGCCTGTTACTCAGACTGTGGCACCCGCACTAACTGAACAAACACGAACGGTGTAGTAGAGCTTCAACCGTAGGAAAGAGTGTTCCATATATGGTCGCACTCTCCGAATTAAGCCAAAGCGGCCGCAAACTGACAACTGTAGACGGTACATT"
k = 10
L = 100
t = 4

ans = FindClumps(Text, k, L, t)
for i in ans:
    print(i, end=" ")

