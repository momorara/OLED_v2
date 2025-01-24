
#!/usr/bin/python

"""
###########################################################################
# OLEDに画像を表示

2024/03/02  start
2024/03/03  pngファイルをOLED上に表示し、白黒反転します。
2025/01/24  独自ライブラリに対応
############################################################################
"""

import lib_oled
import time

def oled_image(image_path):
    # BMP画像を読み込み
    bitmap_image = lib_oled.bitmap_to_image(image_path)
    # BMP画像を描画
    lib_oled.draw_bitmap( 0, 0, bitmap_image)
    # キャンバスをOLEDに表示
    lib_oled.disp_oled()

# #main function
def main():
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')

    # OLED初期化
    lib_oled.oled_ini()
    # oledをクリア
    lib_oled.clear_oled()
    # 描画領域をクリア
    lib_oled.clear_canvas()

    # 画像ファイルの読み込み
    image_path = "kingyo.png"
    # 画像の表示
    oled_image(image_path)
    time.sleep(1)
    lib_oled.clear_oled()
    lib_oled.clear_canvas()

    # 画像ファイルの読み込み
    image_path = "shiyachi.png"
    # 画像の表示
    oled_image(image_path)
    time.sleep(1)
    lib_oled.clear_oled()
    lib_oled.clear_canvas()

    # 画像ファイルの読み込み
    image_path = "tonbo.png"
    # 画像の表示
    oled_image(image_path)
    time.sleep(1)

    lib_oled.clear_oled()
    lib_oled.clear_canvas()


if __name__ == '__main__':
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        pass
    except ValueError as e:
        print(e)