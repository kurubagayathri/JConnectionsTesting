from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.bt.com/")
try:
    cookie_alert = driver.switch_to.alert
    cookie_alert.dismiss()
except:
    pass
mobile_menu = driver.find_element(By.XPATH, "//span[text()='Mobile']")
actions = ActionChains(driver)
actions.move_to_element(mobile_menu).perform()
mobile_phones_option = driver.find_element(By.XPATH, "//*[@id='bt-navbar']")
actions = ActionChains(driver)
actions.move_to_element(mobile_phones_option).perform()
banners = driver.find_elements(By.XPATH, "//div[contains(@class, 'see-handset')]//div[contains(@class, 'slider-item')]")
if len(banners) >= 3:
    print("There are at least 3 banners below 'See Handset details'.")
else:
    print("There are less than 3 banners below 'See Handset details'.")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
view_sim_only_deals = driver.find_element(By.XPATH, "//*[@id='__next']")
actions = ActionChains(driver)
actions.move_to_element(view_sim_only_deals).perform()
expected_title = "SIM Only Deals | SIM Card Deals | BT"
if driver.title == expected_title:
    print("Title validation passed. Current title is:", driver.title)
else:
    print("Title validation failed. Current title is:", driver.title)
plan_info = driver.find_element(By.XPATH, "//*[@id='__next']")
if "125GB 250GB Essential Plan, was £27 £18.90 per month" in plan_info.text:
    print("Plan information validation passed.")
else:
    print("Plan information validation failed. Actual information:", plan_info.text)
driver.quit()