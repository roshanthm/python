def sentence(stn):
    x=stn.split()
    freq={}
                                 # if word in freq:
                                      #freq[word] += 1
                                # else:
                                      # freq[word] = 1
    for i in x:
        freq[i]=freq.get(i,0)+1
    return freq


stn="welcome to the hello to the the"
print(sentence(stn))