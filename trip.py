import pygame 
from pygame.locals import *
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import country_review

dic_country = {'아시아' : ['일본', '중국'],
               '유럽' : ['프랑스', '이탈리아'],
               '북아메리카' : ['미국, 캐나다'],
               '남아메리카' : ['브라질', '콜롬비아'],
               '오세아니아' : ['호주', '뉴질랜드']}

schedule = {}

player = {'일본' : 'https://www.youtube.com/watch?v=CJX05x3GC_U',
          '중국' : 'https://www.youtube.com/watch?v=JJ5WuysjNmA',
          '프랑스' : 'https://www.youtube.com/watch?v=D1rrku5ivaM',
          '이탈리아' : 'https://www.youtube.com/watch?v=ezpniI1GsT8',
          '캐나다' : 'https://www.youtube.com/watch?v=Stl9jwWq4T4',
          '미국' : 'https://www.youtube.com/watch?v=8vr-bgJbPrY',
          '브라질' : 'https://www.youtube.com/watch?v=fQ47MBpjQrw',
          '콜롬비아' : 'https://www.youtube.com/watch?v=UoEAa1Vfqhw',
          '호주' : 'https://www.youtube.com/watch?v=HOY-yz2k3wc',
          '뉴질랜드' : 'https://www.youtube.com/watch?v=SKlk-L4boBQ'}

"""def scheduling(time, stime, country, place):
    for i in range(int(time)):
        t = int(stime) + i
        schedule[str(t)].append(country)
        schedule[str(t)].append(place)"""

def view_ad(country):
    ad_url = player[country]
    driver.get(ad_url)
    
    if(country == '일본'):
        sleep(72)
        
    elif(country == '중국'):
        sleep(273)

    elif(country == '프랑스'):
        sleep(139)

    elif(country == '이탈리아'):
        sleep(279)

    elif(country == '캐나다'):
        sleep(182)

    elif(country == '미국'):
        sleep(189)

    elif(country == '브라질'):
        sleep(157)

    elif(country == '콜롬비아'):
        sleep(441)

    elif(country == '호주'):
        sleep(33)

    elif(country == '뉴질랜드'):
        sleep(63)

driver_route = "/Users/chosungwon/Downloads/chromedriver.exe"

driver = webdriver.Chrome(driver_route)

#-----------------------------------------------------------------------------------------------------#

pygame.init() #초기화

screen = pygame.display.set_mode((800,600),0,32)   #화면 설정
pygame.display.set_caption('가상 여행')     #프로젝트 이름 설정


img = pygame.image.load('C:/Users/chosungwon/Desktop/시작.jpg')  #첫 화면 사진 불러오기
screen.blit(img, (0, 0))
pygame.display.flip()
 

while True:
    ev = pygame.event.poll()
    if ev.type == pygame.MOUSEBUTTONDOWN :          #마우스를 클릭했을 시에
        img = pygame.image.load('C:/Users/chosungwon/Desktop/2번 화면.jpg')  #사진 불러와서 보이게 하기
        screen.blit(img, (0, 0))
        pygame.display.flip()
        break
    
while True:
    ev = pygame.event.poll()
    if ev.type == pygame.MOUSEBUTTONDOWN :          #마우스를 클릭했을 시에
        img = pygame.image.load('C:/Users/chosungwon/Desktop/3번 화면.jpg')  #사진 불러와서 보이게 하기
        screen.blit(img, (0, 0))
        pygame.display.flip()
        break


