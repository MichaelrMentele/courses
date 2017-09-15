from selenium import webdriver
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
        self.fail('finish the test!')

    # She is invited to enter a todo straight away
    # She types "buy peacock feathers into a text box
    # When she hits enter the page updates and the page lists
    # "1: Buy peacock feathers" as an item in a todo list
    # There is stall a text box inviting her to add more todos
    # She enters: "Use peacock feathers to make a fly"
    # The page updates again with the second item on the list
    # Edith wonders if the site will remember her list
    # She sees the site has generated a unique url for her, there is
    # explanatory text to that effect
    # she vists that URL and her todo list is still there
    # she goes to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
