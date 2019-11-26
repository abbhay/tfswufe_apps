#作者 ：    'Abhay'
#时间 ：    '2019-06-09'
#描述 ：     A kinder pythoner
import time
import random
from selenium import webdriver

class JIXUN(object):
    def __init__(self):
        self.zhanghao = input('请输入账号:').strip()
        self.password = input('请输入密码:').strip()
        self.url = 'http://tf-swufe.careersky.cn/jixun'
        self.right_url = 'http://tf-swufe.careersky.cn/jixun/Account/default'
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(self.url)
        self.driver.find_element_by_xpath('//*[@id="apps"]/div/div[1]/div[2]/form/p[1]/input').send_keys(self.zhanghao)
        self.driver.find_element_by_xpath('//*[@id="apps"]/div/div[1]/div[2]/form/p[2]/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="apps"]/div/div[1]/div[2]/form/p[3]/input').send_keys(input('请输入验证码:'))
        self.driver.find_element_by_xpath('//*[@id="apps"]/div/div[1]/div[2]/form/p[4]/a[1]').click()

        if self.driver.current_url == self.right_url:
            self.xianzhuang()
        else:
            self.login()

    def xianzhuang(self):
        self.driver.get('http://tfswufe.careersky.cn/jixun/Begin/Begin')
        try:
            self.driver.find_element_by_xpath("//*[text()='开始答题']").click()
            for i in self.driver.find_elements_by_xpath('//td[2]/div'):
                i.find_element_by_xpath('./label[{0}]'.format(random.randint(1,4))).click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[4]/div/a').click()
            print('已完成')
        except:
            print('现状评估已经刷完')
        finally:
            self.zhiyexingqu()

    def zhiyexingqu(self):
            self.driver.get('http://tfswufe.careersky.cn/jixun/Interest/Interest')
            try:
                self.driver.find_element_by_xpath("//*[text()='开始答题']").click()
                if  self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[4]/div/a'):
                    for cishu in range(7):

                        for i in self.driver.find_elements_by_xpath('//td[2]/div'):
                            i.find_element_by_xpath('./label[{0}]'.format(random.randint(1, 2))).click()
                        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[4]/div/a').click()

                print('已完成')
            except :
                print('职业兴趣已经刷完')
            finally:
               self.zhiyexinge()

    def zhiyexinge(self):
        self.driver.get('http://tfswufe.careersky.cn/jixun/Character/Character')
        try:
            self.driver.find_element_by_xpath("//*[text()='开始答题']").click()
            for cishu in range(7):
                for i in self.driver.find_elements_by_xpath('//dd/div'):
                    i.find_element_by_xpath('../label[{0}]'.format(random.randint(1, 2))).click()
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[4]/div/a').click()

            print('已完成')
        except:
            print('职业性格已经刷完')
        finally:
            self.zhiyejiazhi()

    def zhiyejiazhi(self):
        self.driver.get('http://tfswufe.careersky.cn/jixun/Value/Value')
        try:
            self.driver.find_element_by_xpath("//*[text()='开始答题']").click()
            for cishu in range(3):
                for i in self.driver.find_elements_by_xpath('//li/div'):
                    i.find_element_by_xpath('./label[{0}]'.format(random.randint(1, 2))).click()
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[4]/div/a').click()
                self.driver.find_element_by_xpath('div/div[1]/div[1]/span[1]/input').click()
            self.driver.find_element_by_xpath('div/div[3]/div[1]/span[1]/input').click()
            self.driver.find_element_by_xpath('div/div[2]/div[1]/span[1]/input').click()
            self.driver.find_element_by_xpath('div/div[1]/div[1]/span[1]/input').click()

            print('已完成')
        except:
            print('职业价值观已经刷完')
        finally:
           self.zhiyefengge()

    def zhiyefengge(self):
        self.driver.get('http://tfswufe.careersky.cn/jixun/Learn/Learn')
        try:
            self.driver.find_element_by_xpath("//*[text()='开始答题']").click()
            for cishu in range(6):
                for i in self.driver.find_elements_by_xpath('//td[2]/div'):
                    i.find_element_by_xpath('./label[{0}]'.format(random.randint(1, 2))).click()
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[4]/div/a').click()



            print('已完成')
        except:
            print('学习风格已经刷完')
        finally:
            self.zhiyejineng()

    def zhiyejineng(self):
        self.driver.get('http://tfswufe.careersky.cn/jixun/Skill/Skill')
        try:
            self.driver.find_element_by_xpath("//*[text()='开始答题']").click()
            for cishu1 in random.sample(range(1,36),5):
                self.driver.find_element_by_xpath('//ul/li[{0}]/div[3]'.format(cishu1)).click()
            self.driver.find_element_by_xpath("//*[text()='下一步']").click()
            list_choice = [i for i in range(1,6)]
            random.shuffle(list_choice)
            for i in list_choice:

                self.driver.find_element_by_xpath('//ul/li[{0}]/div[3]'.format(i)).click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[4]/div[1]/a').click()

            for cishu2 in random.sample(range(1, 31), 3):

                self.driver.find_element_by_xpath('//ul/li[{0}]/div[3]'.format(cishu2)).click()
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[4]/div[1]/a').click()
            print('已完成')
        except:
            print('职业技能已经刷完')
        finally:
            pass

    def cutpingmu(self):
        self.driver.execute_script('window.scrollTo(0,10000)')



if __name__ == '__main__':
    test = JIXUN()
    test.login()



