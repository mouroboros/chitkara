
from selenium import webdriver
import os, unittest

class NewVisitorTest (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test')

        #enter to do list straight away
        #she types "buy peacock feathers"
        #hit enter, page updates to show "buy peacock feathers"
        #still text box for new items
        #site has generated unique url
        #url has persistance
        #satisfied she goes to sleep

if __name__ == '__main__':
    unittest.main()
