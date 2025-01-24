
#!/usr/bin/python

"""
###########################################################################
# OLEDデモ ランダムな図形

2024/03/02  start
2025/01/24  独自ライブラリに対応
############################################################################
"""

import lib_oled
import time
import random

# 描画対象の図形の数
num_shapes = 30

def main():
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')

    # OLED初期化
    lib_oled.oled_ini()
    # oledをクリア
    lib_oled.clear_oled()
    # 描画領域をクリア
    lib_oled.clear_canvas()

    # デモプログラムの実行

    for _ in range(5):  # 5回のアニメーションループ
        for _ in range(num_shapes):
            # ランダムな座標と白または黒の色で直線、矩形、円を描画
            x, y = random.randint(0, 127), random.randint(0, 50)
            shape_type = random.choice(["line", "rectangle", "point", "point"])
            dx,dy = random.randint(-20, 20),random.randint(-10, 10)
            if shape_type == "line":
                lib_oled.line(x, y, x + dx, y +dy)
            elif shape_type == "rectangle":
                lib_oled.square(x, y, x + dx, y + dy,0)
            elif shape_type == "point":
                lib_oled.point(x, y)
            lib_oled.disp_oled()

        time.sleep(0.2)  # アニメーションのためのウェイト



if __name__ == '__main__':
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        pass
    except ValueError as e:
        print(e)
