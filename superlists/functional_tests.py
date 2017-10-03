
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, unittest

class NewVisitorTest (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        #enter to do list straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do list'
            )
        #she types "buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')
        #when she hits enter the page updates and now the page lists
        # '1: Buy peacock feathers'
        
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows
                ))
        
        #there is still a text box for new items
        self.fail('Finish the test!')
        #site has generated unique url
        #url has persistance
        #satisfied she goes to sleep

if __name__ == '__main__':
    unittest.main()
