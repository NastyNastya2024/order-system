import requests

img ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtnvAOajH9gS4C30cRF7rD_voaTAKly2Ntaw&s"
response = requests.get(img)

img =response.content
with open("test2.jpg", "wb") as file:
    file.write(response.content)

