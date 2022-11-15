import set_text as wiki
import graph_tool

def get_boolean_user_choice(dialog):
    userInput = input(dialog)
    if userInput.lower() in ('yes', 'y', 'sim', 's', 't', '1', 'true'):
        return True
    else:
        return False

def main():
    if get_boolean_user_choice('Do you wish to inform a new topic?\n'):
        topic = input('Topic: ')
        wiki.get_wiki(topic)

        if get_boolean_user_choice('Do you wish to preview the file?\n'):
            print(wiki.preview_text(500))

        if get_boolean_user_choice('Do you wish to save the file?\n'):
            wiki.write_file('text')
    
    if get_boolean_user_choice('View chart?\n'):
        graph_tool.graph_default()

main()
