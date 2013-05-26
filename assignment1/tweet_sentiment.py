import sys
import json
import re

def mkdict(sfile):
    #afinnfile = open("AFINN-111.txt")
    afinnfile = sfile
    global scores
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

   # print scores.items() # Print every (term, score) pair in the dictionary




def lines(fp):
    
    length = len(fp.readlines())
    fp.seek(0)
    #linestr = fp.readlines()
    
    #print linestr
    for i in range (1, length+1):
        #print "Loop %s" %(i)
        linestr = fp.readline()
        #print linestr
        #print type(linestr)
        j_linestr = json.loads(linestr)
        #print "j_linestr is type", type(j_linestr)
        #print "With keys:", j_linestr.keys()
        #print "*******************************************************"
        if "text" in j_linestr:
            line = j_linestr['text'].encode('utf-8') 
            #print "JSON:", line
            #print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            totalval = 0
            val = 0
            for wordl in scores:
                #print wordl
                pattern = r'\b'+wordl+r'\b'
                #pattern = wordl
                match = re.search(pattern,line.lower())
                #print pattern + "Match:"
                #print match
                #wordl = word.lower()
                if match:
                #if wordl in line:
                    #print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   M A T C H !!!!!!!"
                    val = scores[wordl]    
                    totalval = totalval+val
                    #print "WORD:", wordl, "VAL:", val
            print float(totalval)
#while linestr :   
       #tweets = json.load(linestr)
       #print linestr
       #print tweets["text"]
       #linestr = fp.readline()
    #print "*****finish loop******" 


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #saveout = sys.stdout # save the std output locn
    #fsock = open('ex2tmp.out','w')
    #sys.stdout = fsock

    mkdict(sent_file)
    #lines(sent_file)
    lines(tweet_file)
    #mkdict(sent_file)
    #sys.stdout = saveout #revert stdout
    #fsock.close()

if __name__ == '__main__':
    main()



