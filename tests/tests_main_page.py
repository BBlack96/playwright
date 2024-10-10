import pytest

from base.base_test import BaseTest


@pytest.mark.parametrize("browser", ["firefox", "chromium"], indirect=True)
class TestMainPage(BaseTest):

    @pytest.fixture(autouse=True, scope='function')
    def open_site(self, setup):
        self.main_page.open_main_page()
        yield

    def test_title(self, config):
        assert config.BASE_URL == self.main_page.get_url()

    def test_main(self, config):
        assert config.TITLE == self.main_page.title()

    def test_elements_card(self, config):
        self.main_page.click_elements_card()
        assert config.ELEMENTS_URL == self.elements_page.get_url()

    def test_forms_card(self, config):
        self.main_page.click_forms_card()
        assert config.FORMS_URL == self.elements_page.get_url()

    def test_header_visible(self):
        assert self.main_page.is_visible(self.main_page.get_header())