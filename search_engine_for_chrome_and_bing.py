import selenium.webdriver as webdrivernasir
from webdriver_manager.chrome import ChromeDriverManager


def get_results_Bing(search_term):
    url = "https://www.bing.com"
    browser = webdrivernasir.Chrome(ChromeDriverManager().install())
    browser.get(url)
    search_box = browser.find_element_by_id("sb_form_q") #ID arama moturuna göre değişebilitor
    search_box.send_keys(search_term)
    search_box.submit()    
    
    try:
        links = browser.find_elements_by_xpath("//ol[@id='b_results']//h2//a") #Ol tagındaki class adı değişebiliyor search engine
    except:
        links = browser.find_elements_by_xpath("//h2//a")

    
    results = []
    
    for link in links:
        href = link.get_attribute("href")        
        print(href)
        results.append(href)
    browser.close()
    
    f = open("data_bing.txt", "w+")
        
    for i in range(len(results)):
        f.write("{} ".format(results[i]))
        
    f.close()
    
    return results

