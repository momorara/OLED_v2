
#!/usr/bin/python

"""
###########################################################################
# OLEDに四角、点、線を表示

2024/03/02  start
2024/03/05  デモを増やした
2025/01/24  独自ライブラリに対応
############################################################################
"""

import lib_oled
import time

def main():
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')

    # OLED初期化
    lib_oled.oled_ini()
    # oledをクリア
    lib_oled.clear_oled()
    # 描画領域をクリア
    lib_oled.clear_canvas()

    print("四角を描画")
    # 四角をキャンバスに書く
    lib_oled.square(0, 0, 127, 31,0)
    lib_oled.disp_oled()
    time.sleep(1)
    print("塗りつぶし")
    lib_oled.square(0, 0, 127, 31,1)
    lib_oled.disp_oled()
    time.sleep(1)

    lib_oled.clear_canvas()
    print("四角を描画 移動")
    for x in range(0,127,5):
        lib_oled.square(0, 10, x, 21,1)
        lib_oled.disp_oled()
        time.sleep(0.05)
    time.sleep(1)
    for x in range(0,127,5):
        xx = 0
        # if x > 20:
            # xx = x -20
        lib_oled.square(xx ,10, x, 21,0)
        lib_oled.disp_oled()
        time.sleep(0.05)
    time.sleep(1)

    lib_oled.clear_canvas()
    lib_oled.clear_oled()

    print("点を描画")
    lib_oled.point(0, 0)
    lib_oled.disp_oled()
    time.sleep(1)
    lib_oled.point(127, 0)
    lib_oled.disp_oled()
    time.sleep(1)
    lib_oled.point(0, 31)
    lib_oled.disp_oled()
    time.sleep(1)
    lib_oled.point(127, 31)
    lib_oled.disp_oled()
    time.sleep(1)

    lib_oled.clear_canvas()
    lib_oled.clear_oled()

    print("線を描画")
    lib_oled.line(0, 0, 127, 31)
    lib_oled.disp_oled()
    time.sleep(1)
    lib_oled.line(127, 0, 0, 31)
    lib_oled.disp_oled()
    time.sleep(3)

    lib_oled.clear_canvas()
    lib_oled.clear_oled()

if __name__ == '__main__':
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        pass
    except ValueError as e:
        print(e)