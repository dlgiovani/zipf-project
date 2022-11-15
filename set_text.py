import wikipedia

global content

def get_wiki(topic):
    global content
    p = wikipedia.page(topic)
    content = p.content.encode('utf-8')

def write_file(fileName):
    global content
    file = open(fileName + '.txt', 'wb')
    file.write(content)
    file.close()

def preview_text(size):
    global content
    return content[0:size]