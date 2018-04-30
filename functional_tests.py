from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about cool new online todo app she goes to checck it out
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention todo lists
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a todo straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # She types "buy peacock feathers into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter the page updates and the page lists
        # "1: Buy peacock feathers" as an item in a todo list
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url

        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('2: Use peacock feathers to make')
        self.check_for_row_in_list_table('1: By peacock feathers')

        # Now a new user, Francis comes along to the site
        # we use a new browser session to make sure he can't see Edith's
        # information from her cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Edith's list
        self.browser.get(self.live_server_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item, he is less
        # interesting than Edith
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unique url
        francis_list_url = self.browser.current_url

        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)

        # satisfied they both go to sleep

        # There is stall a text box inviting her to add more todos
        # She e nters: "Use peacock feathers to make a fly"
        self.fail('Finish the test!')

        # The page updates again with the second item on the list
        # Edith wonders if the site will remember her list
        # She sees the site has generated a unique url for her, there is
        # explanatory text to that effect
        # she vists that URL and her todo list is still there
        # she goes to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
