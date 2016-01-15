from .base import TodoFunctionalTest

class ManyListsTest(TodoFunctionalTest):
    def change_list_name(self, list_name):
        inputbox=self.browser.find_element_by_id('id_rename_list')
        inputbox.clear()
        inputbox.send_keys(list_name + '\n')

    def test_can_create_and_view_multiple_lists(self):
      # Edith wants to create and add items.
      # back to the home page.
      # create a new list.
      # see the first list.

      # Edith comes to the home page
      # creates a new List
      # and fills in her grocery list.
      self.browser.get(self.live_server_url)
      self.send_input_to_table('Buy milk')
      self.send_input_to_table('Buy cheese')
      self.check_for_row_in_list_table('Buy milk')
      self.check_for_row_in_list_table('Buy cheese')

      # she sees she can change a list name.
      self.change_list_name('Groceries')

      # Edith goes back to the home page & sees her grocery list.
      self.browser.get(self.live_server_url)
      self.check_for_row_in_list_table('Groceries')

      # Edith creates a new list for her art history homework.
      self.browser.send_input_to_table('Read textbook')

      # Edith opens the home page later and sees both lists.
      self.browser.get(self.live_server_url)
      self.check_for_row_in_list_table('Groceries')
      self.check_for_row_in_list_table('Read textbook')

      # Edith goes to the grocery list and sees what she needs to buy.
      row = self.find_table_row('Groceries')
      row.find_element_by_tag_name('a').click()
      self.check_for_row_in_list_table('Buy milk')
      self.check_for_row_in_list_table('Buy cheese')
