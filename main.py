# /// script
# dependencies = [
#   "selenium"
# ]
# ///
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://ebs.ssc.rcuk.ac.uk")

input("please log in, then navigate to the payslips page, then hit enter")

# Cache the payslips options - this will be the same on every page
payslips_dropdown = driver.find_element(by=By.ID, value="AdvicePicker")
payslips = Select(payslips_dropdown)

option_list = payslips.options

print(option_list)

for i, option in enumerate(option_list):
    payslips_dropdown = driver.find_element(by=By.ID, value="AdvicePicker")
    payslips = Select(payslips_dropdown)

    payslips.select_by_index(i)
    # find "go" button and click it
    #wait 15 seconds (hopefully this is long enough for it to give us a pdf)
    go_button = driver.find_element(by=By.ID, value="Go")
    go_button.click()
    sleep(20)




