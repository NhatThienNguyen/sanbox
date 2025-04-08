import wikipedia

page_title = input("Enter page title: ").strip()

while page_title !='':
    try:
        page =wikipedia.page(page_title)
        print(f"{page_title}")
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError:
