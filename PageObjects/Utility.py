class Utility:

    def __init__(self, driver):
        self.driver = driver

    def input_field_using_css_selector(self, full_name, css_selector):
        text_input = self.driver.find_element_by_css_selector(css_selector)
        text_input.clear()
        text_input.send_keys(full_name)

    def get_value_of_placeholder_with_css(self, css):
        placeholder = self.driver.find_element_by_css_selector(css).get_attribute("placeholder")
        return placeholder
