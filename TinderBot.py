#Importing Modules
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from random import randint
import json

# Launch Chrome on Tinder's website
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.tinder.com')
print("Opened tinder")
sleep(1)

# Import your credentials
with open('creds.json') as json_file:
    data = json.load(json_file)
    print(data)
email = data['email']
password = data['pass']

# Handle Poped Up Window
main_page = driver.current_window_handle
sleep(1)
print(main_page)

# Deal with Cookies
cookies = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/button").click()
print("Clicked Accepted")
sleep(2)

# Deal with Login Page
login_first_page = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/span/div[1]/div/button").click()
print("Clicked Login")
sleep(1)

print(driver.window_handles)

for x in driver.window_handles:
    print(x)
    if x != driver.window_handles:
        login_page = x

sleep(1)

driver.switch_to.window(login_page)
sleep(1)

email = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(email)
sleep(1)

email_accept = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/span").click()
sleep(1)

password = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(password)
sleep(1)

password_accept = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/span").click()
sleep(1)

driver.switch_to.window(main_page)
sleep(5)
print(driver.window_handles)


allow_location = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]/span").click()
print("Allowed Notifications")
sleep(1)

enable_notifications = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
print("Enabled Notifications")

sleep(3)

message_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/aside/nav/div/div/div/div[1]/div/div[2]/button").click()
print("Liked")
sleep(2)

def like():
    like_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button").click()
    sleep(1)

def dislike():
    dislike = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button").click()
    sleep(1)

def random_number():
    a = randint(0,11)
    print(a)
    return a

def auto_swipe():
    while True:
        b = random_number()
        if b == 8 or b == 9 or b == 10:
            dislike()
        elif b == 0 or b == 1 or b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7:
            like()

#while try here is used for in case there is a match
while True:
    try:
        auto_swipe()
    except Exception:
        try:
            match_go_back_main_menu = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/a").click()
            sleep(1)
        except Exception:
            close_popup = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/button[2]").click()
            sleep(1)
