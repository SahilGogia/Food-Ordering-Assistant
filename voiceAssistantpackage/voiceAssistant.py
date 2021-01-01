import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from fd import *

fname = faceid() #recognizes the user and returns the name


if fname == "sahil":

    email = "sahil.gogia025@gmail.com"
else:
    email = "sahil.gogia2018@gmail.com"




def speak(text): #Assistant voice output
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said
listen = False
print("\n")
print("say 'I want to eat something to activate the voice Assistant'...")
text = get_audio().lower() #user voice input
#text = "I want to eat something"
response = ["is hungry", "am hungry", "want to eat", "wants to eat"] #possible replies
if any(x in text for x in response):
     speak("  Can I order something for you")
     text = get_audio().lower()
     text = "yes"
     arr= ["yes","yup", "yee", "ya", "yaa", "yeah"]
     i=0
     if "yes" in text:
          i=1
     elif "yup" in text:
         i=1
     elif "yee" in text:
         i=1
     elif "yeah" in text:
         i=1

     if i==1:
          speak(" From where would you like to order")

          print("\n")
          print("----------------------")
          print("Zomato")
          print("\n"+"----------------------"+"\n")
          text = get_audio().lower()
          text = "zomato"
          website_name = ["Uber" , "swiggy" , "zomato" , "foodpanda"]
          if "uber" in text:
             webbrowser.open('https://www.ubereats.com')
          elif "zomato" in text:
             driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
             driver.get("https://www.zomato.com/ncr") #opens website

             time.sleep(2)
             driver.find_element_by_link_text("Login").click()  #finds the link containing text Login
             action = ActionChains(driver)

             time.sleep(1) # program halt
             driver.find_element_by_xpath("//span[contains(text(),'Continue with Email')]").click() #finds the element by its path and clicks on it
             inpt = driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/section[2]/section/section/section/input")
             inpt.click()
             time.sleep(3)
             inpt.send_keys(email)
             driver.find_element_by_xpath("//span[contains(text(),'Send One Time Password')]").click()
             speak("Please enter the OTP")
             print("\n")
             otp=input()
             otp_char = []
             for x in otp:
               otp_char.append(x)


             #fills up the otp
             otp1 = driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/section[2]/section/div/div/div/input[1]")
             otp1.click()
             otp1.send_keys(otp_char[0])

             otp2 = driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/section[2]/section/div/div/div/input[2]")
             otp2.click()
             otp2.send_keys(otp_char[1])

             otp3 = driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/section[2]/section/div/div/div/input[3]")
             otp3.click()
             otp3.send_keys(otp_char[2])

             otp4 = driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/section[2]/section/div/div/div/input[4]")
             otp4.click()
             otp4.send_keys(otp_char[3])


             otp5 = driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/section[2]/section/div/div/div/input[5]")
             otp5.click()
             otp5.send_keys(otp_char[4])

             otp6 = driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/section[2]/section/div/div/div/input[6]")
             otp6.click()
             otp6.send_keys(otp_char[5])

             time.sleep(3)

             logc = driver.find_element_by_xpath("//span[contains(text(),'Sahil')]")
             login_status = logc.text

             print("\n"+f"Welcome to zomato {login_status}") # authenticates the user and welcome the user
             if "SAhil" in login_status:
                speak(" Login is succesfull ")

             speak(f"Welcome to Zomato {login_status}")
             speak(" Do you have something in mind to eat or do you want me to help you ")

             text = get_audio().lower()

             if "you" in text:
                 speak(" Sure")
                 speak(" Please tell the name of food items you want to eat")
                 #text = "I want to eat chicken"
                 text = get_audio().lower()
                 foo = text
                 search = driver.find_element_by_id("root")
                 search.click()
                 search.send_keys(text)
                 final_find = list(text.split(" "))


                 i =0
                 #food item determining algorithm
                 final_results = []
                 time.sleep(4)
                 while i<len(final_find):
                    str = final_find[i].capitalize()+" - Delivery"
                    try:
                     results  = driver.find_element_by_xpath("//*[contains(text(), '"+str+"')]")
                     fsearch = final_find[i]
                     final_results.append(results.text)
                    except:
                        pass
                    i+=1
                 time.sleep(2)
                 driver.find_element_by_xpath("//*[contains(text(), '"+final_results[0]+"')]").click()
                 time.sleep(4)
                 driver.find_element_by_xpath("//span[contains(text(), 'OKAY')]").click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/header/nav/ul[2]/li[1]/div/div/div[1]/div/div[4]/p[2]').click()
                 driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[5]/div/div/div[2]/div').click()
                 driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[5]/div/div/div[3]/div').click()
                 ##driver.find_element_by_xpath("//*[@id= \"root\"]/div/div[5]/div/div/div[3]/div").click()
                 #driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/section[2]/section/div/button[2]/span/span").click()

                 speak("Based on your needs these are the top 3 delivery restaurants near you.") #Finds the top 3 restaurants around the user
                 top_res = driver.find_elements_by_tag_name("p")
                 i=0
                 j=0
                 k=0
                 l=0
                 m=0
                 n=0
                 res_l=[]
                 temp_list = []
                 of = ["to", "OFF"]
                 print()
                 for x in top_res:
                     if i<=1:
                         i+=1

                     else:
                         try:
                             if float(x.text)<5:
                                 res_l.append(prev)
                         except:
                            prev = x.text
                            if "Promoted" in x.text:
                                     continue
                            if " min" in x.text:
                                l=1
                                m+=1
                            print(x.text)
                            if l ==1:
                                print("\n")
                                l=0
                            if m==3:
                                break

                 f_res_list = []
                 for x in res_l:
                      if "OFF" in x:
                          pass
                      else:
                        f_res_list.append(x)
                 print(f_res_list)
                 speak("From where do you want to order") # user can select the desired restaurant
                 text = input("Enter name: ")
                 #text = get_audio()
                 a = ""
                 order_list = list(text.split(" ",0))
                 for x in order_list:

                     if x in f_res_list:
                      print(x)
                      for rnames in text:
                          if rnames == " ":
                              a+= '-'
                          if rnames.isalnum():
                             a += rnames

                 b=a.lower()
                 z=0
                 scroll = ActionChains(driver)
                 #scroll.move_to_element(order_list[0]).perform()
                 try:

                        cl = driver.find_element_by_xpath('//a[contains(@href, "%s")]' % b)
                        cl.click()
                 except:
                       pass

                 speak(f"These are the top recommended orders from {a}")
                 speak("Do you want me to include meals")
                 #text = "no"
                 text = get_audio().lower()
                 rec_items = driver.find_elements_by_tag_name("h4")
                 additional = 0
                 add_list = []
                 j=1
                 speak(f"These are the {fsearch} available at {a}")
                 #looks for the food items
                 print("\n\n-------------------------------")
                 for x in rec_items:
                          c = x.text
                          d = c.lower()
                          if fsearch in d:
                             if "meal" in d:
                                 continue
                             else:
                               add_list.append(x.text.split(" ",0))
                               print(f"{j}) "+x.text)
                               print()
                               j+=1

                 print("-------------------------------")
                 speak("please tell the item number of the food item you want to order")
                 #text = get_audio().lower()
                 text = input("tell the item number: ")
                 count = int(text)
                 j=0


                 fooitem = add_list[count-1]
                 driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/button/span').click()
                 inpt = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/section[4]/section/section[2]/div[2]/section/section/input')
                 inpt.click()
                 time.sleep(1)
                 inpt.send_keys(fooitem)
                 time.sleep(2)
                 #driver.find_element_by_xpath('//*[@id="root"]/div[2]/main/div/section[4]/section/section[2]/section[2]/h4').click()
                 Add = driver.find_elements_by_xpath("//span[contains(text(), 'Add')]")
                 j=0
                 for i in Add:
                     if j ==1:
                         try:
                           driver.execute_script("arguments[0].click();", WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/section[4]/section/section[2]/section[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div'))))
                           break
                         except:
                             try:
                                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/section[4]/section/section[2]/section[2]/div[3]/div/div/div/div[2]/div/div[2]/div/span'))))
                                break
                             except:
                                 print("Item not found")
                                 break
                     j+=1

                 try:
                     driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Add to order')]"))))
                 except:
                     pass
                 driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/section/div[2]/div/div[2]/button/span'))))
                 driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/button[1]/span'))))
                 #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                 time.sleep(3)
                 iframe = driver.find_element_by_xpath('//*[@id="payment_widget"]')
                 driver.switch_to.frame(iframe) # switches the iframe
                 cash = driver.find_element_by_xpath("//h5[contains(text(), 'Cash')]").click()
                 driver.execute_script("arguments[0].click();", WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, "//h5[contains(text(), 'Cash')]")))) #//*[@id="app"]/div[2]/section/div[6]/div/section  /html/body/div/div[2]/section/div[6]/div/section
                 driver.switch_to.default_content() #switches to default iframe

                 #driver.execute_script("arguments[0].click();", WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/section/div[6]/div')))) #//*[@id="app"]/div[2]/section/div[6]/div/section  /html/body/div/div[2]/section/div[6]/div/section






          elif "swiggy" in text:
             driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
             driver.get("https://www.swiggy.com")
             Login = driver.find_element_by_link_text("Login")
             action = ActionChains(driver)
             action.click(on_element = Login)
             action.perform()
             number = driver.find_element_by_id("mobile")
             number.send_keys("")
             #Login2 = driver.find_element_by_link_text("Login")
             driver.find_element_by_class_name("a-ayg").click()
             speak(" Please speak the OTP number")
             text = get_audio().lower()

             otp = driver.find_element_by_id("otp")
             otp.send_keys(text.replace(" ", ""))
             driver.find_element_by_class_name("a-ayg").click()

          elif "foodpanda" in text:
             webbrowser.open('https://www.foodpanda.com')





elif "what is your name" in text:
    speak("My name is AI")
