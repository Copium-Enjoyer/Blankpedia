from bs4 import BeautifulSoup
import wikipediaapi
import requests

# source = requests.get("https://en.wikipedia.org/wiki/Special:Random")
# soup = BeautifulSoup(source.text, 'html.parser')


def handle_ambiguity():
    where_to_go = {}
    current_category = ""

    category = False
    for i in range(0, len(text_lines)):
        if text_lines[i] == "":
            category = True
            continue

        if category:
            current_category = text_lines[i]
            where_to_go[current_category] = []
            category = False
            continue

        if current_category:
            where_to_go[current_category].append(text_lines[i])

    print(where_to_go)

    for key, definition in where_to_go.items():
        print(key)
        for item in definition:
            print(item)

    user_decision = str(input("Which one of these articles have you had in mind?\n"))

    topics = [*where_to_go.values()]

    # print([*where_to_go.values()])

    for topic in topics:
        if user_decision in topic:
            return user_decision

    return None



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wiki_wiki = wikipediaapi.Wikipedia('en')

    query = "React"

    # wiki_wiki.page()
    page_py = wiki_wiki.page(query)
    # print(page_py.text.splitlines())

    text_lines = page_py.text.splitlines()

    if f"{query} may refer to:" in text_lines[0]:
        print("Ambiguous")
        print(handle_ambiguity())

        # page_py = wiki_wiki.page(query)
        # print(page_py.text)
    else:
        print(page_py.text)

    # for line in page_py.__str__():






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
