import random
wordlist_filename = 'wordlist.diceware.txt'


def GenerateDiceWord():
    '''Generates a password by choosing 6 words randomly from a list.
    The list has a number followed by the word.  The number is 5 digits where
    each digit is one of 1,2,3,4,5,6.  I will generate 5 random digits and 
    concatenate them together to form an index number and then choose the word
    which matches that index number.  Do this 6 times and I will have my 6 word 
    password.
    Look it up in Wikipedia to see why it is a strong passwd even though
    it is chosen from a dictionary list.'''
    index_num = []
    password = []
    random.seed()
    for i in range(1092): #just me being paranoid
        x = random.randrange(0, 10)
    with open(wordlist_filename,'r') as f:
        wordlist = f.readlines()
    for j in range(6): #generate 6 words
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
            
            
        
