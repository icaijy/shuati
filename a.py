from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
lev={
    "入门":0,
    "普及−":1,
    "普及/提高−":2,
    "普及+/提高":3,
    "提高+/省选−":4,
    "省选/NOI−":5,
    "NOI/NOI+/CTSC":6,
    "暂无评定":7
}
def last():
    driver.get("https://www.luogu.com.cn/problem/list")
    
    driver.find_element("css selector",'img[src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgdmlld0JveD0iMCAwIDE0IDE0Ij4KICA8ZGVmcz4KICAgIDxzdHlsZT4KICAgICAgLmNscy0xIHsKICAgICAgICBmaWxsOiBub25lOwogICAgICB9CgogICAgICAuY2xzLTIgewogICAgICAgIGZpbGw6IHJnYmEoMCwwLDAsMC42NSk7CiAgICAgIH0KICAgIDwvc3R5bGU+CiAgPC9kZWZzPgogIDxnIGlkPSJpY29uX3ZlcnRpY2FsX3JpZ2h0IiBkYXRhLW5hbWU9Imljb24vdmVydGljYWwgcmlnaHQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAgLTEpIj4KICAgIDxyZWN0IGlkPSLnn6nlvaJfMzkiIGRhdGEtbmFtZT0i55+p5b2iIDM5IiBjbGFzcz0iY2xzLTEiIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCAxKSIvPgogICAgPHBhdGggaWQ9Iui3r+W+hF8yOCIgZGF0YS1uYW1lPSLot6/lvoQgMjgiIGNsYXNzPSJjbHMtMiIgZD0iTTI2MS44NzYsMTU2LjFoLS45OTJhLjExOS4xMTksMCwwLDAtLjEyNC4xMTJ2OS42NjNhLjExOS4xMTksMCwwLDAsLjEyNC4xMTJoLjk5MmEuMTE5LjExOSwwLDAsMCwuMTI0LS4xMTJ2LTkuNjYzQS4xMTkuMTE5LDAsMCwwLDI2MS44NzYsMTU2LjFabS03Ljg3NiwwdjEuMDE3YS40MzQuNDM0LDAsMCwwLC4xNzcuMzQ0bDQuNjM5LDMuNTI3LTQuNjM5LDMuNTI3YS40MzQuNDM0LDAsMCwwLS4xNzcuMzQ0djEuMDE3YS4xMjUuMTI1LDAsMCwwLC4yLjA4Nmw2LjU0MS00Ljk3My02LjU0MS00Ljk3M0EuMTI1LjEyNSwwLDAsMCwyNTQsMTU2LjFaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMjUxIC0xNTIuOTkyKSIvPgogIDwvZz4KPC9zdmc+"]').click()
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    last=BeautifulSoup(driver.page_source, 'html.parser').find_all('span',attrs={'data-v-beeebc6e':True,'data-v-b5709dda':True,'title':True})[-1]
    return int(last.text.strip()[1:])
l=last()

with open('data_'+str(l)+'.txt','w') as f:
    f.write(str(l))
    f.write("\n")
    for i in range(1000,l+1):
        start_time = time.perf_counter()
        try:
            driver.get("https://www.luogu.com.cn/problem/P"+str(i))
            
            content = driver.page_source
            soup = BeautifulSoup(content, 'html.parser')
            level = soup.find('span', {'data-v-263e39b8': True})
            """
            标签，但目前不知道干嘛用
            while (True):
                try:
                    driver.find_element("css selector", 'span[data-v-e4b7c2ca]').click()
                    break
                except:
                    pass
            tag = soup.find_all('span', class_='lfe-caption',attrs={'data-v-187aafe9': True})
            for a in tag:
                print(a.text.strip())
            """
            f.write(str(lev.get(level.text.strip())))
            f.write(" ")
        except:
            f.write("8 ")
        print("爬取P"+str(i)+"完成！进度："+str(int(100*(i-1000)/(l-1000)))+"%"+" 耗时"+str(round((time.perf_counter()-start_time)*1000))+"ms")
    driver.quit()
    

    
