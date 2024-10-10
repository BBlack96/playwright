from pydantic_settings import BaseSettings

class Config(BaseSettings):
    BASE_URL: str
    ELEMENTS_URL: str
    FORMS_URL: str
    ALERTS_URL: str
    WIDGETS_URL: str
    INTERACTIONS_URL: str
    BOOK_STORE_URL: str
    TITLE: str
