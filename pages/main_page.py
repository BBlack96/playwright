from base.base_page import BasePage
from pages.locators.base_locators import BaseLocators
from pages.locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Open Main Page")
    def open_main_page(self):
        self.open("https://demoqa.com/")

    @allure.step("Click Elements Card")
    def click_elements_card(self):
        self.page.click(MainPageLocators.ELEMENTS_CARD)

    @allure.step("Click Forms Card")
    def click_forms_card(self):
        self.page.click(MainPageLocators.FORMS_CARD)

    @allure.step("Click Alerts Card")
    def click_alerts_card(self):
        self.page.click(MainPageLocators.ALERTS_CARD)

    @allure.step("Click Widgets Card")
    def click_widgets_card(self):
        self.page.click(MainPageLocators.WIDGETS_CARD)

    @allure.step("Click Interactions Card")
    def click_interactions_card(self):
        self.page.click(MainPageLocators.INTERACTIONS_CARD)

    @allure.step("Click Book Store Card")
    def click_book_store_card(self):
        self.page.click(MainPageLocators.BOOK_STORE_CARD)

    @allure.step("Get Header")
    def is_header_visible(self):
        return self.page.locator(BaseLocators.HEADER_LINK)



