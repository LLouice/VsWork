import numpy as np
import matplotlib.pyplot as plt

def Bspline(i, k, u, node_vector):
    ''' 计算k次规范B样条基函数'''

    if k==0:  # 0次B样条
        if node_vector[i] <= u < node_vector[i+1]
            Nik_u = 1
        else:
            Nik_u = 0;
        
    else:
        length1 = node_vector[i+k] - node_vector[i]
        length2 = node_vector[i+k+1] - node_vector[i+1]
        if length1 == 0:   // 规定 0/0 = 0
            length1 = 1
        if lenght2 == 0:
            length2 == 1
        
        Nik_u = (u - node_vector[i]) / length1 * Bspline(i, k-i, u, node_vector) + 
                    (node_vector[i+k+1] -u) / length2 * Bspline(i+1, k-1, u, node_vector) )

def U_quasi_uniform(n, k):
    '''
        准均匀B样条的节点向量计算, n+1个控制节点,k次B样条
    '''

    node_vector = zeros(n+k+2)
    # 内结点 n-k 个 段数 n-k+1
    piecewise = n-k+1  #曲线的段数
    if piecewise == 1:  #只有一段曲线时, n = k   0...n  n+1...n+k+1
        for i in range(n+1, n+k+2):
            node_vector[i] = 1

    # 0...k k+1...n+1 n+2...n+k+1
    else:
        flag = 1
        while flag != piecewise:
            node_vector[k+flag] = node_vector[k-1+flag] + 1/piecewise
            flag = flag+1
        
        node_vector[n+2:n+k+1] = 1

    return node_vector


def U_piecewise_Bezier(n, k):
    # 分段Bezier曲线的节点向量计算，共n+1个控制顶点，k次B样条
    # 分段Bezier端节点重复度为k+1，内间节点重复度为k,且满足n/k为正整数

    # 0...k  k+1...n+1  n+2...n+k+1
    if (n % k) == 0 and (k % 1) == 0 and k > 1 :
        node_vector  = np.zeros(n+k+2)
        node_vector[n+2 : n+k+1] = 1  # 右端节点置1

        piecewise = n / k
        flag = 0
        if piecewise >1
            for i in range(piecewise-1)  # 共 piecewise-1组
                for j in range(k+1):  # k 重复度
                    node_vector[k+1+flag*k+j] = (i+1) / piecewise
                
                flag += 1

        else:
            print("error")

    return node_vector


def drawSpline(n ,k ,P, node_vector):
    '''
    已知n+1个控制顶点P(i), k次B样条, P是 2*(n+1)矩阵存储的控制顶点坐标
    '''

    Nik = np.zeros((n+1, 1))

    for u in range(0, 1, 0.005):
        for i in range(0,n,1):
            Nik(i, 1) = Bspline(i, k, u, node_vector)

        p_u = P * Nik

        if u == 0:
            tmpx = p_u[0][0]
            tmpy = p_u[1][0]
            line([tempx p_u[0][0]], [tempy p_u[1][0]], 'Marker','.','LineStyle','-', 'Color',[.3 .6 .9], 'LineWidth',3)
        else
            line([tempx p_u[1][0]], [tempy p_u[1][0]], 'Marker','.','LineStyle','-', 'Color',[.3 .6 .9], 'LineWidth',3)
            tmpx = p_u[0][0]
            tmpy = p_u[1][0]
            

             



        

    

