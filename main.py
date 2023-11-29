
import time
# 导入selenium包
from selenium import webdriver
# Press the green button in the gutter to run the script.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
# 打开Firefox浏览器
opts=webdriver.ChromeOptions()
# opts._binary_location="/Users/huwenjun1/PycharmProjects/gov_pick/driver/chromedriver"
browser = webdriver.Chrome(opts)

def GetElementWaitByXPath(xPath):

    return WebDriverWait(browser,100,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,xPath)))

def getBuyBtn():
    # btn=None
    xPath="/html/body/div/div[1]/div[5]/div[3]/div[1]/div[1]/div[3]/a"
    return GetElementWaitByXPath(xPath)


def getToLoginBtn():
    xPath="/html/body/div[2]/div/div/div[3]/button"
    return GetElementWaitByXPath(xPath)

def getToFarenLoginBtn():
    xPath="/html/body/div/div[1]/div/div[2]/div/form/div/div[1]/div/div/div/div/h2[2]/div[1]"
    return GetElementWaitByXPath(xPath)



def getFaRenLoginPageBtn():
    xPath="/html/body/div/div[3]/form/div/div[2]/div[1]/a[2]"
    return GetElementWaitByXPath(xPath)


def getFaRenUserName():
    xPath="/html/body/div/div[3]/form/div/div[2]/div[3]/div[1]/div[1]/input"
    return GetElementWaitByXPath(xPath)

def getFaRenPwd():
    xPath="/html/body/div/div[3]/form/div/div[2]/div[3]/div[1]/div[5]/input"
    return GetElementWaitByXPath(xPath)



def getFaRenLoginBtn():
    xPath="/html/body/div/div[3]/form/div/div[2]/div[3]/div[1]/div[10]"
    return GetElementWaitByXPath(xPath)


if __name__ == '__main__':
    browser.get("https://yzzt.wuhan.gov.cn/fwq/front/#/produce-detail?id=13")
    btn=getBuyBtn()
    btn.click()
    btn=getToLoginBtn()
    btn.click()
    btn=getToFarenLoginBtn()
    btn.click()
    btn_faRenLoginPage=getFaRenLoginPageBtn()
    btn_faRenLoginPage.click()
    txt_username=getFaRenUserName()
    txt_username.send_keys("91420102MA4L0ARB20")
    txt_pwd=getFaRenPwd()
    txt_pwd.send_keys("Ab123456")
    btn_faRenLogin=getFaRenLoginBtn()
    btn_faRenLogin.click()
    while True:
        if browser.current_url=="https://yzzt.wuhan.gov.cn/fwq/front/#/home":
            ele=GetElementWaitByXPath("/html/body/div/div[1]/div[5]/div[2]/div[1]/div[2]/div/div[1]")
            if ele.text.startswith("欢迎"):
                break
        time.sleep(1)
    # 停留三秒
    # 关闭浏览器
    # browser.quit()
    browser.get("https://yzzt.wuhan.gov.cn/fwq/front/#/produce-detail?id=13")
    while True:
        btn=getBuyBtn()
        btn.click()
        time.sleep(2)
        browser.refresh()


