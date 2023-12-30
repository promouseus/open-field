from enum import unique
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import json


firefox_options = webdriver.FirefoxOptions()
#firefox_options.headless = True
firefox_options.set_preference('layout.css.devPixelsPerPx','2.0') # 2.0this sets high resolution, better OCR

driver = webdriver.Remote(
    command_executor='http://selenium:4441',
    options=firefox_options
)
driver.set_window_size(1920, 3240) # Headless / fullscreen

#cat succubusSiteMapProducts.xml|grep '<loc>'|awk -F'<loc>' '{print $2}'|awk -F '</loc>' '{print $1}'



filepath = 'succubusProductScrape.txt'
with open(filepath) as fp:
   line = fp.readline()
   while line:
        #print(line.strip())
        path_file='./image_headless.png'
        path_url=line

        print("Scraping: ", path_url)

        driver.get(path_url)
        time.sleep(2)
        driver.save_screenshot(path_file)
        time.sleep(1)

        #curl -T image2_headless.png http://localhost:9998/tika --header "Accept: application/json" --header "Content-type: image/png" --header ": nld"|json_pp

        print("OCR on: ", path_url)

        tikaurl='http://tika:9998/tika'
        headers={"Content-type": "image/png", "X-Tika-OCRLanguage": "nld", "Accept": "application/json"}
        response = requests.put(tikaurl, headers=headers, data=open(path_file,'rb').read())

        pageDocument = {
        "id": path_url,
        "title": driver.title,
        "text": response.json()["X-TIKA:content"].split('<div class="ocr">')[1].split("</div>")[0].replace("\n", " ")
        }
        print(json.dumps(pageDocument))

        print("Store search data of: ", path_url)
        solrurl='http://solr:8983/solr/ilse/update/json/docs'
        headers={'Content-type': 'application/json'}
        response = requests.post(solrurl, headers=headers, data=json.dumps(pageDocument))
        print(response.text)

        line = fp.readline() # Read next line

# line = fp.readline()

# 16:45 started

#print(json.dumps(pageDocument))

#curl -X POST -H 'Content-Type: ' 'http://localhost:8983/solr/my_collection/update/json/docs' --data-binary '
#{
#  "id": "1",
#  "title": "Doc 1"
#}'

# curl http://localhost:8983/solr/ilse/update?commit=true
# curl http://localhost:8983/solr/ilse/select?q=*:*

# Get unique ULR list from page
#uniqueLinks = []
#elems = driver.find_elements(By.XPATH, "//a[@href]")
#for elem in elems:
#    if elem.get_attribute("href") not in uniqueLinks:
#        uniqueLinks.append(elem.get_attribute("href"))
#        #print(elem.get_attribute("href"))
#    else:
#        continue
#uniqueLinks.sort()
#print(*uniqueLinks, sep = "\n")

driver.quit()


#curl http://localhost:8983/solr/ilse/query -d '
#{
#  "query": "text:schoenen",
#  "limit": 2,     // this single-valued parameter was overwritten.
#  "filter": ["text:paars","text:sneaker"]    // this multi-valued parameter was appended to.
#}'