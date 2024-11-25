
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


def list_paragraphs(browser):
    """Функция для листания параграфов статьи."""
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input("Нажмите Enter, чтобы продолжить к следующему параграфу...")


def search_article(browser, query):
    """Функция для поиска статьи по запросу."""
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.clear()  # Очищаем поле поиска
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Даем время загрузиться странице


def navigate_related_article(browser):
    """Функция для перехода на связанную статью."""
    related_links = browser.find_elements(By.XPATH, "//div[@class='hatnote navigation-not-searchable']//a")

    if not related_links:
        print("Нет связанных статей.")
        return None

    print("Связанные статьи:")
    for index, link in enumerate(related_links):
        print(f"{index + 1}. {link.text}")

    choice = int(input("Выберите номер статьи для перехода (или 0 для выхода): "))
    if choice == 0:
        return None
    elif 1 <= choice <= len(related_links):
        related_links[choice - 1].click()
        time.sleep(2)  # Даем время загрузиться странице
        return browser
    else:
        print("Неверный выбор.")
        return None


def main():
    browser = webdriver.Chrome()
    try:
        initial_query = input("Введите ваш запрос для поиска в Википедии: ")
        browser.get("https://ru.wikipedia.org")
        time.sleep(2)

        # Ищем статью
        search_article(browser, initial_query)

        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы статьи")
            print("2. Перейти на связанную статью")
            print("3. Выйти из программы")

            choice = input("Ваш выбор: ")
            if choice == "1":
                list_paragraphs(browser)
            elif choice == "2":
              if navigate_related_article(browser) is None:

                break
            elif choice == "3":
              print("Выход из программы.")
              break
        else:
            print("Неверный выбор. Пожалуйста, выберите еще раз.")
    finally:
      browser.quit()

if __name__ == "__main__":
    main()

