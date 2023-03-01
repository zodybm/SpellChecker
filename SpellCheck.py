def spellCheck(word) :
    file = open("english3.txt", "r")
    table = dict()
    while True :
        line = file.readline()
        hashed = hash(line)
        table.update({hashed : line})
        if not line:
            break
    wordHash = hash(word)
    if (table.get(wordHash)) :
        print(word)
        return
    
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    length = len(word)
    temp = word
    for i in range(length) :
        for j in range(len(chars)) :
            temp = temp.replace(temp[i], chars[j])
            rehash = hash(temp)
            if (table.get(rehash)) :
                print(temp)
            temp = word
        temp = word
            
        
spellCheck("suppey\n")