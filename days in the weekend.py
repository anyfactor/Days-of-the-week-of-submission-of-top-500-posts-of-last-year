from selenium import webdriver

browser= webdriver.Chrome(executable_path=r"")
browser.get('https://old.reddit.com/r/all/top/?sort=top&t=year')

def scraper(pages):
    for i in range(pages):
        time = browser.find_elements_by_tag_name('time')
        for i in (time):
            print(i.get_attribute("title")[:3])
           
        next_button= browser.find_element_by_class_name('next-button')
        next_button.click()

scraper(20)
