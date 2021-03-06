from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):

        ## User opens site on their browser
        self.browser.get(self.live_server_url)

        ## The browser should show the site's objective, which is a to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        ## The user creates an initial element: 1. Buy peacock feathers
        ## The page updates and shows this element in the list
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        ## The decides to add a new one, Use peacock feathers to make a fly
        ## The page updates again and shows both element
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')

        inputbox.send_keys(Keys.ENTER)

        ## Page updates and both elements should be in the list
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')


        ## A unique URL is generated for the user, to remember the list that
        ## they have created for next time
        # self.fail('Finish the test!')
        ## User re-visits site to confirm the list is still there

    def test_multiple_users_can_start_lists_at_different_urls(self):
        ## Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        ## She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        ## Now a new user, Francis, comes along to the sire

        ## We use a new broser ession to make ure that no information
        ## of Edith's is coming through from cookies
        self.browser.quit()
        self.browser = webdriver.Firefox()

        ## Francis visits the home page. There is no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        ## Francis starts a new list by entering a new item. He is less
        ## interesting than Edith

        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        ## Francis gets his own URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        ## Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        ## Satisfied, they both go back to sleep
