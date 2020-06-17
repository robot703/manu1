def slimbody():
    show_cody("마른체형 코디", description='*마른 체형 코디*\n'
                                     + '1.딱 달라붙지 않는 정사이즈보다 한치수 큰 상하의\n'
                                     + '2. 밝은 색감의 옷과 화려한 패턴으로 왜소한 체형을 보완\n')


def normalbody():
    show_cody("보통체형 코디", description='*보통 체형 코디*\n'
                                     + '1.슬랙스코디\n'
                                     + '다리라인을 잡아주는 아이템\n'
                                     + '여름이나 겨울 언제든 매치가능\n'
                                     + '2.코트\n'
                                     + '가을, 겨울에 부해보이지도 않고 왜소해보이지도 않도록 매치\n')


def fatbody():
    show_cody("뚱뚱한 체형 코디", description='*뚱뚱한 체형*\n'
                                       + '코디1.정장스타일로 몸매라인을 잡아주는 아이템\n'
                                       + '2.어두운 색감의 옷이나 패턴이 들어가 있지않은 옷\n'
                                       + '3.사이즈는 정사이즈로 입는 걸 추천\n')


def bmi():
    he = askfloat(title="'BMI계산기'", prompt="'키를 입력하세요(m)'")
    we = askfloat(title="'BMI계산기'", prompt="'몸무게를 입력하세요(kg)'")
    bmi = we / (he * he)
    bmi = round(bmi, 1)

    if bmi <= 18.5:
        slimbody()
    elif bmi < 25:
        normalbody()
    else:
        fatbody()
