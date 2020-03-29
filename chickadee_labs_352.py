from Crawler import Crawler
from pathlib import Path
from names import get_first_name, get_last_name
from selenium.webdriver.common.keys import Keys
from random import random
from time import time, sleep

from config import username, password
from data import chickadee_data

due_time = "8:00 AM"

def upload(url):
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

		for assignment in chickadee_data:
			name, due_date = assignment

			new_folder_button = crawler.findElementByXPath("//button[. = 'New Folder']")
			crawler.click(new_folder_button)

			name_input = crawler.findElementByXPath("//*[@id='nameId']")
			name_input.send_keys(name)
			category_dropdown = crawler.findElementByXPath("//option[text()='Chickadee Labs']")
			category_dropdown.click()
			score_input = crawler.findElementByXPath("//*[@id='z_bu']")
			score_input.send_keys("10")
			new_grade_item_button = crawler.findElementByXPath("//a[text()='[New Grade Item]']")
			new_grade_item_button.click()

			sleep(.5)
			crawler.switchFrameByXPath("//iframe[@title='New Grade Item']")

			numeric_button = crawler.findElementByXPath("//a[text()='Numeric']")
			numeric_button.click()
			grade_name_input = crawler.findElementByXPath("//*[@id='z_c']")
			grade_name_input.send_keys(name)
			grade_short_name_input = crawler.findElementByXPath("//*[@id='z_h']")
			grade_short_name_input.send_keys(name.split(" ")[0])
			grade_category_dropdown = crawler.findElementByXPath("//option[text()='Chickadee Labs (30% of final grade)']")
			grade_category_dropdown.click()

			crawler.switchToParentFrame()
			save_button = crawler.findElementByXPath("//td/button[text()='Save']")
			crawler.click(save_button)
			restrictions_button = crawler.findElementByXPath("//span[text()='Restrictions']")
			crawler.click(restrictions_button)
			has_due_date_checkbox = crawler.findElementByXPath("//*[@id='z_n']")
			crawler.click(has_due_date_checkbox)
			due_date_input = crawler.findElementByXPath("//*[@id='z_o']")
			while len(due_date_input.get_attribute('value')) > 0:
				due_date_input.send_keys(Keys.BACKSPACE)
			due_date_input.send_keys(due_date)
			due_time_input = crawler.findElementByXPath("//*[@id='z_o$time']")
			while len(due_time_input.get_attribute('value')) > 0:
				due_time_input.send_keys(Keys.BACKSPACE)
			due_time_input.send_keys(due_time)
			save_and_close_button = crawler.findElementByXPath("//button[text()='Save and Close']")
			crawler.click(save_and_close_button)

	except Exception as e:
		print('EXCEPTION', e)
	end = int(time())
	print('TOTAL TIME ELAPSED: %s' % (end - start))