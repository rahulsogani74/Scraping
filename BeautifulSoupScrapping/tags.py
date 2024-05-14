import requests
from bs4 import BeautifulSoup

# Read the HTML file
with open("sample.html", "r") as f:
    html_doc = f.read()
    
# Create a BeautifulSoup object
soup = BeautifulSoup(html_doc, 'html.parser')

# Printing the prettified HTML content
print(soup.prettify())

# Accessing the title of the HTML document
print(soup.title)

# Accessing the string inside the title tag
print(soup.title.string)

# Accessing the first div element
print(soup.div)
print("")

# Finding all div elements in the HTML document
print(soup.find_all("div"))

# Printing href attribute and text of all 'a' elements
for link in soup.find_all("a"):
    print(link.get("href"))
    print(link.get_text())
    
# Finding an element by its id
print(soup.find(id="link3"))

# Selecting all div elements with class "italic"
print(soup.select("div.italic"))

# Selecting the span element with id "italic"
print(soup.select("span#italic"))

# Accessing the class attribute of the span element
print(soup.span.get("class"))

# Finding an element by its id
print(soup.find(id="italic"))

# Finding all elements with class "italic"
print(soup.find_all(class_="italic"))

# Printing children of the div with class "container"
for child in soup.find(class_="container").children:
    print(child)
    
# Printing parent elements of the element with class "box"
for parent in soup.find(class_="box").parents:
    print(parent)
    break

# Modifying attributes and content of the element with class "container"
cont = soup.find(class_="container")
cont.name = "span"
cont["class"] = "myClass class2"
cont.string = "I am a Student"
print(cont)

# Creating new 'ul', 'li' tags and inserting them into the HTML document
ulTag = soup.new_tag("ul")

liTag = soup.new_tag("li")
liTag.string = "Home"
ulTag.append(liTag)

liTag = soup.new_tag("li")
liTag.string = "About"
ulTag.append(liTag)

liTag = soup.new_tag("li")
liTag.string = "Login"
ulTag.append(liTag)


soup.html.body.insert(0, ulTag)

# Writing modified HTML content to a new file
with open("modified.html", "w") as f:
    f.write(str(soup))

# Checking if the element with class "container" has id and class attributes
cont = soup.find(class_="container")
print(cont.has_attr("id"))
print(cont.has_attr("class"))

# Custom functions for filtering elements based on attributes
def has_class_but_not_id(tag):
    return not tag.has_attr("class") and not tag.has_attr("id")


def has_content(tag):
    return tag.has_attr("content")


# Finding elements using custom functions
results = soup.find_all(has_class_but_not_id)

for result in results:
    print(result, "\n\n")


results = soup.find_all(has_content)

for result in results:
    print(result, "\n\n")