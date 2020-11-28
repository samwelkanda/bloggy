from selenium import webdriver

browser = webdriver.Firefox(executable_path='/home/kiptoo/.local/bin/geckodriver')

# Samwel has heard about a cool new blog. He goes to
# check out its homepage

browser.get('http://0.0.0:8000')

# He notices the page header and title mention blog application.

assert 'My Blog' in browser.title

# He finds an interesting post on python
# He click it right away and starts to read it
# He finds it interesting and decides to comment on how great
# the post is
# After liking the post so much he decides to share it with his
# friend Silas
# He checks out a recommended post on Django

browser.quit()