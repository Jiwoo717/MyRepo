import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import getpass

# Credentials from environment variables
FB_EMAIL = os.environ.get('FB_EMAIL') or getpass.getpass("Enter your Facebook email: ")
FB_PASSWORD = os.environ.get('FB_PASSWORD') or getpass.getpass("Enter your Facebook password: ")
GMAIL_EMAIL = os.environ.get('GMAIL_EMAIL') or getpass.getpass("Enter your Gmail email: ")
GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD') or getpass.getpass("Enter your Gmail password: ")

# open facebook function
def openFB():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driverOne = webdriver.Chrome(PATH)

    driverOne.get("https://facebook.com")

    find_it = driverOne.find_element_by_id("email")
    find_it.send_keys(FB_EMAIL)
    find_it = driverOne.find_element_by_id("pass")
    find_it.send_keys(FB_PASSWORD)
    find_it.send_keys(Keys.ENTER)

# open gmail function
def openGmail():
    PATH2 = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH2)

    driver.get("https://gmail.com")

    fill_field = driver.find_element_by_tag_name("Sign In")
    fill_field.send_keys(Keys.ENTER)
    time.sleep(1)
    login_box = driver.find_element_by_tag_name('input')
    login_box.send_keys(GMAIL_EMAIL)
    login_box.send_keys(Keys.ENTER)

root = tk.Tk()

# GUI with buttons for the actions
canvas = tk.Canvas(root, bg="#B4B3CC")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.7, relx=0.15, rely=0.1)

gettingStarted = tk.Button(root, text="Open you Fb Page", padx=30, pady=10, bg="#3437F3", fg="white", command=openFB)
gettingStarted.pack()

openGmail = tk.Button(root, text="Open your Gmail", padx=30, pady=10, fg="black", bg="#00D32D", command=openGmail)
openGmail.pack()

root.mainloop()
