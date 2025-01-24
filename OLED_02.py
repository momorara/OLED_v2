
#!/usr/bin/python

"""
###########################################################################
# OLEDにTTフォントを使って文字を表示

2024/03/03  start
2024/03/05  5から32ドットの文字を順次表示
2025/01/24  独自ライブラリに対応
############################################################################
"""

import lib_oled
import time


#main function
def main():

    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')
    print("外部フォントで表示します。")
    print("30ドット以内の文字を表示できます。")

    # OLED初期化
    lib_oled.oled_ini()
    # oledをクリア
    lib_oled.clear_oled()
    # 描画領域をクリア
    lib_oled.clear_canvas()
    
    for size in range(5,33):
        font = lib_oled.set_font("fonts-japanese-gothic.ttf", size)
        text = str(size) + "ドット"
        if size < 18:
            text = text + "の文字"
        print("文字サイズ",size)
        # テキストをキャンバスに書く
        lib_oled.text(0,0,text,font)
        # キャンバスの情報をOLEDに転送
        lib_oled.disp_oled()
        # キャンバスをクリア
        lib_oled.clear_canvas()
        time.sleep(1)
    time.sleep(5)


if __name__ == '__main__':
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        pass
    except ValueError as e:
        print(e)