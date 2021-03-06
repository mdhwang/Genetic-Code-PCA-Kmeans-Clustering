from itertools import permutations 

def CalcFreq(sequence,n,width):
    '''
    Takes in genome sequence and splits into lengths of width and creates frequency
    table of words  of length n
    '''
    print("Cutting into fragments of length {} and word length {}.".format(width,n))
    
    # Initialize Dictionary
    perm = permutations(['a','t','g','c']*4,n)
    words = {}
    for each in perm:
        name = ""
        for letter in each:
            name += letter
        words[name] = 0
    
    master = []
    for i in range(int(len(sequence)/width)):
        start = i*300
        end = start + 300
        chunk = sequence[start:end]
        blank = words.copy()
        for x in range(int(len(chunk)/n)):
            c_start = x*n
            c_end = c_start+n
            w = chunk[c_start:c_end]
            blank[w] += 1
        master.append(blank)
    
    return master