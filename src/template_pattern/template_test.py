"""
    템플릿 패턴 테스트

    Description:
        템플릿 패턴 테스트를 위한 코드
    Author:
        Name: Junhyeok Yang
        Email: surfing2003@naver.com
"""
from caffeinebeverage import Coffee, Tea

if __name__ == "__main__":
    tea = Tea()
    coffee = Coffee()

    print("홍차 준비중...")
    tea.prepare_recipe()

    print("커피 준비중...")
    coffee.prepare_recipe()
