



import wikipediaapi
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Исправлено: правильный импорт Keys
browser = webdriver.Chrome()
driver = webdriver.Chrome()

# Инициализация драйвера (например, Chrome)
def main():
    browser.get("https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%9F%D0%BE%D1%80%D0%BE%D0%B4%D1%8B_%D0%BA%D0%BE%D1%88%D0%B5%D0%BA")
    time.sleep(5)
    wiki_wiki = wikipediaapi.Wikipedia('ru')  # Используем русскую Википедию
    category = "Категория:Породы_кошек"
    category_page = wiki_wiki.page(category)

    if not category_page.exists():
        print("Категория не найдена.")
        return

    # Получаем связанные страницы из категории
    related_pages = category_page.categorymembers

    while True:
        # 1. Выводим список пород кошек
        print("\nСписок пород кошек:")
        for idx, related_page in enumerate(related_pages):
            print(f"{idx + 1}. {related_page.title}")

        choice = input("Введите номер породы для просмотра (или 'выход' для завершения): ")

        if choice.lower() == 'выход':
            break

        if choice.isdigit() and 1 <= int(choice) <= len(related_pages):
            page = related_pages[int(choice) - 1]
            print("\nСтатья:", page.title)
            print(page.text[:1000])  # Выводим первые 1000 символов статьи

            while True:
                print("\nВыберите действие для статьи:")
                print("1. Листать параграфы текущей статьи")
                print("2. Перейти на одну из связанных страниц")
                print("3. Вернуться к списку пород кошек")
                print("4. Выйти из программы")
                action_choice = input("Ваш выбор: ")

                if action_choice == '1':
                    print("\nСодержимое статьи:")
                    for section in page.sections:

                     print(section.title)
                     print(section.text)
                     break

                elif action_choice == '2':
                   related_pages = page.links

                   print("\nСвязанные статьи:")
                   for idx, related_page in enumerate(related_pages.keys()):
                     print(f"{idx + 1}. {related_page}")

                   related_choice = input("Введите номер статьи для перехода (или 'назад' для возврата): ")
                   if related_choice.isdigit() and 1 <= int(related_choice) <= len(related_pages):
                      page = related_pages[list(related_pages.keys())[int(related_choice) - 1]]
                   elif related_choice.lower() == 'назад':
                     break
                   else:
                     print("Неверный ввод. Попробуйте снова.")

                elif action_choice == '3':
                  break

                elif action_choice == '4':
                  print("Выход из программы.")
                  return  # Завершаем программу

                else:
                  print("Неверный выбор. Пожалуйста, выберите 1, 2, 3 или 4.")

if __name__ == "__main__":
    main()