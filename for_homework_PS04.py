from selenium import webdriver

import wikipediaapi

def main():
    # Указываем пользовательский агент
    user_agent = "MyWikipediaApp/1.0 (https://example.com; myemail@example.com)"
    wiki_wiki = wikipediaapi.Wikipedia('ru', user_agent=user_agent)  # Используем русскую Википедию

    while True:
        # 1. Спрашиваем у пользователя первоначальный запрос
        query = input("Введите запрос для поиска на Википедии (или 'выход' для завершения): ")
        if query.lower() == 'выход':
            break

        # 2. Переход по первоначальному запросу в Википедии
        page = wiki_wiki.page(query)

        if not page.exists():
            print("Страница не найдена. Попробуйте другой запрос.")
            continue

        # 3. Предлагаем пользователю три варианта действий
        while True:
            print("\nСтатья:", page.title)
            print(page.text[:1000])  # Выводим первые 1000 символов статьи
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")

            choice = input("Ваш выбор: ")

            if choice == '1':
                # Листаем параграфы
                print("\nСодержимое статьи:")
                for section in page.sections:
                    print(section.title)
                    print(section.text)
                break  # Возвращаемся к основному меню после просмотра

            elif choice == '2':
                # Перейти на одну из связанных страниц
                print("\nСвязанные статьи:")
                related_pages = page.links
                for idx, related_page in enumerate(related_pages.keys()):
                    print(f"{idx + 1}. {related_page}")

                related_choice = input("Введите номер статьи для перехода (или 'назад' для возврата): ")
                if related_choice.isdigit() and 1 <= int(related_choice) <= len(related_pages):
                    page = related_pages[list(related_pages.keys())[int(related_choice) - 1]]
                elif related_choice.lower() == 'назад':
                    break
                else:
                    print("Неверный ввод. Попробуйте снова.")

            elif choice == '3':
                print("Выход из программы.")
                return  # Завершаем программу

            else:
                print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()



