import urllib

def check_profanity(word):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+word)
    output = connection.read()
    connection.close()
    return output

print check_profanity("sh0t")