import pytest
import pages


class TestFooter:

    #Проверка на соответствие текста кнопки "Войти"
    def test_enter_button_text(self, page):
        pages.index_page.open_index_page(page)
        actual_result = pages.index_page.get_text_from_enter_button(page)
        assert actual_result == 'Войти', f'Неверный текст в кнопке "Войти" - {actual_result}'

    #Проверка на наличие кнопки "войти"
    def test_enter_button_on_the_page(self,page):
        pages.index_page.open_index_page(page)
        button_locator = page.locator('button.btn:text("Войти")')
        assert button_locator.is_visible(), "Button 'Войти' not found or not visible."


    #Проверка на соответствие текста ссылки "Забыли пароль?"
    def test_forgot_password_text(self, page):
        pages.index_page.open_index_page(page)
        link_locator = page.locator('span.link')
        link_text = link_locator.inner_text()
        assert link_text == "Забыли пароль?", f'Expected link text to be "Забыли пароль?", but got "{link_text}"'

    #Проверка на наличие ссылки восстановления пароля "Забыли пароль?"
    def test_forgot_password_link_on_the_page(self,page):
        pages.index_page.open_index_page(page)
        link_locator = page.locator('span.link')
        assert link_locator.is_visible(), "Button 'Войти' not found or not visible."
