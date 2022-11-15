import re, json, treat_file

dictionary  = {}

def clean(line):
    return re.sub(r'\n', '', line.lower())

def get_dict():
    text = open('text.txt', 'r')
    for line in text.readlines():
        line = clean(line)
        try:
            index = dictionary[line[0]]
            try:
                index[line] += 1
            except:
                index[line] = 1
        except:
            dictionary.update(  {   line[0]: {line: 1}   }  )

    text.close()
    return dictionary

def get_list():
    listing     = []
    #text = open('text.txt', 'r')
    text = treat_file.get_list()
    for line in text:
        line = clean(line)
        for index in listing:
            if index[0] == line[0]:
                for array in index[1]:
                    if array[0] == line:
                        array[1] += 1
                        break
                else:
                    index[1].append([line, 1])
                break
        else:
            listing.append( [   line[0],   [ [line, 1] ]   ] )
    
    #text.close()
    return listing


def get_unordered_list():
    ordList     = [[],[]]
    text = open('text.txt', 'r')

    for line in text.readlines():
        line = clean(line)
        if len(ordList) > 0:
            if line in ordList[0]:
                ordList[1][ordList[0].index(line)] += 1
            else:
                ordList[0].append(line)
                ordList[1].append(1)
        else:
            ordList[0].append(line)
            ordList[1].append(1)
    
    text.close()
    return ordList

def get_ordered_list(orderBy = False, limit = 10, wordSizeMin = 0, index = 0):
    text = open('text.txt', 'r')
    listing = []
    ordList     = [[],[]]

    thisList = get_list()

    for order in thisList:
        for wordObj in order[1]:
            if len(wordObj[0]) > wordSizeMin:
                listing.append(wordObj)

    listing.sort(key=lambda i:i[index], reverse = orderBy)

    if limit > len(listing):
        limit = len(listing)

    listing = [listing[i] for i in range(limit)]

    for listItem in listing:
        ordList[0].append(listItem[0])
        ordList[1].append(listItem[1])

    text.close()
    return ordList

