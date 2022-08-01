"""
    팩토리 메서드 패턴 테스트
    Description:
        팩토리 메서드 패턴 테스트를 위한 코드
    Author:
        Name: Junhyeok Yang
        Email: surfing2003@naver.com
"""
from pizzastore import ChicagoPizzaStore, NYPizzaStore

if __name__ == "__main__":
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.order_pizza("cheese")
    print(f"주문한 {pizza.get_name()}")

    pizza = chicagoStore.order_pizza("cheese")
    print(f"주문한 {pizza.get_name()}")
