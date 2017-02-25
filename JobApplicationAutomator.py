from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://h30631.www3.hp.com/search-jobs")

try:
    job_category = Select(driver.find_element_by_name('ac'))
    country = Select(driver.find_element_by_name('Country'))
    state = Select(driver.find_element_by_name('State'))
    city = Select(driver.find_element_by_name('City'))

    job_category.select_by_visible_text('Information Technology')
    country.select_by_visible_text('United States')
    state.select_by_visible_text('Texas')
    city.select_by_visible_text('Austin')
    driver.find_element_by_xpath("//button[text()='Search']").click()

    search_results = driver.find_elements_by_xpath('//*[@id="search-results-list"]/ul/li')
    number_of_jobs = len(search_results)
    print number_of_jobs

    print "Job Description \t Job Location \n"
    for i in range(1, number_of_jobs):
        job_description = driver.find_element_by_xpath('//*[@id="search-results-list"]/ul/li[' + str(i) + ']/a/h2').text
        job_location = driver.find_element_by_xpath('//*[@id="search-results-list"]/ul/li[' + str(i) + ']/span').text
        print job_description + '\t' + job_location

except Exception, e:
    print e
finally:
    driver.close()
