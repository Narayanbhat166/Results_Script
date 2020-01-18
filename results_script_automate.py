from selenium import webdriver
import time
browser = webdriver.Chrome(r'C:\Users\Narayan Bhat\Downloads\chromedriver_win32\chromedriver')
browser.get('http://www.results.jssstuniv.in') 
prefix = "01JST18CS"
time.sleep(10)

for i in range(1,10):
    elem = browser.find_element_by_id('USN')
    usn = prefix + f"{i:03d}"
    elem.send_keys(usn) 
    button = browser.find_element_by_class_name('button2')
    button.click() 
    print("waiting for 2 seconds, check your result")
    try:
        maths = browser.find_element_by_id('cred1')
    except:
        print("Failed")  
    else:
        maths.send_keys("4")
    try:
        dsd = browser.find_element_by_id('cred2')
    except:
        print("Failed")
    else:
        dsd.send_keys("3")
    try:
        toc = browser.find_element_by_id('cred3')
    except: 
        print("Failed")
    else:
        toc.send_keys("4")
    try:
        dms = browser.find_element_by_id('cred4')
    except:
        print("Failed")
    else:
        dms.send_keys("3")
    try:
        data_structures = browser.find_element_by_id('cred5')
    except:
        print("Failed")
    else:
        data_structures.send_keys("4")
    try:
        java = browser.find_element_by_id('cred6')
    except:
        print("Failed")
    else:
        java.send_keys("4")
    try:
        ds_lab = browser.find_element_by_id('cred7')
    except:
        print("Failed")
    else:
        ds_lab.send_keys("1.5")
    try:
        dsd_lab = browser.find_element_by_id('cred8')
    except:
        print("Failed")
    else:
        dsd_lab.send_keys("1.5")
    button = browser.find_element_by_class_name('button')
    button.click()
    time.sleep(2) #wait for 3 seconds
    print("Waited for 3 seconds")
    button = browser.find_element_by_class_name('button2')
    button.click() 
print("done")