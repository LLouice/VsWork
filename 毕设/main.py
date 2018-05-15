import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


def Bspline(i, k, u, node_vector):
    ''' 计算k次规范B样条基函数'''

    if k == 0:  # 0次B样条
        if node_vector[i] <= u < node_vector[i + 1]:
            Nik_u = 1.0
        else:
            Nik_u = 0.0

    else:
        length1 = node_vector[i + k] - node_vector[i]
        length2 = node_vector[i + k + 1] - node_vector[i + 1]
        if length1 == 0.0:   # 规定 0/0 = 0
            length1 = 1.0
        if length2 == 0.0:
            length2 = 1.0

        Nik_u_1 = (u - node_vector[i]) / length1 * \
            Bspline(i, k - 1, u, node_vector)
        Nik_u_2 = (node_vector[i + k + 1] - u) / \
            length2 * Bspline(i + 1, k - 1, u, node_vector)
        Nik_u = Nik_u_1 + Nik_u_2

    return Nik_u


def U_uniform(n, k):
    t = np.linspace(0, 1, n + k + 2, endpoint=True)
    return t


def U_quasi_uniform(n, k):
    '''
        准均匀B样条的节点向量计算, n+1个控制节点,k次B样条
    '''
    t = np.linspace(0, 1, n - k + 2, endpoint=True)  # 内结点 均匀分布
    t = np.append(np.zeros(k), t)  # 左边 k个结点 置0
    t = np.append(t, np.ones(k))  # 右边 k个结点 置1
    return t


def U_piecewise_Bezier(n, k):
    # 分段Bezier曲线的节点向量计算，共n+1个控制顶点，k次B样条
    # 分段Bezier端节点重复度为k+1，内间节点重复度为k,且满足n/k为正整数

    # 0...k  k+1...n+1  n+2...n+k+1
    if (n % k) == 0 and (k % 1) == 0 and k > 1:
        node_vector = np.zeros(n + k + 2)
        node_vector[n + 2: n + k + 1] = 1  # 右端节点置1

        piecewise = n / k
        flag = 0
        if piecewise > 1:
            for i in range(piecewise - 1):  # 共 piecewise-1组
                for j in range(k + 1):  # k 重复度
                    node_vector[k + 1 + flag * k + j] = (i + 1) / piecewise
                flag += 1
        else:
            print("error")
    return node_vector


def U_quasi_uniform_old(n, k):
    '''
        准均匀B样条的节点向量计算, n+1个控制节点,k次B样条
    '''

    node_vector = np.zeros(n + k + 2)
    # 内结点 n-k 个 段数 n-k+1
    piecewise = n - k + 1  # 曲线的段数
    if piecewise == 1:  # 只有一段曲线时, n = k   0...n  n+1...n+k+1
        for i in range(n + 1, n + k + 2):
            node_vector[i] = 1

    # 0...k k+1...n+1 n+2...n+k+1
    else:
        flag = 1
        while flag != piecewise:
            node_vector[k + flag] = node_vector[k - 1 + flag] + 1 / piecewise
            flag = flag + 1

        node_vector[n + 1:n + k + 2] = 1

    return node_vector


# ctr =np.array( [(3 , 1), (2.5, 4), (0, 1), (-2.5, 4),
#                 (-3, 0), (-2.5, -4), (0, -1), (2.5, -4), (3, -1),])

# ctr = np.array([(3, 4), (2.5, 7), (0, 1), (-2.5, 4),
#                 (-3, 0), (-2.5, -4), (0, 8), (2.5, -4), (3, -1), ])

ctr = np.array([[50.,  25.],
                [59.,  12.],
                [50.,  10.],
                [57.,   2.],
                [40.,   4.],
                [40.,   14.]])

color = ['r', 'y', 'w']

x = ctr[:, 0]
y = ctr[:, 1]

# uncomment both lines for a closed curve
# x=np.append(x,[x[0]])
# y=np.append(y,[y[0]])

l = len(x)
n = l - 1
k = 3

# 均匀B样条
# ---------------------------uniform---------------


def bspline_uniform(n, k):
    node_vector = U_uniform(n, k)  # n+k+2
    # n = t-k-1 =>　n+1?
    Nik = np.zeros((n + 1, 1))
    P_u_x = list()
    P_u_y = list()

    for u in np.linspace(k / (n + k + 1), (n + 1) / (n + k + 1), 500, endpoint=True):
            # for u = 0 : 0.005 : 1
        for i in range(0, n + 1, 1):
            Nik[i, :] = Bspline(i, k, u, node_vector)

        p_u = np.dot(ctr.T, Nik)  # 曲线上点的坐标
        P_u_x.append(p_u[0, 0])  # 所有点的横坐标
        P_u_y.append(p_u[1, 0])  # 所有点的纵坐标

    P_u_x = np.asarray(P_u_x)
    P_u_y = np.asarray(P_u_y)
    plt.plot(P_u_x, P_u_y, "g-", linewidth=2.0, label='B-spline uniform')

# 准均匀


def bspline_quasi(n, k):
    t = U_quasi_uniform(n, k)
    tck_quasi = [t, [x, y], k]
    u3 = np.linspace(0, 1, (max(l * 2, 70)), endpoint=True)
    out_quasi = interpolate.splev(u3, tck_quasi)
    plt.plot(out_quasi[0], out_quasi[1], color[k - 3],
             linewidth=2.0, label='B-spline quasi degree ' + str(k))


def main():
    # 控制点及连线
    plt.plot(x, y, 'k--', label='Control polygon',
             marker='o', markerfacecolor='red')
    # plt.plot(x,y,'ro',label='Control points only')
    bspline_uniform(n, k)
    bspline_quasi(n, k)
    bspline_quasi(n, k + 1)

    plt.legend(loc='best')
    plt.axis([min(x) - 1, max(x) + 1, min(y) - 1, max(y) + 1])
    plt.title(' B-spline curve evaluation')
    # plt.show()
    plt.pause(150)
    plt.close()

if __name__ == '__main__':
    main()
