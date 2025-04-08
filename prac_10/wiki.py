import wikipedia

page_title = input("Enter page title: ")

while page_title !='':
    try:
        page =wikipedia.page(page_title)
        print(f"{page_title}")
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"We need a more specific title. Try one of the following, or a new search: ")
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f"Page id {page_title} does not match any pages. Try another id!")
    page_title = input("Enter page title: ")
print("Thank you")