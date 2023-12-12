import time

import undetected_chromedriver as uc


if __name__ == "__main__":
    print("getting the driver")
    driver = uc.Chrome()
    driver.get("https://www.google.com")
    time.sleep(30)