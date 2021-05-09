def check1():
    ans = input("정답을 입력하시오")
    if ans == "OOXO":
        print("정답~")
    else:
        print("떙!")
        
# 1. sigmoid 함수의 경우, zero centered하지 않아서 weight가 다같이 증감하는 경향을 보이게 됨.
# 2. dead ReLU가 발생하는 경우는 크게 두가지가 있다.
       # 첫번째, 초기설정을 data에 너무 떨어진 weight를 잡아버린 경우
       # 두번째, 학습률이 너무 커서 weight조정 중에 data에 너무 멀어지게 되는 경우
# 3. 데이터 전처리 과정을 통해 입력 레이어에서만 zero-mean이 해결 가능하고 다음 레이어부터는 문제 해결 불가능
# 4. 검증데이터가 학습이나 평가데이터와 곂칠 순 있더라도, 학습과 평가 데이터끼리는 구분해야한다.

def check2():
    ans = input("정답을 입력하시오")
    #CNN의 층이 깊어진다면 사소한 파라미터의 변화도 깊은 층이 받는 영향은 커집니다. 이전 layer의 파라미터 변화로 인해, 현재 layer의 입력 분포가 달라지는 현상이 일어나기 때문입니다. 
    #이를 “Covariate Shift”라고 하며, 이를 줄이기 위해서 BN을 사      용하게 됩니다. 또한, BN을 사용하면 비교적 hyper-parameter에서 자유로워집니다. learning rate를 올려서 더 빠른 학습을 가능하게 하고, 또한, local minima를 쉽게 빠져나오게       #만들 수 있습니다.
#     크기가 큰 α를 유지한다면, 학습은 빠르지만 optima 부근에서 맴돌 뿐 정확히 수렴하기 어렵습니다.
# 크기가 작은 α를 유지한다면, 학습이 매우 느리고 overfitting이나 learning stop이 일어날 수 있습니다.
    print((a) learning rate decay) 
    print((b),(c),(d) step decay, exponential decay, 1/t decay)

def check3():
    ans = input("정답을 입력하시오")
    if ans == "4" or ans == "4번":
        print("정답~")
    else:
        print("떙!")
    
def check4():
    ans1 = input("m의 값 : ")
    ans2 = input("update되는 parameter 개수 : ")
    if ans1 == "300" and ans2 == "60":
        print("정답~")
    else:
        print("떙!")
        
def check5():
    ans = input("정답을 입력하시오")
    if ans == "OOOO":
        print("정답~")
    else:
        print("떙!")

def check6(answer):
    if answer == 1:
        print('정답입니다!')
    else:
        print('오답입니다!')
# Batch-Normalization은 N개의 그룹을 만들어 각 그룹별로 정규화하는 과정이다. N개의 그룹은 각각 M개의 값을 가지고 있다. 즉 [M,N]형태의 미니배치 데이터에서는 모든 column에 대해 정규화를 진행한다고 말할 수 있다.

def check7(answer):
    print("simoid 함수는 output이 zero centered가 되지 않아 입력이 양수로만 들어올 경우, ")
    print("gradient가 모두 양수이거나 모두 음수가 된다.")
    print("따라서 preprocessing을 통해 모든 입력이 양수가 되는 것을 방지해주어야 한다.")
    
def check8():
    ans = input("정답을 입력하시오")
    if ans == '1':
        print('정답')
    else:
        print('오답')
        
def check9():
    print('토론해봅시다!')
    
def check10(answer):
    if answer == ['x','o','o','o']:
        print('정답입니다!!!!!')
    else:
        print('오답오답오답')

def check11(a):
    print('데이터들의 모든 차원을 동일한 범위로 만들어 비슷하게 기여할 수 있도록')
    print('이미지는 이미 각 차원 간 scale이 어느정도 맞춰져있기 때문 0~255')
    if a[0]!='X':
        print('3번 틀림')
    if a[1]!= 'O':
        print('4번 틀림')

def check12(answer):
    if answer == 'XXX':
        print('정답')
    else :
        print('오답')
        
def check13(answer):
    real_answer = 'ooxo'
    for i in range(4):
        if real_answer[i] == answer[i].lower():
            print("{} 번 정답입니다".format(i+1))
        else:
            print("{} 번 오답입니다".format(i+1))
            
def check14_1(ans):
	if ans == 'cde b':
		print('정답')
	else:
		print('오답')

def check14_2(ans):
    if ans == 'OOXO':
        print('정답')
    else:
        print('오답')
# '(3) 이미지는 이미 특정 범위값을 가지는 것이므로, 일반적으로 normalization은 수행하지 않음'            
            
def check15(answer):
    if answer == "OOOOOX":
        print("정답입니다.")
    else:
        print("오답입니다.")