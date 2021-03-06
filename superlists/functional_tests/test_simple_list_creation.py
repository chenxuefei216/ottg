from .base import TodoFunctionalTest
from selenium import webdriver

class NewVisitorTest(TodoFunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage.
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # She is invited to enter a to-do itme straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feather" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        self.send_input_to_table('Buy peacock feathers')

        # When she hits enter, she is taken to a new url,
        # and now the page lists
        # "1. Buy peacock feathers" as an item in a to-do lists
        edith_list_url = self.browser.current_url
        self.assertRegexpMatches(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('Buy peacock feathers')

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make fly"
        self.send_input_to_table('Use peacock feathers to make fly')

        #The homepage updates again, and now shows both items on her lists
        self.check_for_row_in_list_table('Buy peacock feathers')
        self.check_for_row_in_list_table('Use peacock feathers to make fly')

        # Now a new user Francis comes along

        ## We use a new browser session to make sure no information
        ## of Edith's comes along (EG cookies, localStorage)
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make fly', page_text)

        # Francis starts a new list by entering a new item.
        self.send_input_to_table('Buy milk')

        # Francis gets his own unique url
        francis_list_url = self.browser.current_url
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        #Satisfied, they both go back to sleep
