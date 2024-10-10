from base.base_page import BasePage

class ElementsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://demoqa.com/elements"