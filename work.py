from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import smtplib
import time

PATH = "D:\python_projects\chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://tymbe.com/tymber/login")

email = driver.find_element(By.ID, "username").send_keys("EMAIL")
password = driver.find_element(By.ID, "password").send_keys("PASSWORD")

prihlasit = driver.find_element(By.XPATH, "//*[@id='tymbe']/div/div/form/div[3]/button").click()
time.sleep(5)

hledat = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/button").click()
okres = driver.find_element(By.XPATH, "//*[@id='filter_loccation']").send_keys("Ostrava")
hledat = driver.find_element(By.XPATH, "//*[@id='Main']/div/div[3]/div/form/button").click()
time.sleep(5)

while True:
	smeny = driver.find_elements(By.XPATH, "//*[@id='Main']/div/div[1]")
	for smena in smeny:
		den = smena.find_elements(By.TAG_NAME, "H3")
		for i in den:
			print(i.text)
			if(i.text == "pátek"):	#pátek is friday in my language
				with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
					smtp.ehlo()
					smtp.starttls()
					smtp.ehlo()
					sender = "EMAIL"
					sender_password = "PASSWORD"
					receiver = "EMAIL"
					smtp.ehlo()
					smtp.login(sender, sender_password)
					subject = 'smena na pátek' #smena na pátek == shift for friday
					body = "smena na patek"
					message = f'Subject: {subject}\n\n{body}'
					smtp.sendmail(sender, receiver, message)
					print("Email sent!")
					driver.quit()
			else:
				time.sleep(20)



			



