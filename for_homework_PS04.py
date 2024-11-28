
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys



# Предлагаем пользователю три варианта действий
print("\nВыберите действие:")
print("1. Листать параграфы текущей статьи")
print("2. Перейти на одну из связанных страниц")
print("3. Выйти из программы")

choice = input("Ваш выбор (1/2/3): ")

if choice == '1':
    # Листаем параграфы (по сути, это просто повторный вывод)
    continue
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
break
else:
print("Некорректный выбор.")

driver.quit()

if __name__ == "__main__":
    main()
