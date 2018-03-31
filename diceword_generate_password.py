from __future__ import print_function
import random
import argparse
wordlist_filename = 'wordlist.diceware.txt'
num_words = 6

#TODO change to using diceware8k.txt.  The FAQ says if you use a computer random number generator
#  (even though it advises not to), then to insure a uniform distribution of words, it is best 
#  to using a list of words that is a whole power of two in length.  That is why there is the
#  diceware8k list.

def GenerateDiceWord():
    '''Generates a password by choosing 6 words randomly from a list.
    The list has a number followed by the word.  The number is 5 digits where
    each digit is one of 1,2,3,4,5,6.  I will generate 5 random digits and 
    concatenate them together to form an index number and then choose the word
    which matches that index number.  Do this 6 times and I will have my 6 word 
    password.
    Look it up in Wikipedia to see why it is a strong passwd even though
    it is chosen from a dictionary list.'''
    global wordlist_filename
    global num_words
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Specify the filename of a wordlist in diceware format.  Uses {} by default.".format(wordlist_filename))
    parser.add_argument("-n", "--num_words", help="The number of words you would like in the produced password.  Defauult is {}".format(num_words), type=int)
    args = parser.parse_args()
    if args.filename:
        wordlist_filename = args.filename
    if args.num_words:
        num_words = args.num_words
    index_num = []
    password = []
    random.seed()
    for i in range(1092): #just me being paranoid
        x = random.randrange(0, 10)
    try:
        with open(wordlist_filename,'r') as f:
            wordlist = f.readlines()
    except:
        print("Could not open {}".format(wordlist_filename))
        return
    for j in range(num_words): #generate [6] words
        for i in range(5):  #need 5 digits to form an index for each word
            index_num.append(str(random.randrange(1,7)))
        index = ''.join(index_num)
        for line in wordlist:
            words = line.split()
            if words[0] >= index:
                password.append(words[1])
                break
        index_num = []
    return password

if __name__ == '__main__':
    print(GenerateDiceWord())
            
            
        
