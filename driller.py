from Crawler import Crawler
from pathlib import Path
from names import get_first_name, get_last_name
from selenium.webdriver.common.keys import Keys
from random import random
from time import time

from config import username, password

def load_more(url):
	crawler = Crawler()
	crawler.get(url)
	assert "Sign In" in crawler.title, "TITLE INCORRECT"
	try:
		start = int(time())

		user_name_input = crawler.findElementByXPath("//*[@id='userNameInput']")
		user_name_input.send_keys(username)
		password_input = crawler.findElementByXPath("//*[@id='passwordInput']")
		password_input.send_keys(password)
		submit_button = crawler.findElementByXPath("//*[@id='submitButton']")
		crawler.click(submit_button)

		new_folder_button = crawler.findElementByXPath("//button[. = 'New Folder']")
		crawler.click(new_folder_button)

		name_input = crawler.findElementByXPath("//*[@id='nameId']")
		name_input.send_keys("Random Name")
		submission_type_dropdown = crawler.findElementByXPath("//*[@name='SL_SubmissionType']")
		crawler.click(submission_type_dropdown)

	except Exception as e:
		print('EXCEPTION', e)
	# crawler.close()
	end = int(time())
	print(start)
	print(end)
	print('TOTAL TIME ELAPSED: %s' % (end - start))