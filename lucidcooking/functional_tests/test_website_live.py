from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase




class FunctionalTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def testLiveWebsiteIsWorking(self):
		# User visits the homepage
		self.browser.get('http://cooking.langato.com')

		# User sees Lucid Cooking in the title
		self.assertIn('Lucid Cooking', self.browser.title)
