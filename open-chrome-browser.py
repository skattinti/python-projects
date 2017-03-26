from selenium import webdriver
import time

driver = webdriver.PhantomJS()  # Optional argument, if not specified will search path.
driver.set_window_size(1120, 550)
driver.get('http://www.google.com/xhtml')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
