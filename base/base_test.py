from pages.elements_page import ElementsPage
from pages.main_page import MainPage
from pytest import fixture

class BaseTest:
    _main_page = None
    _elements_page = None

    @fixture(autouse=True)
    def setup(self, request, page):
        request.cls.page = page

    @property
    def main_page(self):
        if self._main_page is None:
            self._main_page = MainPage(self.page)
        return self._main_page

    @property
    def elements_page(self):
        if self._elements_page is None:
            self._elements_page = ElementsPage(self.page)
        return self._elements_page
