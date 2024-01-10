def BetterFrequentWords(Text, k):
    # your code here
    FrequentPatterns = []
    freqMap = FrequencyTable(Text, k)
    max = MaxMap(freqMap)
    for key in freqMap:
        # add each key to words whose corresponding frequency value is equal to m
        if freqMap[key]==max:
            FrequentPatterns.append(key)
    return FrequentPatterns

def MaxMap(freqMap):
    return max(freqMap.values())

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

        
Text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
k = 3
r = BetterFrequentWords(Text, k)
for i in r:
    print(i,end=" ")