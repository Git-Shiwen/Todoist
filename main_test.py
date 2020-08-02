from appium import webdriver
from Project import Project
from Task import Task
import time

def login(email_address, email_pwd):
    #Choose login using email
    driver.find_element_by_id('com.todoist:id/btn_welcome_email').click()
    driver.implicitly_wait(10)

    # Click Cancel button
    driver.find_element_by_id('com.google.android.gms:id/cancel').click()
    driver.implicitly_wait(10)

    # input email address
    email_element = driver.find_element_by_id('com.todoist:id/email_exists_input')
    time.sleep(1)
    driver.set_value(email_element, email_address)

    # Continue click button
    driver.find_element_by_id('com.todoist:id/btn_continue_with_email').click()
    time.sleep(3)

    # Input passowrd
    email_pwd_element = driver.find_element_by_id('com.todoist:id/log_in_password')
    #driver.implicitly_wait(1)
    driver.set_value(email_pwd_element, email_pwd)

    # Login
    driver.find_element_by_id('com.todoist:id/btn_log_in').click()
    time.sleep(5)

def scenario_create_prject(project_name):
    #Create project
    project = Project(driver, project_name)
    project.create_project()
    time.sleep(5)

    #Verify if the project is created
    project.verify_project_created()

def scenario_reopen_task(project_name, task_name):
    task_project = Project(driver, project_name)
    task_project.open_project()

    task = Task(driver, project_name, task_name)
    task.create_task()

    #Verify if the task is created
    task.verify_task_created()

def main():
    print('*'*50)
    print('    Testing scenario: 1) Create Project (P)')
    print('                      2) Reopen Task (T)')
    print('*'*50)
    testing_scenario = input('Please input single letter P or T? ').upper()

    #Choose testing scenarios
    if testing_scenario == 'P':
        print('Test "Create Project"')
    elif testing_scenario == 'T':
        print('Test "Reopen Task"')
    else:
        print('Wrong input')
        return

    desired_cap = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "app": "C:\\Users\\wshiwen\\Downloads\\com.todoist_15.8.3_7434.apk",
        "appActivity": "com.todoist.activity.HomeActivity",
        "appPackage": "com.todoist"
    }

    #create the driver instance
    global driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
    time.sleep(5)

    #Login
    email_address = 'auto_testing@yahoo.com'
    email_pwd = 'testing123456'
    login(email_address, email_pwd)

    #Choose testing scenarios
    if testing_scenario == 'P':
        project_name = 'test_project'
        scenario_create_prject(project_name)
    elif testing_scenario == 'T':
        project_name = 'test_project'
        task_name = 'test_task'
        scenario_reopen_task(project_name, task_name)


if __name__ == '__main__':
    main()
