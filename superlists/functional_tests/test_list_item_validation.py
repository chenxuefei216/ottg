from .base import TodoFunctionalTest
from unittest import skip

class ItemValidationTest(TodoFunctionalTest):
    @skip("Haven't implemented this")
    def test_cannot_add_empty_list_item(self):
        # Edith goes to the home page, and accidentally tries
        # to submit an empty list item.
        # She hits "Enter" on the empty input box

        #The home page refreshes, and there is an error message
        #saying that list items cannot be blank

        #She tries again with some text for the item
        #which now works.

        # Perversely tries to enter a second blank item

        #She receives a similar warning on the list page

        #and she can correct it by filling some text in
        self.fail("finish the app")
