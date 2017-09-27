
from selenium import webdriver
browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
browser.get('http://localhost:800')
assert 'Django' in browser.title
