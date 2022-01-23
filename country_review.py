#리뷰 불러오기
#리뷰는 나라이름_review

def openfile():
    country_nam = input("나라 이름을 입력하세요:")
    country_nam = country_nam.upper()
    country_name = country_nam + "_review.txt"
    try:
        with open('C:/Users/chosungwon/Desktop/review/' + country_name,'r') as file:
            line = file.readline()
            print(line.strip('\n'))
            while line != '':
                line = file.readline()
                print(line.strip('\n'))
    except:
        print("Error : 파일을 다시 확인해 주세요")

def writefile():
    review_n = input("후기를 작성해 주세요 :")
    file_w = input("나라 이름을 입력하세요 :")
    file_w = file_w.upper()
    file_w = file_w + ".txt"
    try:
        review_w = open("C:/Users/chosungwon/Desktop/review/" + file_w,"w")
        review_w.write(review_n)
        review_w.close()
        print("저장되었습니다.")
    except:
        print("Error : 알 수 없는 에러가 생겼습니다")
