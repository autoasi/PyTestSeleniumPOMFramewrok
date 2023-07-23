# ----------------------------------------------------------------------------
#   SUPPORTED LOCATOR STRATEGIES:
#       * XPATH
#       * ID
#       * NAME
#       * CSS_SELECTOR
#       * TAG_NAME
#       * LINK_TEXT
#       * PARTIAL_LINK_TEXT
# ----------------------------------------------------------------------------

from selenium.webdriver.common.by import By

username_field = (By.ID, "username")
password_field = (By.NAME, "password")
submit_button = (By.XPATH, "//button[@class='btn']")
error_message = (By.ID, "error")
