import re


def get_list():
    file = open('text.txt', 'r', encoding='utf-8')

    cleanFile = re.sub(     "[^a-z'\n-]",  '\n',     file.read().lower())

    cleanFile = cleanFile.replace('\n', ',')
    cleanFile = cleanFile.replace(' ', '')

    array = []
    array = cleanFile.split(',')
    while True:
        try:
            array.remove('')
        except:
            break
    
    file.close()
    return array