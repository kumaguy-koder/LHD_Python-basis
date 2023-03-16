import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

if __name__ == '__main__':
    # 出力
    # print("Hologram design")

    # ------------------------------------------------------------
    # Numpyを使ってみる その1　リストから配列
    # data1 = [1, 2, 3]
    # arr1 = np.array(data1)
    #
    # data2 = [[1, 2, 3], [4, 5, 6]]
    # arr2 = np.array(data2)
    #
    # print("arr1")
    # print(arr1)
    # print("arr2")
    # print(arr2)

    # ------------------------------------------------------------
    # Numpyを使ってみる その２ ゼロ配列
    # arr1 = np.zeros(10)
    # print("arr1")
    # print(arr1)
    #
    # arr2 = np.zeros((3, 3))
    # print("arr2")
    # print(arr2)
    #
    # a = np.array([[1, 2, 3], [4, 5, 6]])
    # arr3 = np.zeros_like(a)
    # print("arr3")
    # print(arr3)

    # ------------------------------------------------------------
    # Numpyを使ってみる その３ ndarray要素アクセス
    # arr1 = np.array([1, 2, 3, 4, 5, 6])
    # print("arr1: " + str(arr1))
    # print("arr1[1]: " + str(arr1[1]))
    #
    # arr1[1] = 1
    # print("arr1: " + str(arr1))
    #
    # arr2 = arr1[2:]
    # print("arr2: " + str(arr2))
    #
    # arr3 = arr1[:2]
    # print("arr3: " + str(arr3))
    #
    # arr4 = arr1[arr1 > 4]
    # print("arr4: " + str(arr4))

    # ------------------------------------------------------------
    # Numpyを使ってみる その4 演算
    # arr1 = np.array([1, 2, 3])
    # arr2 = arr1 * 2
    # print("arr2: " + str(arr2))
    #
    # arr3 = np.array([4, 5, 6])
    # arr4 = arr1 + arr3
    # print("arr4: " + str(arr4))

    # ------------------------------------------------------------
    # Matplotを使ってみる その1　散布図
    # x = np.random.randint(50, size=100)
    # y = np.random.randint(50, size=100)
    #
    # plt.scatter(x, y)
    # plt.show()

    # ------------------------------------------------------------
    # Matplotを使ってみる その2 sin/cos
    x = np.arange(-2*np.pi, 2*np.pi, np.pi/50)

    s = np.sin(x)
    c = np.cos(x)

    plt.title("sin / cos")
    plt.xlabel("rad")
    plt.ylabel("value")
    plt.grid("true")

    #plt.plot(x, s, label="sin")
    plt.plot(x, c, label="cos")
    plt.legend()
    
    plt.savefig("./graph.eps")
    plt.show()

    # ------------------------------------------------------------
    # Pillowを使ってみる　その１　入力
    # img = Image.open("./bird2.bmp")
    # img_np = np.array(img)
    #
    # print("画素値:")
    # print(img_np)
    # print("データタイプ: " + str(type(img_np)))
    # print("データ形状: " + str(img_np.shape))
    # print("全画素数: " + str(img_np.size))

    # ------------------------------------------------------------
    # Pillowを使ってみる　その２　表示
    # img = Image.open("./bird2.bmp")
    # img_np = np.array(img)
    #
    # # img_np[:, :, 0] = 0
    # # img_np[:, :, 1] = 0
    #
    # img_np_R = img_np[:, :, 0]
    # img_np_G = img_np[:, :, 1]
    # img_np_B = img_np[:, :, 2]
    #
    # fig = plt.figure()
    #
    # ax1 = fig.add_subplot(2, 2, 1)
    # ax1.set_title("Original")
    # ax1.imshow(img_np)
    #
    # ax2 = fig.add_subplot(2, 2, 2)
    # ax2.set_title("R")
    # ax2.imshow(img_np_R)
    #
    # ax3 = fig.add_subplot(2, 2, 3)
    # ax3.set_title("G")
    # ax3.imshow(img_np_G)
    #
    # ax4 = fig.add_subplot(2, 2, 4)
    # ax4.set_title("B")
    # ax4.imshow(img_np_B)
    #
    # plt.show()

