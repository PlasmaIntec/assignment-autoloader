from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui

class Crawler:
	def __init__(self):
		options = webdriver.ChromeOptions()
		options.add_experimental_option("detach", True)
		# options.add_argument('headless')
		driver = webdriver.Chrome(options=options)
		driver.set_window_position(0, 0)
		driver.set_window_size(730, 1600)
		wait = ui.WebDriverWait(driver, 3)
		self.driver = driver
		self.wait = wait

	def closeExtraTabs(self):
		if len(self.driver.window_handles) == 1:
			return
		this_window = self.driver.window_handles[1]
		self.driver.switch_to_window(this_window)
		self.driver.close()
		original_window = self.driver.window_handles[0]
		self.driver.switch_to_window(original_window)

	def getTitle(self):
		return self.driver.title

	def get(self, url):
		self.driver.get(url)
		self.title = self.driver.title
		
	def scrollTo(self, element):
		self.driver.execute_script("arguments[0].scrollIntoView()", element)
		# print("SCROLLED")

	def switchFrameByXPath(self, xpath_selector):
		self.driver.switch_to.frame(self.driver.find_element_by_xpath(xpath_selector))
		# print("SWITCHED TO FRAME WITH XPATH: ", xpath_selector)

	def switchToParentFrame(self):
		self.driver.switch_to.parent_frame()

	def highlight(self, xpath_selector):
		# try: # reset previous highlight if there was a previous highlight
		# 	if self.previousHighlight:
		# 		print('PREV: ', self.previousHighlight)
		# 		element = self.findElementByXPath(self.previousHighlight)
		# 		self.driver.execute_script('''
		# 			var ele = arguments[0];
		# 			ele.setAttribute('style', 'background: initial; border: initial;');
		# 			console.log('UNSET');
		# 			console.log(ele);
		# 			console.log('STYLE');
		# 		''', element)
		# except Exception as e:
		# 	if e.__class__.__name__ == 'AttributeError':
		# 		print('NO PREVIOUS HIGHLIGHT')
		# 	elif e.__class__.__name__ == 'TimeoutException':
		# 		print('COULD NOT FIND ELEMENT WITH XPATH: ', self.previousHighlight)
		# 	else:
		# 		print('GENERIC ERROR', e.__class__.__name__)
		element = self.findElementByXPath(xpath_selector)
		self.driver.execute_script('''
			var ele = arguments[0];
			ele.setAttribute('style', 'background: yellow; border: 2px solid red;');
			console.log(ele);
		''', element)
		self.previousHighlight = xpath_selector

	def findElementByXPath(self, xpath_selector):
		# print("FOUND ELEMENT WITH XPATH: ", xpath_selector)
		return self.wait.until(
			EC.element_to_be_clickable((By.XPATH, xpath_selector))
		)

	def findPresentElementByXPath(self, xpath_selector):
		# print("FOUND ELEMENT WITH XPATH: ", xpath_selector)
		return self.wait.until(
			EC.presence_of_element_located((By.XPATH, xpath_selector))
		)

	def findElementsByXPath(self, xpath_selector):
		elements = self.wait.until(
			EC.visibility_of_any_elements_located((By.XPATH, xpath_selector))
		)
		print(f"FOUND {len(elements)} ELEMENTS WITH XPATH: ", xpath_selector)
		return elements

	def click(self, element):
		ActionChains(self.driver).move_to_element(element).click().perform()
		# print("CLICKED")

	def close(self):
		self.driver.close()