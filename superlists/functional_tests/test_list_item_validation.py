from .base import TodoFunctionalTest
from unittest import skip

class ItemValidationTest(TodoFunctionalTest):
    
    def test_cannot_add_empty_list_item(self):
        # Edith goes to the home page, and accidentally tries
        # to submit an empty list item.
        # She hits "Enter" on the empty input box
        self.browser.get(self.live_server_url)
        self.send_input_to_table('')

        #The home page refreshes, and there is an error message
        #saying that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #She tries again with some text for the item
        #which now works.
        self.send_input_to_table('Buy milk')
        self.check_for_row_in_list_table('1. Buy milk')

        # Perversely tries to enter a second blank item
        self.send_input_to_table('')

        #She receives a similar warning on the list page
        self.check_for_row_in_list_table('1. Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #and she can correct it by filling some text in
        self.send_input_to_table('Make tea')
        self.check_for_row_in_list_table('1. Buy milk')
        self.check_for_row_in_list_table('2. Make tea')
