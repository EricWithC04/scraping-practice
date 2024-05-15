from bs4 import BeautifulSoup as bs

contents = """
<html lang="en">
<head>
<title>Just testing</title>
</head>
<body>
. . .
</body>
<html>"""

soup = bs(contents, features="html.parser")

soup.find_all("elemento")
soup.find_all(["elemento1", "elemento2"])

classResults = soup.find_all(class_="clase a buscar")
nameResults =soup.find_all(name="username")

print(classResults)
print(nameResults)