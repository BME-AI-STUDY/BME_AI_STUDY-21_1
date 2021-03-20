""" QUIZ 1 """
def check1(answer1, answer2):
    if (answer1 == '100') and (answer2 == 'cant know'):
        return 1
    else:
        return 0

""" QUIZ 2 """
def check2(answer):
    if answer == "validation":
        return 1 
    else:
        return 0
        
""" QUIZ 3 """
def check3(answer):
    if answer == "학습률":
        return 1 
    else:
         return 0

""" QUIZ 6 """ 
def check6(answer):
    if answer == 2:
        print('정답!')
    else :
        print('오답!')

# 해설: test시, test용 data를 메모리 각각의 training data와 모두 비교하기 때문에 classification 속도는속도는 training data의 size와 선형비례한다.

""" QUIZ 7 """
def check7(answer):
    if answer == 3:
        print('정답!')
    else:
        print('오답!')
        
# 해설: 주피터 노트북에서 answer1.plot_quiz7() 함수를 실행시켜 나오는 그래프를 참고하자.경사하강법을 무한히 사용한다고 global minimum에 도달하는 것을 보장할 수 없다. Local minimum에 갇혀 빠져나오지 못할 수 있다. 
def plot_quiz7():
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.linspace(0.5, 6.2, 200)
    y = (x-2)*(x-1)*(x-4)*(x-6)
    plt.plot(x,y)
    plt.xlabel('w')
    plt.ylabel('loss')
    plt.grid(True)
    plt.axis([0,6.5, -20, 15])
    props = dict(facecolor='black', shrink=0.1)
    plt.annotate('local_minimum', xytext=(3,-8), xy=(1.35,-2.7), arrowprops=props, fontsize=14, ha='center')
    plt.annotate('global_minimum', xytext=(3.5,-18), xy=(5.35,-12.7), arrowprops=props, fontsize=14, ha='center')
    
""" QUIZ 8 """ 
def check8_1(answer1) :
    if answer1 == (10,1):
        print("딩동댕")
    else :
        print("땡")

def check8_2(answer2) :
    if answer2 == (1,1):
        print("딩동댕")
    else :
        print("땡")

def check8_3(answer3):
    print("1/m * W.T * dC/dY 이 정답입니다. 직접 비교해보세요")

""" QUIZ 9 """ 
def check9_1(a):
    if a == 18:
        print("정답입니다.")
    else :
        print("오답입니다.")
        
def check9_2(a):
    m=1
    if a == (3,m):
        print("정답입니다.")
    else :
        print("오답입니다.")
    
""" QUIZ 10 """
def check10(answer):
    if answer == '교차검증':
        print("정답입니다.")
    elif answer == 'cross validation' or answer == 'Cross validation' or answer == 'Cross Validation' :
        print('정답입니다.')
    else:
        print('오답입니다.')
        print('대문자, 하이폰 사용, 띄어쓰기에 따라 오답 판정이 날 수도 있으니 답지를 확인해 주세요')
        
""" QUIZ 11 """
def check11(answer):
    if answer[0]!='10,8':
        print('1) 오답')
    if answer[1]!='8,3':
        print('2) 오답')
    if answer[2]!='3':
        print('3) 오답')
    if answer[3]!='10,3':
        print('4) 오답')
    else:
        print('정답')

""" QUIZ 12 """
# 다맞아야 정답 처리 순서대로 'o, x, o'
def check12(answer):
    if answer == ['o', 'x', 'o']:
        print('정답입니다!')
    else :
        print('다시 풀어보세요')

""" QUIZ 13 """
def check13_1(answer):
    if answer == 0.094:
        print("정답입니다.")
    else:
        print("오답입니다.")

def check13_2(answer):
    if answer == 0.800:
        print("정답입니다.")
    else:
        print("오답입니다.")
        
''' 값을 바꾼 부분은 #으로 표시 및 주석

def run_train(x, y):
    output, aux_nn = forward_neuralnet(x)
    loss, aux_pp = forward_postproc(output, y) 
    accuracy = eval_accuracy(output, y)
    
    G_loss = 1.0
    G_output = backprop_postproc(G_loss, aux_pp, loss)  #loss 값을 추가로 받아줌,
    backprop_neuralnet(G_output, aux_nn)
    
    return loss, accuracy

def forward_postproc(output, y):
    diff = output - y
    square = np.square(diff)
    loss = np.sqrt(np.mean(square))                     #RMES_loss^2 = MES_loss 이므로
    return loss, diff

def backprop_postproc(G_loss, diff, loss):              #loss 값을 추가로 받아줌
    shape = diff.shape
    
    g_loss_square = ( np.ones(shape) / np.prod(shape)) / (2 * loss) 
#여기서 loss 값을 넣어줌, 2*loss 로 나누는 이유는 편미분에 의해 값이 바뀌었으므로
    g_square_diff = 2 * diff
    g_diff_output = 1

    G_square = g_loss_square * G_loss
    G_diff = g_square_diff * G_square
    G_output = g_diff_output * G_diff
    
    return G_output
'''

""" QUIZ 14 """
def check14(answer):
    if answer== '1001':
        print('정답')
    else: 
        print('오답')

""" QUIZ 15 """
def check15(w1, w2):
    if w1 == 6 and w2 == 6:
        print("정답입니다!")
    else:
        print("틀렸습니다!")
