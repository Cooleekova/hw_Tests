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

    def test_no_project_alert_button_redirects_to_add_page(self):
        self.browser.get(self.live_server_url)
        # The user requests the page for the first time

        add_url = self.live_server_url + reverse('add')
        self.browser.find_element(By.TAG_NAME, 'a').click()
        self.assertEquals(self.browser.current_url, add_url)

    
    def test_user_sees_project_list(self):
        # At first we create single test project 'project1'
        Project.objects.create(
            name = 'project1',
            budget = 10000
        )
        self.browser.get(self.live_server_url)
        # The user sees the project on the screen
        self.assertEquals(
            self.browser.find_element(By.TAG_NAME, 'h5').text,
            'project1'
        )

    
    def test_user_redirected_to_project_detail(self):
        # At first we create single test project 'project1'
        project1 = Project.objects.create(
            name = 'project1',
            budget = 10000
        )
        self.browser.get(self.live_server_url)
        # The user sees the project on the screen,
        # clicks the 'VISIT' button and is redirected to the project detail page
        detail_url = self.live_server_url + reverse('detail', args=[project1.slug])
        self.browser.find_element(By.LINK_TEXT, 'VISIT').click()
        self.assertEquals(self.browser.current_url, detail_url)