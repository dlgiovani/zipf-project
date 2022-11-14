import re


def get_list():
    file = open('text.txt', 'r')

    cleanFile = re.sub(     '[^a-z\n-]',  '\n',     file.read().lower())

    cleanFile = cleanFile.replace('\n', ',')

    array = []
    array = cleanFile.split(',')
    while True:
        try:
            array.remove('')
        except:
            break
    
    file.close()
    return array