done = False
while not done :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :#키이벤트

            if event.key == pygame.K_6:
                img = pygame.image.load('C:/Users/chosungwon/Desktop/전체 지도.jpg')     #북아메리카 사진 불러오기
                img2 = pygame.image.load('C:/Users/chosungwon/Desktop/제목 없음.png')
                screen.blit(img, (0, 0))
                screen.blit(img2, (0, 0))
                pygame.display.flip()

            if event.key == pygame.K_7:
                img = pygame.image.load('C:/Users/chosungwon/Desktop/1-1.png')     #북아메리카 사진 불러오기
                screen.blit(img, (0, 0))
                pygame.display.flip()
                country=input()
                print(country)
                
            if event.key == pygame.K_1:                   #1번 키를 눌렀을 시
                img = pygame.image.load('C:/Users/chosungwon/Desktop/북아메리카.jpg')     #북아메리카 사진 불러오기
                screen.blit(img, (0, 0))
                pygame.display.flip()

            if event.key == ord('a'):                       #a키를 눌렀을 시 변수(country)에 캐나다 저장하기
                country=('캐나다')
                print(country)

            if event.key == ord('b'):
                country=('미국')
                print(country)
                
            if event.key == pygame.K_2:
                img = pygame.image.load('C:/Users/chosungwon/Desktop/남아메리카.jpg')
                screen.blit(img, (0, 0))
                pygame.display.flip()
                
            if event.key == ord('c'):
                country=('콜롬비아')
                print(country)

            if event.key == ord('d'):
                country=('브라질')
                print(country)
           

            if event.key == pygame.K_3:
                img = pygame.image.load('C:/Users/chosungwon/Desktop/유럽.jpg')
                screen.blit(img, (0, 0))
                pygame.display.flip()

            if event.key == ord('e'):
                country=('프랑스')
                print(country)

            if event.key == ord('f'):
                country=('이탈리아')
                print(country)

                
            if event.key == pygame.K_4:
                img = pygame.image.load('C:/Users/chosungwon/Desktop/아시아.jpg')
                screen.blit(img, (0, 0))
                pygame.display.flip()

            if event.key == ord('g'):
                country=('중국')
                print(country)

            if event.key == ord('h'):
                country=('일본')
                print(country)
                
            if event.key == pygame.K_5:
                img = pygame.image.load('C:/Users/chosungwon/Desktop/오세아니아지도.jpg')
                screen.blit(img, (0, 0))
                pygame.display.flip()

            if event.key == ord('i'):
                country=('호주')
                print(country)

            if event.key == ord('j'):
                country=('뉴질랜드')
                print(country)

        if event.type == pygame. QUIT:
            done=True

flag_ad = input("다음 나라의 홍보 광고를 보시겠습니까?(y/n) : ")

while(flag_ad != 'y' and flag_ad != 'n'):
    flag_ad = input("다시 입력해주세요(y/n) : ")

if(flag_ad == 'y'):
    view_ad(country)

#-----------------------------------------------------------------------------------------------------------------#

driver.get("http://www.hanatour.com/")

tourist = input("가고싶은 곳을 입력해 주세요 : ")
driver.find_element_by_name('searchQuery').send_keys(tourist)
driver.find_element_by_xpath('//*[@id="search"]/button').click()

flag = True
page_now = 0

while(flag):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    tour_list = soup.find("div", {"class" : "conts"})
    tour_list = soup.find("div", {"class" : "search_product"})
    tour_list = soup.find_all("div", {"class" : "prod_tit test"})

    result = soup.find("div", {"class" : "search_keyword"})
    result = soup.find("span", {"class" : "keyword_count"})
    result = soup.find("em").text

    if(int(result)%10 == 0):
        page = int(result) // 10

    else:
        page = int(result) // 10 + 1
        
    if(result == '0'):
        tourist = input("검색결과가 없습니다.\n다시 입력해 주세요 : ")
        driver.find_element_by_name('searchQuery').send_keys(tourist)
        driver.find_element_by_xpath('//*[@id="search"]/button').click()
            
    else:
        print("\n")
        page_now += 1
                
        for n in range(len(tour_list)):
            print(n+1, ' ', tour_list[n].text)

        com = input("이 중에 마음에 드시는 것이 있습니까?(y/n) : ")
                
        if(com == 'y'):
            num = int(input("번호를 입력해 주세요 : "))
            time = int(input("여행할 시간을 입력해주세요 : "))
            s_time = int(input("여행을 시작할 시간을 입력해주세요 : "))
            #scheduling(time, s_time, country, tour_list[num-1].text)
            for i in range(int(time)):
                t = i+int(s_time)
                schedule[t] = country
                schedule[t] = tour_list[num-1].text
                
            flag_1 = input("일정을 더 세우시겠습니까?(y/n) : ")
                    
            if(flag_1 == 'y'):               
                tourist = input("가고싶은 곳을 입력해 주세요 : ")
                driver.find_element_by_name('searchQuery').send_keys(tourist)
                driver.find_element_by_xpath('//*[@id="search"]/button').click()
                        
            elif(flag_1 == 'n'):
                flag = False

        elif(com == 'n'):
            if(page_now == page):
                print("다 보셨습니다.\n")
            else:
                driver.find_element_by_xpath('//*[@id="searchForm"]/div/div[5]/div[1]/div[2]/div[5]/a[13]').click()

#-----------------------------------------------------------------------------------------------------------------------------------------#

#country = input("가고 싶은 곳을 입력하세요(일본, 중국, 이탈리아, 프랑스, 미국, 캐나다, 콜롬비아, 브라질, 호주, 뉴질랜드):\n")
people = int(input("가는 인원의 수를 입력하세요"))
if people == 2:
    bed = input("더블인가요, 트윈인가요?")
    if bed == "트윈":
        people = 3
    else:
        pass
