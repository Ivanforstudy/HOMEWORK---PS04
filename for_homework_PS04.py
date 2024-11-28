
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
browser = webdriver.Chrome()
driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера (например, Chrome)
driver = webdriver.Chrome()
base_url = "https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B8_(%D1%80%D0%BE%D0%B4)"  # Замените на нужный URL
driver.get(base_url)

def main():
    while True:
        # Предлагаем пользователю три варианта действий
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Ваш выбор (1/2/3): ")

        if choice == '1':
            # Листаем параграфы (например, можно добавить код для отображения параграфов)
            print("Листаем параграфы...")  # Замените на нужный код

        elif choice == '2':
            # Получаем список связанных страниц
            related_links = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/wiki/"]')
            print("\nСвязанные страницы:")

            for i, link in enumerate(related_links):
                print(f"{i + 1}. {link.text}")

            try:
                related_choice = int(input("Выберите номер страницы для перехода: ")) - 1
                if 0 <= related_choice < len(related_links):
                    related_page = related_links[related_choice]
                    driver.get(base_url + related_page.get_attribute('href').split('/')[-1])
                    time.sleep(2)  # Ждем загрузки новой страницы
                else:
                    print("Некорректный выбор.")

            except ValueError:
                print("Ошибка: некорректный ввод.")

        elif choice == '3':
            print("Выход из программы.")
            break  # Правильно использовать break в цикле.

        else:
            print("Некорректный выбор.")

    driver.quit()  # Закрытие



if __name__ == "__main__":  # Правильный синтаксис для проверки имени модуля
    main()
