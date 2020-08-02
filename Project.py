from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class Project:

    def __init__(self, webdriver, project_name = 'default'):
        self.driver = webdriver
        self.project_name = project_name
        self.hamburger_button = False

    def create_project(self):
        # Click hamburger button
        if self.hamburger_button == False:
            self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Change the current view']").click()
            time.sleep(5)

        # Click create project
        self.driver.find_element_by_id('com.todoist:id/add').click()
        time.sleep(2)

        # Create project name
        project_name_element = self.driver.find_element_by_id('com.todoist:id/name')
        time.sleep(1)
        project_name_element.send_keys(self.project_name)

        # Click enter button, the project is created
        self.driver.execute_script('mobile:performEditorAction', {'action': 'done'})
        print('Create project completed')

    def open_project(self):
        # Click hamburger button
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Change the current view']").click()
        self.hamburger_button = True
        time.sleep(5)

        #Open an existing project
        self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Expand/collapse']").click()
        time.sleep(5)
        project_name_path="//android.widget.TextView[@content-desc='{}']".format(self.project_name)
        #Known bug: failed to check if the project name exists
        try:
            project_name_element = self.driver.find_element_by_xpath(project_name_path)
            time.sleep(2)
            project_name_element.click()
            time.sleep(2)
        except NoSuchElementException:
            print('Project not exist')
            time.sleep(2)
            self.create_project()
        except:
            return

    # To do check if the project has been created
    def verify_project_created(self):
        pass
