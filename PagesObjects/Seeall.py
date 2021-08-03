import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Utilities.CustomLogger import logs


class seeall:
    seeall_link_xpath = '//div[@id="divHomeMenu"]/div[@class="col-sm menu-margin"]/ul/li[8]/a'
    all_links_MMI_xpath = "//div[@id='divMyMarketIntelligence'] //a"
    Survey_report_xpath = "//div[@id='divMyMarketIntelligence']/div[1]/div[3]/div/img[2]"
    links_under_survey_reports_xpath = "//div[@id='myMarketIntelligencePopupBody'] //a"

    def __init__(self, driver):
        self.driver = driver

    def checllalllinksin_Seeall(self):

        statuscodes = {}

        self.driver.find_element_by_xpath(seeall.seeall_link_xpath).click()
        links = self.driver.find_elements_by_xpath(seeall.all_links_MMI_xpath)

        for i in links:
            href = str(i.get_attribute('href'))
            if href.__contains__('Logoff.aspx') or href.__contains__(str(None)):
                continue
            else:
                status = requests.get(href).status_code
                logs.loggen().info(href + " Status code " + str(status))
                statuscodes[href] = status
                # assert (status == 200),f"The status code for {href} is {status}"
                # assert (status == 200), take_screenshot(self.driver,'checllalllinksin_Seeall')

        surveysandreports = self.driver.find_element_by_xpath(seeall.Survey_report_xpath).click()

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                       seeall.links_under_survey_reports_xpath)))

        surveyandreportslinks = self.driver.find_elements_by_xpath(seeall.links_under_survey_reports_xpath)

        for i in surveyandreportslinks:
            href = str(i.get_attribute('href'))
            if href.__contains__('Logoff.aspx') or href.__contains__(str(None)):
                continue
            else:
                status = requests.get(href).status_code
                logs.loggen().info(href + " Status code " + str(status))
                statuscodes[href] = status
                # assert (status == 200), f"The status code for {href} is {status}"

        return statuscodes
