#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-    
#作者 ：    'keng'
#时间 ：    '21:18'
#描述 ：     A kinder pythoner

import time
from selenium import webdriver
import random
class pingjiao(object):
    def __init__(self):
        self.url = 'https://urp.tfswufe.edu.cn/cas/login?service=http%3A%2F%2Fportal.tfswufe.edu.cn%2Fweb%2Fguest'
        self.golal_url = 'http://jwc.tfswufe.edu.cn/eams/quality/stdEvaluate!finishAnswer.action'
        self.right_url = 'http://portal.tfswufe.edu.cn/web/guest/243/'
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(self.url)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(input('输入你的账号：'.strip()))
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(input('输入你的密码：'.strip()))
        self.driver.find_element_by_xpath('//*[@id="authcode"]').send_keys(
            input('请输入验证码:'))
        self.driver.find_element_by_xpath('//*[@id="fm1"]/div[1]/section[2]/input[4]').click()
        time.sleep(1)
        if self.driver.current_url == self.right_url:
            self.startpost()
        else:
            self.login()

    def startpost(self):
        self.driver.get('http://jwc.tfswufe.edu.cn/eams/quality/stdEvaluate.action')
        #post_node = self.driver.find_elements_by_xpath('//div[@class="grid"]//tbody/tr')
        post_url = self.driver.find_elements_by_xpath('//div[@class="grid"]//tbody/tr/td[6]/a')
        urls = []
        for i in post_url:
            urls.append(i.get_attribute('href'))
            print(i)

        for url in urls:
            try:
                self.driver.get(url)
                time.sleep(1)
                self.radom_post()

            except:
                print('有错啊兄弟')

    def radom_post(self):
        print('评教已经成功，马上开始下一个哟')
        test_post = self.driver.find_elements_by_xpath('//*[@id="app-main"]/div[2]/div/div')
        for post in test_post[1:]:
            post.find_element_by_xpath('./ul/li[{0}]/input'.format(random.randint(1, 3))).click()

        self.driver.find_element_by_xpath('//*[@id="sub"]').click()
        self.driver.switch_to_alert().accept()






if __name__ == '__main__':
    pingjiao = pingjiao()
    pingjiao.login()