import wikipediaapi
import re


def handle_ambiguity():
    # initialize a dictionary with options to go to
    where_to_go = {}
    current_category = ""

    # parse the ambiguity message for other options to go to
    category = False
    # iterate through lines of raw text
    for i in range(0, len(text_lines)):
        # there's an empty before a category, so we take it as an indicator of it
        if text_lines[i] == "":
            category = True
        elif category:
            # as we're inside of category we initialize the list that will be assigned to a where_to_go key
            current_category = text_lines[i]
            where_to_go[current_category] = []
            category = False
        elif current_category:
            # now we can append topics to current_category
            where_to_go[current_category].append(text_lines[i])

    # looping through a where_to_go dict to show all the topics
    # for key, definition in where_to_go.items():
    #     print(key)
    #     for item in definition:
    #         print(item)

    topics = [*where_to_go.values()]

    print(topics)

    # place for user input to handle the ambiguity and continue script's job with real wikipedia article
    user_decision = str(input("\nWhich one of these articles have you had in mind?\n"))

    type_of_def = {}

    for topic in topics:
        for article_name in topic:

            if article_name.find(user_decision) != -1:
                links_key, *explanation = article_name.split(re.findall(", a |, an |, the +", article_name)[0])

                return links_key

    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wiki_wiki = wikipediaapi.Wikipedia('en')

    query = str(input("Bring me the source article (either link or exact title):\n"))

    page_py = wiki_wiki.page(query)
    text_lines = page_py.text.splitlines()

    if f"may refer to:" in text_lines[0]:
        print("Ambiguous")
        query = handle_ambiguity()
        print(page_py.links)
        # print(query)
        print(page_py.links[query].text)




        # page_py = wiki_wiki.page(query)
        # print(page_py.text)
    else:
        print(page_py.text)

    # for line in page_py.__str__():






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
