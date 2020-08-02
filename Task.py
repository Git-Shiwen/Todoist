from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class Task:

    def __init__(self, webdriver, project_name = None, task_name = 'default'):
        self.driver = webdriver
        self.project_name = project_name
        self.task_name = task_name

    def create_task(self):
        # Click create task
        time.sleep(2)
        self.driver.find_element_by_id('com.todoist:id/fab').click()
        time.sleep(5)

        # #Create task name
        task_name_element = self.driver.find_element_by_id('android:id/message')
        time.sleep(1)
        task_name_element.send_keys(self.task_name)
        time.sleep(3)
        self.driver.execute_script('mobile:performEditorAction', {'action': 'done'})
        time.sleep(3)
        self.driver.find_element_by_id('android:id/button1').click()

        print('Create task completed')

    #To do, check if the task has been created
    def verify_task_created(self):
        pass
