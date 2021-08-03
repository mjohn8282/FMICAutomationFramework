import inspect

import requests

from Utilities.CustomLogger import logs


class Homepage:



    def __init__(self, driver):
        self.driver = driver
        # self.RTEstimatorurl = 'https://fmicdev.dat.com/Web/GlobalPages/RTEstimator.aspx'

    # def RTEstimator(self):
    #     self.driver.get('https://fmicdev.dat.com/Web/GlobalPages/RTEstimator.aspx')

    def CheckHomepage_links(self):
        logs.loggen().info("starting " + inspect.stack()[0][3] + "")
        links = self.driver.find_elements_by_xpath(".//a")
        for i in links:
            href = str(i.get_attribute('href'))
            if href.__contains__('Logoff.aspx') or href.__contains__(str(None)):
                continue
            else:
                status = requests.get(href).status_code
                logs.loggen().info(href + " Status code " + str(status))
