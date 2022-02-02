
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint
import pickle
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from tkinter import *
import tkinter as tk
from tkinter import messagebox,filedialog
from tkinter import scrolledtext, Listbox

def sleep():
    time.sleep(randint(1, 5))



#Open Browser




#Removes navigator.webdriver flag

# For older ChromeDriver under version 79.0.3945.16

#option.add_argument("user-data-dir=selenium")
#For ChromeDriver version 79.0.3945.16 or over
"""option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("window-size=1280,800")
#option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)"""

def interface():
    
    def Ok(e1,description,ep,images):
        
        titre = e1.get()
        description = description.get("1.0", tk.END)
        prix = ep.get()
        if(titre != "" and description != "") :
            file1 = open('logs.txt', 'r')
            Lines = file1.readlines()
            for line in Lines:
                proxy_ip_port = 'fr.smartproxy.com:'+str(40000+randint(1, 500))
                proxy = Proxy()
                proxy.proxy_type = ProxyType.MANUAL
                proxy.http_proxy = proxy_ip_port
                proxy.ssl_proxy = proxy_ip_port
                options = webdriver.ChromeOptions()
                
                proxy.add_to_capabilities(capabilities)
                EMAIL,PASSWORD,city=(line.strip().split(':'))
                driver = webdriver.Chrome(desired_capabilities=capabilities,options=options)
                
                
                

                
                    
                login(driver,EMAIL,PASSWORD)
                    
                    
                while True:
                        try:
                            abtn = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div/header/div[1]/nav[2]/div[1]/a[2]')))
                            if 'pro' in driver.current_url:
                                
                                post_pro(city,driver,titre,description,prix,images)

                            else:
                                post_normal(city,driver,titre,description,prix,images)
                            driver.close()
                            break
                        except Exception as e:
                            print(e)
                            input(' ')
                            continue
                 

        else :
            
            messagebox.showinfo("", "Blank Not allowed")

    def to_del():
            file1 = open('logs.txt', 'r')
            Lines = file1.readlines()
            for line in Lines:
                proxy_ip_port = 'fr.smartproxy.com:'+str(40000+randint(1, 500))
                proxy = Proxy()
                proxy.proxy_type = ProxyType.MANUAL
                proxy.http_proxy = proxy_ip_port
                proxy.ssl_proxy = proxy_ip_port
                options = webdriver.ChromeOptions()
                
                #options.add_argument('--user-data-dir=C:\\Users\\Public\\python\\lbc\\selenium')
                options.page_load_strategy='normal'
                capabilities = webdriver.DesiredCapabilities.CHROME
                proxy.add_to_capabilities(capabilities)
                EMAIL,PASSWORD,city=(line.strip().split(':'))
                driver = webdriver.Chrome(desired_capabilities=capabilities,options=options)
               
                del_an(login(driver,EMAIL,PASSWORD))
        
        
        
    global root
    root = tk.Tk()
    root.title("LBC")
    root.geometry("700x600")
    global e1
    global e2
    global group
    Label(root, text="Titre").place(x=10, y=10)

    Label(root, text="Description").place(x=10, y=50)


    e1 = Entry(root,width=50)
    e1.place(x=150, y=10)

    



    description = scrolledtext.ScrolledText(root, 
                                      wrap = tk.WORD, 
                                      width = 60, 
                                      height = 5, )

  
    #text_area.grid(column = 0, pady = 10, padx = 10)

    description.place(x=150,y=50)
    images =[]
    
    def populatebox():
        root.filename = filedialog.askopenfilenames(title="Select A File")
        for file in root.filename:
            
            listBox.insert("end", file)
            images.append(file)
    listBox = Listbox(root,width = 80, 
                                      height = 8)
    listBox.pack()
    listBox.place(x=150,y=250)
    Label(root, text="Prix").place(x=10, y=195)
    ep = Entry(root,width=50)
    ep.place(x=150, y=200)
    
    
   
    btn = Button(root, text="Ajouter image", command = lambda: populatebox()).place(x=300, y=400)
    #btn.pack()
    Button(root, text="Login", command= lambda: Ok(e1,description,ep,images) ,height = 2, width = 13).place(x=270, y=500)
    Button(root, text="Supprimer les annonces", command= lambda: to_del() ,height = 2, width = 20).place(x=400, y=500)

    root.mainloop()


def del_an(driver):
    #https://www.leboncoin.fr/compte/pro/mon-activite
    abtn = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div/header/div[1]/nav[2]/div[1]/a[2]')))
            
    sleep()
    driver.get('https://www.leboncoin.fr/compte/pro/mon-activite')
    sleep()
    #
    try : 
        ele = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root-portal"]/div/div[2]/button')))
                

        ActionChains(driver).click(ele).perform()
        sleep()
    except:
        pass
    ele = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ads-widget"]/div/div/div[3]/div[1]/div/div/div/label/span/input')))
            
    sleep()
    ActionChains(driver).click(ele).perform()
    sleep()
    ele = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ads-widget"]/div/div/div[3]/div[1]/div/div/div/div[2]/button[1]')))
            
    sleep()
    ActionChains(driver).click(ele).perform()
    sleep()
    ele = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mainContent"]/div/div/form/div/button')))
            
    sleep()
    ActionChains(driver).click(ele).perform()
    input('')
def login(driver,email,password):
    while True:
        driver.get("https://www.leboncoin.fr/")  
        try:
            
            try:
                #time.sleep(30)
            #didomi-notice-agree-button
                time.sleep(5)

                cookies = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))).click()
                ActionChains(driver).click(cookies).perform()
                #pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))
            except Exception as e:
                pass
            #//*[@id="container"]/div[2]/div/div[1]/div/header/div[1]/nav[2]/div[2]/button
            sleep()
            login=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[2]/div/div[1]/div/header/div[1]/nav[2]/div[2]/button')))
            ActionChains(driver).click(login).perform()
            time.sleep(5)

            break
        except Exception as e:
            print("Home page",e)
            input('')
            continue

    while True:
        try:
            email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
            sleep()
            password = driver.find_element(By.ID,"password").send_keys(password)
            btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/div/div[2]/form/div[5]/button')))
            sleep()
            ActionChains(driver).click(btn).perform()
            sleep()
            break
        
        except Exception as e:
            print("Somthing went wrong ! go to login page and tape enter to restart the login.",e)
            input('')
            continue
    return driver


"""

       ##################### CONTACT ME FOR FULL CODE on benseryamohammed1@gmail.com

"""
