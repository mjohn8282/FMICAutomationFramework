import inspect
from PagesObjects.Loginpage import Login
from Utilities.CustomLogger import logs


def login(setup):
    logs.loggen().info("************ Verifying Homepage Title ***********")
    logs.loggen().info("************ Verifying " + inspect.stack()[0][3] + "***********")
    driver = setup
    driver.get("https://benchmarktest.dat.com/")
    lp = Login(driver)
    lp.setUsername("john.moses@dat.com")
    lp.setPassword("Dat@1794")
    lp.clickLoginbtn()
