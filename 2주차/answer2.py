def check1():
    ans = input("정답을 입력하시오")
    if ans == "(0,0,0,0,0,1)":
        print("정답")
    else:
        print("땡")
        
def check2(answer):
    if answer == 4:
        print('Correct!')
    else:
        print('Wrong!')
        
def check3():
    ans = input("정답을 입력하시오")
    if ans == "oxxo":
        print("정답")
    else:
        print("땡")   
# 1. : 교차 엔트로피 수식으로 확인가능
# 2. : FP만 감소한다고 가정하면 정밀도만 증가하게 되고, F1은 정밀도와 재현율의 조화평균이기에 증가하긴 하지만 좀처럼 증가하진 않는다.
# 3. : 람다는 하이퍼파라미터라서 학습중에 변하는 값이 아니다.
# 4. : Multiclass SVM는 특정 차이만 보이면 0이 되어버리고, Softmax classifier는 각각 스코어를 계산하기 때문에 더 예민하다.
        
def check4():
    ans = input("정답을 입력하시오")
    if ans == "1":
        print("정답")
    else:
        print("땡")     
        
def check5(ans1, ans2, ans3, ans4, ans5):
    if ans1 == "Layer" and ans2 ="Activation Function" and ans3="Predict Data" and ans4="Label Data" and ans5 == "Loss Function":
        print("정답")
    else:
        print("땡")  

def check6(answer):
    if answer == 3:
        print('정답')
    else :
        print('오답')
        
def check7(answer):
    if answer == 2:
        print('정답')
    else:
        print('오답')
# 2번: label이 정답인 output의 경우 1과의 MSE를 사용할 수 있고, label이 오답인 경우 0과의 MSE를 사용할 수 있다. 그러나 대부분의 이진분류 문제에서 MSE보다는 sigmoid-cross-entropy를 loss function으로 사용하는데, 이는 성능의 차이 때문이다.

def check8(answer) :
    if answer == 3:
        print("딩동댕")
    else :
        print("땡")

def check9(answer):
    if answer == 4:
        print('정답입니다.')
    else:
        print('오답입니다.')
        
def check10(answer):
    if answer == 'O':
        print('정답')
    elif answer == 'X':
        print('오답')
        
def check11(answer):
    if answer[0]!=0.95:
        print('accuracy 오답')
    if answer[1]!=0.91:
        print('precision 오답')
    if answer[2]!=1:
        print('recall 오답')
    else:
        print('정답')
        
def check12(a):
    if a != 1:
        print('오답입니다.')
    if a == 1:
        print('정답입니다^^')

    
def check13(answer):
    if answer == "OOXXO":
        print("정답입니다.")
    else:
        print("오답입니다.")

        
def check14_1(answer):
    if answer == 11:
        print('정답')
    else :
        print('오답')

def check14_2(answer):
    if answer == "교차 엔트로피" :
        print('(3) 정답\n(4) 두 확률 분포가 닮아갈수록 값이 작아짐\n(5) 교재 94~95')
    else :
        print('(3) 오답\n(4) 두 확률 분포가 닮아갈수록 값이 작아짐\n(5) 교재 94~95')

def check15_1(ans): print("정답입니다!") if (ans == "3") else print("오답입니다")
def check15_2(ans): print("정답입니다!") if (ans == "3") else print("오답입니다")