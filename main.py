# /// script
# dependencies = [
#   "selenium"
# ]
# ///
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep
import os
import glob

SLEEP_TO_WAIT_FOR_PDF_LOAD = 10
DOWNLOADS_DIR = "C:\\users\luj96656\\downloads\\"
driver = webdriver.Chrome()
driver.get("https://ebs.ssc.rcuk.ac.uk")

input("please log in, then navigate to the payslips page, then hit enter")

# Cache the payslips options - this will be the same on every page
payslips_dropdown = driver.find_element(by=By.ID, value="AdvicePicker")
payslips = Select(payslips_dropdown)

option_list = [option.text for option in payslips.options]

for i, option in enumerate(option_list):
    try:
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
        # wait for pdf download. if acrobat opens here you might run into a fileaccessdenied error.
        # i just renamed acrobat.exe so it didnt open...
        sleep(1)

        list_of_files = glob.glob(
            DOWNLOADS_DIR + "*.pdf"
        )  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)  #
        print(f"latest file: {latest_file}")

        new_filename = f"{DOWNLOADS_DIR}{option.replace(' ', '')}.pdf"
        os.rename(latest_file, new_filename)

    except Exception as e:
        print(f"skipped {option}: {str(e)}")
