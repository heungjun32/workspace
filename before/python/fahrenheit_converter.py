# -*- coding: utf-8 -*-


def main(celsius_value):
    print("본 프로그램은 섭씨를 화씨로로 변환해주는 프로그램입니다")
    print("============================")
    # ===Modify codes below=================

    print("변환하고 싶은 섭씨 온도를 입력해주세요: ") 
    celsius_value = input()
    fahrenheit_value = (float(celsius_value) * 1.8) + 32

    print("섭씨온도: ",celsius_value)
    print("화씨온도: ",fahrenheit_value)
    


    # ======================================
    print("===========================")
    print("프로그램이 종료 되었습니다.")


if __name__ == '__main__':
    # main()
    celsius_value = celsius_value()
    print(celsius_value)
    
