import os
import shutil

import allure
import pytest
from playwright.sync_api import sync_playwright

from config.config import Config

headless = False
screenshots_dir = "screenshots"
videos_dir = "videos"


@pytest.fixture(scope="session", autouse=True)
def cleanup():
    for directory in [screenshots_dir, videos_dir]:
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)


@pytest.fixture(scope="session")
def browser(request):
    with sync_playwright() as p:
        browser = getattr(p, request.param).launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture(scope="function", autouse=True)
def test_artifacts(request):
    yield
    if request.node.rep_call.failed:
        allure.attach.file(f"screenshots/{request.node.name}.png", name="screenshot",
                           attachment_type=allure.attachment_type.PNG)
        allure.attach.file(f"videos/{request.node.name}.webm", name="video",
                           attachment_type=allure.attachment_type.WEBM)


@pytest.fixture(scope="function")
def context(request, browser):
    context = browser.new_context(record_video_dir="videos/")
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context, request):
    page = context.new_page()
    yield page
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
    page.close()
    if request.node.rep_call.failed:
        page.video.save_as(path=f"videos/{request.node.name}.webm")


@pytest.fixture(name="config", scope="session", autouse=True)
def config_fixture():
    return Config(_env_file=".env")