elif people == 6:
    adult = input("성인(만 12세이상)은 몇명인가요?(최대 4명)")
    if adult == '2':
        bed = input("더블인가요, 트윈인가요?")
        if bed == "트윈":
            adult == '3'
        else:
            pass
    elif int(adult) > 2:
        adult = str(int(adult)+1)

    child = str(int(input("아동(만 11세 이하)은 몇명인가요?(최대 2명)")))
    if child == "1":
        age = str(int(input("아동은 몇살인가요?\n"))+2)
    elif child == "2":
        age = str(int(input("아동 중 더 나이가 많은 사람은 몇살(만)인가요?(1명)\n"))+2)
        age2 = str(int(input("아동 중 나이가 적은 사람은 몇살(만)이가요?\n"))+2)

elif people > 2:
    people+=1
                
driver.get('http://www.hanatour.com/asp/booking/mtravel/rmt-00000.asp?')
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[1]/div/ul[1]/li[3]/div[2]/input[2]').click()
if country == "일본":
    driver.find_element_by_xpath('//*[@id="jq_marjor_city_select"]/tbody/tr[2]/td/a[2]').click()
elif country == "중국":
    driver.find_element_by_xpath('//*[@id="jq_marjor_city_select"]/tbody/tr[3]/td/a[4]').click()
elif country == "이탈리아":
    driver.find_element_by_xpath('//*[@id="jq_marjor_city_select"]/tbody/tr[4]/td/a[1]').click()
elif country == "프랑스":
    driver.find_element_by_xpath('//*[@id="jq_marjor_city_select"]/tbody/tr[4]/td/a[2]').click()
elif country == "미국":
    driver.find_element_by_xpath('//*[@id="jq_marjor_city_select"]/tbody/tr[5]/td/a[3]').click()
elif country == "캐나다":
    driver.find_element_by_xpath('//*[@id="jq_marjor_city_select"]/tbody/tr[7]/td/a[2]').click()
elif country == "콜롬비아":
    driver.find_element_by_xpath('//*[@id="jq_marjor_city_select"]/tbody/tr[9]/td/a[7]').click()
elif country == "브라질":
    driver.find_element_by_xpath('//*[@id="jq_marjor_city_select"]/tbody/tr[9]/td/a[1]').click()
elif country == "호주":
    driver.find_element_by_xpath('//*[@id="jq_marjor_city_select"]/tbody/tr[6]/td/a[2]').click()
elif country == "뉴질랜드":
    driver.find_element_by_xpath('//*[@id="jq_marjor_city_select"]/tbody/tr[6]/td/a[4]').click()

driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[2]/div/ul[3]/li[2]/div[1]/div/a').click()
driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[2]/div/ul[3]/li[2]/div[1]/div/div/div/div/ul/li['+ str(people) +']/a').click()
if people == "6":
    driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[2]/div/ul[3]/li[2]/div[2]/ul[1]/li[2]/div[1]/div/a').click()
    driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[2]/div/ul[3]/li[2]/div[2]/ul[1]/li[2]/div[1]/div/div/div/div/ul/li['+ str(adult) +']/a').click()
    driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[2]/div/ul[3]/li[2]/div[2]/ul[1]/li[2]/div[2]/div/a').click()
    driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[2]/div/ul[3]/li[2]/div[2]/ul[1]/li[2]/div[2]/div/div/div/div/ul/li['+ str(int(child)+1) +']/a').click()
    if child == "2":
        driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[2]/div/ul[3]/li[2]/div[2]/ul[1]/li[2]/div[4]/div/a').click()
        driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[2]/div/ul[3]/li[2]/div[2]/ul[1]/li[2]/div[4]/'+'div/div/div/div/div/div[1]/div/ul/li['+age2+']/a').click()
    driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[2]/div/ul[3]/li[2]/div[2]/ul[1]/li[2]/div[3]/div/a').click()
    driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[2]/div/ul[3]/li[2]/div[2]/ul[1]/li[2]/'+'div[3]/div/div/div/div/div/div[1]/div/ul/li['+ age +']/a').click()
    driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/div[2]/div/ul[3]/li[2]/div[2]/div/a[3]').click()
driver.find_element_by_xpath('//*[@id="searchForm_rmt"]/div/button').click()

for n in schedule:
    print(n, schedule[n])

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

flag_review = input("여행 후기를 작성하시겠습니까?(y/n) : ")

while(flag_review != 'y' and flag_review != 'n'):
    flag_review = input("다시 입력해 주세요(y/n) : ")

if(flag_review == 'y'):
    flag_review_ex = input("후기 예시를 보시겠습니까?(y/n) : ")

    while(flag_review_ex != 'y' and flag_review_ex != 'n'):
        flag_review_ex = input("다시 입력해 주세요(y/n) : ")

    if(flag_review_ex == 'y'):
        country_review.openfile()

    country_review.writefile()

pygame.quit()
