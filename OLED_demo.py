
#!/usr/bin/python

"""
###########################################################################

2024/03/03  lib_oledを使うデモ

############################################################################
"""

import lib_oled
import time
from PIL import Image

#main function
def main():
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')

    line1 = "01234567890123456789"
    line2 = "abcdefghijklmnopqrstu"
    line3 = "ABCDEFGHIJKLMNOPQRSTU"
    # OLED初期化
    lib_oled.oled_ini()
    # oledをクリア
    lib_oled.clear_oled()
    # 描画領域をクリア
    lib_oled.clear_canvas()

    # フォント設定
    font = lib_oled.set_font("DejaVuSans.ttf", 10)
    # テキストをキャンバスに書く
    lib_oled.text(0,0,line1,font)
    lib_oled.text(0,11,line2,font)
    lib_oled.text(0,22,line3,font)
    # キャンバスの情報をOLEDに転送
    lib_oled.disp_oled()
    time.sleep(1)

    lib_oled.square(0, 0, 127, 31,0)
    lib_oled.disp_oled()
    time.sleep(1)

    lib_oled.point(50,10)
    lib_oled.disp_oled()
    time.sleep(1)

    lib_oled.line(127, 0, 0, 31)
    lib_oled.disp_oled()
    time.sleep(1)

    bitmap_image = lib_oled.bitmap_to_image("tonbo.png")
    lib_oled.draw_bitmap(0, 0, bitmap_image)
    lib_oled.disp_oled()
    time.sleep(3)
    lib_oled.clear_oled()

if __name__ == '__main__':
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        pass
    except ValueError as e:
        print(e)
