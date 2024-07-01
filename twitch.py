from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from seleniumbase import Driver


driver = Driver(uc=True)
driver.get("https://m.twitch.tv/")
sleep(5)
close_button = driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='Accept']/parent::*")
close_button.click()

# click on the search icon
search_icon = WebDriverWait(driver, timeout=5).until(
    es.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/search')]"))
)
search_icon.click()

# enter a search query "StarCraft II"
search_input = WebDriverWait(driver, timeout=5).until(
    es.element_to_be_clickable((By.XPATH, "//input[@value='']"))
)
search_input.send_keys("StarCraft II")
search_input.send_keys(Keys.RETURN)

# scroll down the page two times
wait = WebDriverWait(driver, timeout=5)
wait.until(es.presence_of_element_located((By.TAG_NAME, 'body')))
for _ in range(2):
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    sleep(2)

# play content
driver.find_element(By.XPATH, '//div[2]/h2').click()

try:
    # find the play/pause button of the video
    play_button = WebDriverWait(driver, timeout=5).until(
        lambda driver: driver.find_element(By.XPATH, '//button[@data-a-target="player-play-pause-button"]'))
    if play_button.get_attribute('data-a-player-state') != 'paused':
        print("The video is playing.")
    else:
        print("The video is not played.")
except Exception as e:
    print(f"The video player element could not be found: {e}")

# save screenshot
sleep(3)
driver.save_screenshot("reports/streamer_page.png")
driver.quit()
