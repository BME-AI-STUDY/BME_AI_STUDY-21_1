def check1():
    ans = input("정답을 입력하시오")
    if ans == 'max,index':
        print('무야호~')
    else:
        print('오답')

def check2():
    ans = input("정답을 입력하시오")
    if ans == "OXXO":
        print("무야호~")
    else:
        print("떙!")
        
def check3():
    ans = input("정답을 입력하시오")
    if ans == "교차엔트로피" or ans == "교차 엔트로피" or ans == "cross entropy" or ans == "crossentropy":
        print("무야호~")
    else:
        print("떙!")

def check4():
    ans1 = input("odd =")
    ans2 = input("logit =")
    if ans1 == y/1-y and ans2 == log(y/1-y):
        print("무야호~")
    else:
        print("떙!")

def check5():
    print('토론해 봅시다!')
        
def check6(answer_1, answer_2, answer_3, answer_4, answer_5):
    answers = [answer_1, answer_2, answer_3, answer_4, answer_5]
    labels = ['(N,b)', '(N,b)', '(1)', '(1)', '(N,b)']
    print()
    for n in range(5):
        if answers[n] == labels[n]:
            print('answer_{} : 정답'.format(n+1))
        else:
            print('answer_{} : 오답'.format(n+1))

def check7(answer1, answer2, answer3):
    if answer1 == "4e^(-3)" and answer2 == "4e^(-3)" and answer3 == "e^(-3)":
        print("정답")
    else:
        print("땡")

def check8():
    print("단순히 한차례 선택분류를 할 것이 아닌 이후의 데이터를 가지고 학습을 시켜 새로운 데이터가 들어와도 제대로 분류할 수 있게끔 해야하기 때문이다.")
    print("따라서 확률값으로 변환시켜 확률값을 토대로 weight를 조정하여 학습을 시키는 과정이 이후에 이루어진다")

"""Quiz 9"""
def check9_1(answer1):
    if answer1 == 4:
        print('정답입니다.')
    else:
        print('오답입니다.')

def check9_2(answer2):
    if answer2 == 'chain rule':
        print('정답입니다.')
    elif answer2 == 'chainrule':
        print('정답입니다.')
    else:
        print('오답입니다.')
        
def check10(answer) :
    if answer == (1024, [1024,1024], 1024):
        print("딩동댕")
    else :
        print("땡")
        
def check11(answer):
    if answer[0]!=-0.05:
        print('ㄱ 오답')
    if answer[1]!=0.05:
        print('ㄴ 오답')
    if answer[2]!=-0.05:
        print('ㄷ 오답')
    if answer[3]!=0:
        print('ㄹ 오답')
    else:
        print('정답')
        
def check12(input_vector, logits_vector, probability, num_of_perceptron):
    if input_vector == ['n',7] and logits_vector == ['n',3] and probability == ['n',3] and number_of_perceptron ==3 :
        return True
    else : 
        return False

def check13(ans): 
    print("정답입니다!") if (ans == "2") else print("오답입니다")
    
def check14(answer) :
    if answer == 3:
        print('정답')
    else :
        print('오답')
        
def check15(answer):
    if answer == "OOXOX":
        print("정답입니다.")
    else:
        print("오답입니다")