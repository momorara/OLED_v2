
#!/usr/bin/python

"""
###########################################################################
# OLEDに文字を表示

2024/03/02  start
2024/03/03  OLED組み込みフォントを使用して文字を表紙する。
            ただし、文字が小さく、英数字のみ、反面文字数は多く表示できます。
2025/01/24  独自ライブラリに対応
############################################################################
"""

import lib_oled
import time


#main function
def main():
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')
    print("TTフォントで表示します。")
    line1 = "01234567890123456789"
    line2 = "abcdefghijklmnopqrstu"
    line3 = "ABCDEFGHIJKLMNOPQRSTU"
    print(line1)
    print(line2)
    print(line3)

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



if __name__ == '__main__':
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        pass
    except ValueError as e:
        print(e)
