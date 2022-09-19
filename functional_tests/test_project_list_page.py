from selenium import webdriver
from selenium.webdriver.common.by import By
from budget.models import Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestProjectListPage(StaticLiveServerTestCase):
    
    def setUp(self):
        """Creates new browser instance"""
        self.browser = webdriver.Chrome()

    
    def tearDown(self):
        """Closes the browser when testing is finished"""
        self.browser.close()


    def test_no_project_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        # The user requests the page for the first time
        
        alert = self.browser.find_element(By.CLASS_NAME, 'noproject-wrapper')
        self.assertEquals(
            alert.find_element(By.TAG_NAME, 'h3').text,
            'Sorry, you don\'t have any projects, yet.'
        )