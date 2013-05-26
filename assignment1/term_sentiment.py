import sys
import re
import json

def mkdict(sfile):
    #afinnfile = open("AFINN-111.txt")
    afinnfile = sfile
    global scores
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.



def hw(dict):
    #print 'Hello, world!'
    for key in dict:
        #avg = sum(dict[key])/float(len(dict[key]))
        avg = float(dict[key])
        print key, avg
        #print "Average is :", avg






def lines(fp):
    newwords ={}
    #print str(len(fp.readlines()))

    length = len(fp.readlines())
    fp.seek(0)
    #linestr = fp.readlines()
    
    #print linestr
    for i in range (1, length+1):
        linestr = fp.readline()
        j_linestr = json.loads(linestr)
        if "text" in j_linestr:
            line = j_linestr['text'].encode('utf-8') 
#            print line
            totalval = 0
            val = 0
            for wordl in line.split():
                wordl =wordl.lower()
                if wordl in scores:
                    val = scores[wordl]
                    totalval += val

#            for wordl in scores:
#                pattern = r'\b'+wordl+r'\b'
#                match = re.search(pattern,line.lower())
#                if match:
#                    val = scores[wordl]    
#                    totalval += val
            # following section iterates each word in line
            for wordn in line.split():
                #wordn = wordn.lower()
                #if wordn not in scores:
                newwords[wordn] = newwords.get(wordn,0)+totalval
#                    if wordn in newwords:
                        
#                        newwords[wordn].append(totalval)
#                    else:
#                        newwords[wordn]=[]
#                        newwords[wordn].append(totalval)
    return newwords



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    mkdict(sent_file)
    #lines(sent_file)
    nwords=lines(tweet_file)
    #print dict_words
    hw(nwords)
#    print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
#    print nwords["@JonasBrothers"]
#    print nwords["Kieran"]
if __name__ == '__main__':
    main()
