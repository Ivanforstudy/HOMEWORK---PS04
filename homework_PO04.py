
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def browse_wikipedia():
    browser = webdriver.Chrome()

    while True:
        # 1. Спрашиваем у пользователя первоначальный запрос
        search_query = input("Введите запрос для поиска на Википедии (или 'выход' для завершения): ")
        if search_query.lower() == 'выход':
            break

        # 2. Переход по первоначальному запросу в Википедии
        search_url = f"https://ru.wikipedia.org/wiki/{search_query}"
        browser.get(search_url)

        # Проверяем, доступна ли страница
        if "404" in browser.title:
            print("Страница не найдена. Попробуйте другой запрос.")
            continue

        while True:
            # 3. Предлагаем пользователю три варианта действий
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")
            choice = input("Ваш выбор (1/2/3): ")

            if choice == '1':
                # Листаем параграфы статьи
                paragraphs = browser.find_elements(By.TAG_NAME, "p")
                for paragraph in paragraphs:
                    print(paragraph.text)
                    input("Нажмите Enter для продолжения...")

            elif choice == '2':
                # Переход на одну из связанных страниц
                links = browser.find_elements(By.TAG_NAME, "a")
                related_links = [link for link in links if
                                 link.get_attribute('href') and '/wiki/' in link.get_attribute('href')]

                if not related_links:
                    print("Нет связанных страниц.")
                    continue

                print("Выберите связанную страницу:")


                for index, link in enumerate(related_links[:5], start=1):  # Ограничение до 5 связанных страниц
                    print(f"{index}. {link.text}")

                link_choice = input("Введите номер страницы для перехода (или 'назад' для возврата): ")

                if link_choice.lower() == 'назад':
                    continue

                try:
                    link_index = int(link_choice) - 1
                    if 0 <= link_index < len(related_links):
                        browser.get(related_links[link_index].get_attribute('href'))
                    else:
                        print("Неверный номер. Попробуйте снова.")
                except ValueError:
                    print("Пожалуйста, введите номер.")

            elif choice == '3':
                browser.quit()
                return

            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

    browser.quit()


if __name__ == "__main__":
    browse_wikipedia()


