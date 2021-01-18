
#Loads selenium and webdriver for chrome
from selenium import webdriver

#Imports time which allows for a delay
import time

#Opens Chrome
web = webdriver.Chrome()
#Accesses Bootcampspot
web.get('https://bootcampspot.com/')

#Adds a 5 second delay for the HTML elements to render.
time.sleep(1)

#A variable holding the email log in
email = "daccian.k@gmail.com"
#This finds the log in form in the browser
login = web.find_element_by_xpath('//*[@id="emailAddress"]')
#Takes the login variable which is the xpath to the email log in and fills it with the variable email.
login.send_keys(email)
#A variable holding the pwsd
passwd = "GoofyGoober1*"
#Finds the form entry for the password
pwd = web.find_element_by_xpath('//*[@id="password"]')
#Enters the password
pwd.send_keys(passwd)

#finds the log in button
loginbutton = web.find_element_by_xpath('/html/body/div/section/div/div[2]/button')
#clicks the log in button
loginbutton.click()

time.sleep(5)
#Survey-----------------------------------

#Start the survey
startsurvey = web.find_element_by_xpath('//*[@id="main-content"]/div/section/div/div/div/button')
startsurvey.click()

time.sleep(4)

#HOW WOULD YOU RATE YOUR OVERALL SATISFACTION WITH CLASS THIS PAST WEEK?
satisfied = web.find_element_by_xpath('//*[@id="main-content"]/div/section/div/div/form/ol/li[1]/fieldset/div/label[4]')
satisfied.click()
time.sleep(.5)

#HOW WOULD YOU RATE THE PACE OF CLASS?
pace = web.find_element_by_xpath('//*[@id="213-3"]')
pace.click()
time.sleep(.5)

#HOW SATISFIED WERE YOU WITH THE LEVEL OF ACADEMIC SUPPORT YOU RECEIVED
support = web.find_element_by_xpath('//*[@id="214-4"]')
support.click()
time.sleep(.5)

#DO YOU THINK YOU ARE PREPARED TO APPLY WHAT YOU LEARNED THIS PAST WEEK OUTSIDE OF THE COURSE SETTING?
prepared = web.find_element_by_xpath('//*[@id="215-4"]')
prepared.click()
time.sleep(.5)

#HOW ENGAGING WAS YOUR INSTRUCTOR THIS PAST WEEK?
engaged = web.find_element_by_xpath('//*[@id="216-5"]')
engaged.click()
time.sleep(.5)

#HOW CLEAR WAS YOUR INSTRUCTOR THIS PAST WEEK?
clear = web.find_element_by_xpath('//*[@id="217-5"]')
clear.click()
time.sleep(.5)

#HOW KNOWLEDGEABLE DID YOUR INSTRUCTOR SEEM TO BE THIS PAST WEEK?
knowledgable = web.find_element_by_xpath('//*[@id="218-5"]')
knowledgable.click()
time.sleep(.5)

#HOW WOULD YOU RATE THE USEFULNESS OF THE LAST HOMEWORK FEEDBACK YOU RECEIVED?
useful = web.find_element_by_xpath('//*[@id="219-4"]')
useful.click()
time.sleep(.5)

#HOW MANY HOURS DID YOU SPEND OUTSIDE OF CLASS THIS PAST WEEK ON HOMEWORK?
hours = web.find_element_by_xpath('//*[@id="220-3"]')
hours.click()
time.sleep(.5)

#Anything else to add?
cool = "Cryptography and python are cool"
anythingelse = web.find_element_by_xpath('//*[@id="221"]')
#enters the phrase
anythingelse.send_keys(cool)

#IN WHAT WAYS DID YOUR INSTRUCTIONAL TEAM SUPPORT OR NOT SUPPORT YOU THIS PAST WEEK? (INSTRUCTOR, TA'S, LEARNING ASSISTANTS, ETC.)

supportcomment = "I did not receive the practice questions for the security + exam"
supportcommentsubmit = web.find_element_by_xpath('//*[@id="222"]')
supportcommentsubmit.send_keys(supportcomment)

time.sleep(2)

#Submit Feedback
#submission = web.find_element_by_xpath('//*[@id="main-content"]/div/section/div/div/form/div/div/button')
#submission.click()

#Confirmation
#get_confirmation_web_text = web.find_element_by_css_selector('')
#print(get_confirmation_web_text.text)
#if ((get_confirmation_web_text) == thank you for signing in) :
#    print("Log in was successful")
#else:
#    print("Log in failed")