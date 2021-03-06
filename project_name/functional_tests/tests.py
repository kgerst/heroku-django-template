# -*- coding: utf-8 -*-
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FirstFunctionalTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

	def test_home_title(self):
		self.browser.get(self.get_full_url("home"))
		self.assertIn("{{project_name}}", self.browser.title)	
	