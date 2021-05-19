from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os, random, sys, time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(r'.\chromedriver.exe',chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://passport2.chaoxing.com')
driver.find_element_by_name("uname").send_keys("15571071099")
driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys("szy666")
input('请输入验证码和登录')                                                            

# dataList = driver.find_elements_by_xpath("//em[@class='orange']")
# dataList[0].click()    

def level_1st():
    driver.switch_to.frame("frame_content")
    # 进入首页，开始选择课程
    time.sleep(1)
    #引号内添加要刷的相应那门课程的xpath
    c_click = driver.find_element_by_xpath('//a[@title="会计学原理"]')
    c_click.click()

    # li_click = driver.find_element_by_xpath("")
    # driver.execute_script("window.scrollT0(0,3000)")
    # driver.back()#向后退 前进是forward（）
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])


# 判断是否有通知
def if_message():
    time.sleep(1)
    judge = 1
    while judge:
        try:
            close_widow = driver.find_element_by_xpath("/html/body/div[9]/div/a")
            close_widow.click()
            print(111)
        except:
            print("无弹窗")


# 进入视频并且播放
def into_vedio_window():
    time.sleep(1)
    driver.find_elements_by_xpath("//em[@class='orange']")[0].click()
    time.sleep(2)


# 播放课
def play_vedio():
    time.sleep(1)
    driver.switch_to.frame("iframe")
    # 这里有一个嵌套iframe
    driver.switch_to.frame(0)
    begin_vedio = driver.find_element_by_xpath("//*[@id='video']/button").click()
    time.sleep(3)
    print("课程已经开始播放")


# 判断是否有答题框，其实这个逻辑挺简单的，只不过我不知道怎么触发答题框，
# 选择题的话依次选择ABCD直到对了就可以
def if_question():
    pass


# 判断视频是否完成
def if_vedio_finished():
    time.sleep(1)
    vedio_start_time =''
    vedio_end_time= '1'
    # data = driver.find_element_by_xpath("//span[@class='vjs-current-time-display']").get_attribute(
    # "textContent").split(":")
    # vedio_start_time = int(data[0]) * 60+ int(data[1])
    # data = driver.find_element_by_xpath("//span[@class='vjs-duration-display']").get_attribute(
    #     'textContent').split(':')
    # vedio_end_time = int(data[0]) * 60+ int(data[1])
    while True:
        try:
            if (vedio_start_time == vedio_end_time):
                return 
            else:
                vedio_start_time = driver.find_element_by_xpath("//span[@class='vjs-current-time-display']").get_attribute(
    "textContent")
                vedio_end_time = driver.find_element_by_xpath("//span[@class='vjs-duration-display']").get_attribute(
        'textContent')
                print("{}/{}".format(vedio_start_time, vedio_end_time)) 

            time.sleep(1)  # 每10秒检测一次视频是否完成
        except:
            pass



# 判断有第二节课吗有就播放
def if_have_2nd_class(vedio_start_time, vedio_end_time):
    if vedio_start_time == vedio_end_time:
        try:
            # 开始播放第二个视频
            driver.switch_to.default_content()
            driver.switch_to.frame("iframe")
            driver.switch_to.frame(1)
            driver.find_element_by_xpath("//*[@id='video']/button").click()
            time.sleep(3)

        except:
            pass
            print("已结束")


def start_next(vedio_start_time, vedio_end_time):
    if vedio_start_time == vedio_end_time:
        try:
            driver.switch_to.default_content()
            print("开始点下一页")
            driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[8]").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[4]").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[6]").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[8]").click()
            time.sleep(0.5)
        except:
            print("开始点没有小节的下一页")
            driver.switch_to.default_content()
            driver.find_element_by_xpath("//*[@id='mainid']/div[1]/div[2]").click()
            time.sleep(1)
            pass


if __name__ == '__main__':
    driver.set_window_size(1280,200)
    level_1st()
    # if_message()
    into_vedio_window()
    for each in driver.find_elements_by_xpath("//span[@class='roundpoint  orange01 jobCount']"):
        each.click()
        play_vedio()
        if_vedio_finished()
        # while time_tuple[0] != time_tuple[1]:
        #     time_tuple = if_vedio_finished()
        #     try:
        #         if_have_2nd_class(time_tuple[0], time_tuple[1])
        #         if time_tuple[0] == time_tuple[1]:
        #             print("开始测试第二节课时间")
        #             time_tuple_2 = if_vedio_finished()
        #             while time_tuple_2[0] != time_tuple_2[1]:
        #                 time_tuple_2 = if_vedio_finished()
        #                 start_next(time_tuple_2[0], time_tuple_2[1])
        #     except:
        #         start_next(time_tuple[0], time_tuple[1])