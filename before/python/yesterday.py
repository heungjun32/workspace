f = open("yesterday.txt", 'r')
yesterday_lyric = " "
while True:
        line = f.readline()
        if not line:
                break
        yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()  

yesterday = yesterday_lyric.count("yesterday")
Yesterday = yesterday_lyric.count("Yesterday")
print ("Number of a Word 'yesterday'", yesterday)
print ("Number of a Word 'Yesterday'", Yesterday)