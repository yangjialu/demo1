import atx
import time
import pytest
from pages.base import BasePage


@pytest.fixture()
def init_app_noreset():
    app = atx.connect()
    BasePage(app).close_app()
    BasePage(app).start_app()
    if BasePage(app).findId("com.sabac.hy:id/first_skip", timeout=1):
        BasePage(app).clickId("com.sabac.hy:id/first_skip")
    yield app
    BasePage(app).close_app()


@pytest.fixture()
def init_app_reset():
    app = atx.connect()
    BasePage(app).close_app()
    BasePage(app).start_app()
    yield app
    BasePage(app).close_app(clear=True)
