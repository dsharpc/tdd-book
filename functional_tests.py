from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # User opens site on their browser
        self.browser.get('http://localhost:8000')

        # The browser should show the site's objective, which is a to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # The user creates an initial element: 1. Buy peacock feathers
        # The page updates and shows this element in the list

        # The decides to add a new one, Use peacock feathers to make a fly
        # The page updates again and shows both elements

        # A unique URL is generated for the user, to remember the list that
        # they have created for next time

        # User re-visits site to confirm the list is still there

if __name__ == "__main__":
    unittest.main()