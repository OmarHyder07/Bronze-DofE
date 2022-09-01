def palindrome_checker(word):
    score = 0
    length = len(word)
    p = list(word)
    old_amount_of_times = (len(word) / 2)
    amount_of_times = int(old_amount_of_times)
    for x in range(int(amount_of_times)):
        length = len(word)
        if p[length-length+x] == p[length-1-x]: 
            score = score + 1
    if score == amount_of_times:
        palindrome = 1
        return palindrome 
    else:
        palindrome = 0
        return palindrome

def word_splitter(word):
    length = len(word)
    p = list(word)
    print(p)
    
    
test = input("type a word ")
word_splitter(test) 
palindrome = palindrome_checker(test) 
print(palindrome)
