import allure
import pytest
from playwright.sync_api import sync_playwright

from config.config import Config

headless = False


@pytest.fixture(scope="session")
def browser(request):
    with sync_playwright() as p:
        browser =  getattr(p, request.param).launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture(scope="function", autouse=True)
def attach_allure_artifacts(request):
    yield
    if request.node.rep_call.failed:
        allure.attach.file(f"traces/{request.node.name}.zip", name="trace", attachment_type="application/zip")
        allure.attach.file(f"screenshots/{request.node.name}.png", name="screenshot",
                           attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope="function")
def context(request, browser):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path=f"traces/{request.node.name}.zip")
    context.close()


@pytest.fixture(scope="function")
def page(context, request):
    page = context.new_page()
    yield page
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
    page.close()

@pytest.fixture(name="config", scope="session", autouse=True)
def config_fixture():
    return Config(_env_file=".env")
