def check1(ans1, ans2):
    if ans1 != '139':
        print("땡!")
        # (10*5 + 5) + (5*8 + 8) + (8*4 + 4)
    if ans2 != '2':
        print("땡!")
    else:
        print("mooyaho~")

# check2
# 서술형 문제로 따로 정답은 없습니다.
# 저희조에서 진행해보며 loss 값과 training accuracy 사이의 관계, 그리고 training accuracy에 영향을 주는 요인을 고려하였을 때,
# gap 차이가 가장 많이 발생하는 경우는 overfitting이 되었을 때 일텐데 overfitting이 되었다는 가정하에 가장 해당 learning rate값일 확률이 높은 것은 low learning rate일 때라고 이야기가 나왔습니다. 하지만 low learning rate일 때, 너무 작은 learning rate로 하게 되면 gradient가 0에 가까워져 weight나 bias값에 수정이 일어나지 않을 수도 있고 데이터 수, label 개수나 데이터 전처리와도 상관관계가 높기 때문에 항상 특정지어서 이야기는 안될 거 같고 이부분에 대해서 토의해보고 싶었습니다.
        
def check3():
    ans = input("순서대로 입력하시오(ex:010101011100)")
    if ans != '111001110110':
        print("땡!")
        # (10*5 + 5) + (5*8 + 8) + (8*4 + 4)
    else:
        print("mooyaho~")
        
# check4  
# Stride와 Pooling은 둘다 기존의 layer보다 크기가 작은 layer을 출력한다는 것, 그리고 특징을 추출할 때 사용한다는 것이 공통점이다.
# 차이점은 생성되는 layer의 차이의 변화이다.
# Stride는 size 설정값에 따라 생성되는 layer(convolutional layer)의 수가 달라지지만,
# Pooling은 convolutinoal layer에서 특정 부분을 추출해내는 것이기 때문에 전체 layer의 개수에 영향을 미치지 않는다.
# 즉, Stride 값이 작을수록 convolutional layer의 수가 증가하는데이는 feature가 많다는 것을 의미하고 이는 overfitting이 일어날 가능성이 높아지기 떄문에 유의. 
# Pooling은 그 layer의 값에서 특징적인 부분을 추출해내는 용도이므로, 그 이미지의 특징을 더 잘 나타내도록 한다.

def check5():
    print('Max Pooling의 경우, stride x stride 범위의 특징 중, 가장 활성화가 많이 된 특징을 extract 한다.')
    print('Average Pooling의 경우, stride x stride 범위의 특징들의 평균값을 extract 한다.\n')
    print('Max Pooling의 경우 stride x stride 범위의 값 중 하나를 제외한 나머지를 버리기 때문에 Feature extraction 측면에서 좋지 않다고 판단할 수 있지만,')
    print('오히려 가장 특징적인 값을 보존하기 때문에 stride x stride 범위의 지역 특성을 어느정도 유지 가능하다고 볼 수 있다.\n')
    print('Average Pooling의 경우 stride x stride개의 특징을 평균내기 때문에 역으로 특징이 모호해진다고 생각할 수 있다.')
    
"""Quiz 6"""
def check6(answer):
    if answer == 2:
        print('정답입니다.')
    else:
        print('오답입니다.')
    
def check7():
    print("선형성의 조건으로는 superposition(f(x1+x2) = f(x1) + f(x2_))와 Homogeneity(f(ax1)=af(x1)) 가 있다.")
    print("그 중 superposition의 조건을 만족하지 못하므로, 비선형 함수이다.")
    print("ex) x1=-1이고 x2=2일 때, f(-1+2) = 1, f(-1)+f(2) = 2")
    
def check8(answer) :
    if answer == (55, 96, 4) :
        print("딩동댕")
    else :
        print("땡")
        
def check9(correct, fault):
    if correct == "가/다" and fault == "나/라":
        print("정답")
    else:
        print("땡")
#나: 다층 퍼셉트론을 도입해도 비선형 활성화 함수가 없으면 선형 처리는 하나의 선형 처리로 줄여 표현할 수 있으므로 비선형 활성화 함수는 다층 퍼셉트론의 필수 구성요소이다.
#라: np.sign()함수를 이용하여 ReLU 함수의 미분값을 쉽게 나타낼 수 있다.

def check10(a_output_size, a_parameters, b_output_size, b_parameters ):
    if a_output_size != [28, 28, 1]:
        print('a output volume size 오답')
    if a_parameters != 75:
        print('a parameter 개수 오답')
        
    if b_output_size != [28, 28, 1]:
        print('b output volume size 오답')
    if b_parameters != 54:
        print('a parameter 개수 오답')    


def check11(answer1, answer2, answer3):
    if answer1 == ['패딩'] and answer2 == ['o'] and answer3 == ['풀링']:
        print('정답입니다!')
    else:
        print('땡')
        
def check12(ans):
    for v in ans:
        if v.lower() =='x':
            print('정답입니다!')
        else:
            print("오답입니다!")
            
def check13(answer):
    if answer == "OOXOOX":
        print("정답입니다.")
    else:
        print("오답입니다.")
        
        
def check14_1():
	ans = input("OX를 입력")
	if ans == 'XOOOX':
		print('정답')
	else:
		print('오답')
# (1) 하얀 부분이 높은, 검은 부분이 낮은 지점
# (5) 필터의 크기, stride가 필요함 

def check14_2():
	ans = input("(6)의 답 입력(나머지는 그냥 확인)")
	if ans == '22':
		print('(6)정답')
		print('(7) pooling layer에는 parameter가 없음')
		print('(8) (F-1)/2 ')