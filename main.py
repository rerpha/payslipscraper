# /// script
# dependencies = [
#   "selenium"
# ]
# ///
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

SLEEP_TO_WAIT_FOR_PDF_LOAD = 10

driver = webdriver.Chrome()
driver.get("https://ebs.ssc.rcuk.ac.uk")

input("please log in, then navigate to the payslips page, then hit enter")

# Cache the payslips options - this will be the same on every page
payslips_dropdown = driver.find_element(by=By.ID, value="AdvicePicker")
payslips = Select(payslips_dropdown)

option_list = [option.text for option in payslips.options]

for i, option in enumerate(option_list):
    print(f"doing option {i}, payslips: {option}")
    payslips_dropdown = driver.find_element(by=By.ID, value="AdvicePicker")
    payslips = Select(payslips_dropdown)

    payslips.select_by_index(i)
    # find "go" button and click it
    go_button = driver.find_element(by=By.ID, value="Go")
    go_button.click()
    sleep(SLEEP_TO_WAIT_FOR_PDF_LOAD)
    # fuck you oracle why do I have to click twice to view a pdf
    # I could be clever here and not wait but I am rather lazy and can't be arsed.
    go_button = driver.find_element(by=By.ID, value="Go")
    go_button.click()
    sleep(SLEEP_TO_WAIT_FOR_PDF_LOAD)
    export_button = driver.find_element(by=By.ID, value="Export")
    export_button.click()






