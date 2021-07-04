# Import niezbędnych bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# DANE testowe
valid_first_name = "Marcin"
valid_last_name = "Nowak"
valid_country = "Polska"
valid_phone_number = "123456789"
valid_email = "wsb.pl@wsb"
valid_password = "Qwert347626@"
valid_register_country = "Filipiny"

gender = "male"

invalid_phone = "dsfg"
invalid_email = "marcin.nowak123gmail.com"

class WizzairRegistration(unittest.TestCase):
    # Warunki wstępne testów
    def setUp(self):
        print("Przygotowanie testu")
        # Tutaj właczymy przeglądarkę
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        # Wejdziemy na stronę wizzaira
        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl/#/')

    # Instrukcje po każdym teście
    def tearDown(self):
        print("Sprzątanie po teście")
        # Wyłączamy przeglądarkę
        self.driver.quit()

    # Metody testowe - zaczynają się od słowa "test"
    def testInvalidEmail(self):
        print("Prawdziwy test")
        # Tutaj będziemy wykonywać KROKI

        # KROK 1 : Kliknij "Zaloguj"
        driver = self.driver
        zaloguj_btn = self.driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        zaloguj_btn.click()
        #print(type(zaloguj_btn))
        # Poczekajmy 15 sekund, żeby zdążyć zauważyć co się dzieje
        #time.sleep(15)

        # KROK 2 : Kliknij „Rejestracja”
        driver.find_element_by_css_selector('button[data-test="registration"]').click()

        # KROK 3 : Wpisz imię
        name_input = driver.find_element_by_name('firstName')
        name_input.send_keys(valid_first_name)

        # KROK4: Wpisz nazwisko
        lastname_input = driver.find_element_by_name('lastName')
        lastname_input.send_keys(valid_last_name)

        # KROK 5 : Wybierz płeć
        if gender == "female":
            lastname_input.click()
            # Wybierz kobietę
            driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]').click()
        else:
            # Odsłoń mężczyznę
            name_input.click()
            # Wybierz mężcyznę
            driver.find_element_by_xpath('//label[@data-test="register-gendermale"]').click()

        # KROK 6 : Wpisz kod kraju
        driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]').click()
        cc_input = driver.find_element_by_name('phone-number-country-code')
        cc_input.send_keys(valid_country, Keys.RETURN)

        # KROK 7: Wpisz nr telefonu
        phone_input = driver.find_element_by_name('digits-phone-number-input')
        phone_input.send_keys(valid_phone_number)

        # KROK 8 : Wpisz email
        phonenumber_input = driver.find_element_by_name('email')
        phonenumber_input.send_keys(valid_email)

        # KROK 9 : Wpisz hasło
        phonenumber_input = driver.find_element_by_name('password')
        phonenumber_input.send_keys(valid_password)

        # KROK 10 : Wpisz kod kraju
        #driver.find_element_by_xpath('//div[@data-test="booking-register-country"]').click()
        country_input = driver.find_element_by_name('country-select')
        country_input.send_keys(valid_register_country, Keys.RETURN)

        # KROK 11 : Zaznacz checkboxy zgód
        #driver.find_element_by_css_selector('//input[@data-test="registration-privacy-policy-checkbox"]').click()
        #driver.find_element_by_css_selector('//input[@data-test="registration-wizz-account-policy-checkbox"]').click()

        #### UWAGA! TUTAJ BĘDZIE TEST !!!
        # Wyszukaj wszystkie możliwe błędy
        # ..find_elements... zwraca LISTĘ WebElementów
        possible_errors = driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        # !!!!!!!!!!!!! Sprawdź, które są widoczne
        # Pusta lista na widoczne błędy
        visible_errors = []
        # Dla każdego błędu w liście possible_errors
        for error in possible_errors:
            # Jelsi błąd jest widoczny
            if error.is_displayed():
                # Dodaj go do listy widocznych
                visible_errors.append(error)

        # !!!!!!!!!!!!!!!! Sprawdż, czy widoczny jest tylko jeden z nich
        # Czy lista visible_errors zawiera wyłacznie jeden element
        assert len(visible_errors) == 1 # "czysty Python"
        self.assertEqual(len(visible_errors), 1) # metoda unittestowa (prawie to samo)
        # !!!!!!!!!!!!!!!! Sprawdź, czy treść jest poprawna: "Nieprawidłowy adres e-mail"
        print("Tekst błędu na stronie: ", visible_errors[0].text)
        assert visible_errors[0].text == "Nieprawidłowy adres e-mail"
        self.assertEqual(visible_errors[0].text, "Nieprawidłowy adres e-mail") # (prawie to samo co czysty Python)

        time.sleep(4)

    def testInvalidPhoneNumber(self):
        print("Prawdziwy test")

    # Tutaj będziemy wykonywać KROKI przypadku testowego nr 002 Rejestracja nowego użytkownika używając niepoprawnego numeru telefonu

        # KROK 1 : Kliknij "Zaloguj"
        driver = self.driver
        zaloguj_btn = self.driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        zaloguj_btn.click()

        # KROK 2 : Kliknij „Rejestracja”
        driver.find_element_by_css_selector('button[data-test="registration"]').click()

        # KROK 3 : Wpisz imię
        name_input = driver.find_element_by_name('firstName')
        name_input.send_keys(valid_first_name)

        # KROK4: Wpisz nazwisko
        lastname_input = driver.find_element_by_name('lastName')
        lastname_input.send_keys(valid_last_name)

        # KROK 5 : Wybierz płeć
        if gender == "female":
            lastname_input.click()
            # Wybierz kobietę
            driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]').click()
        else:
            # Odsłoń mężczyznę
            name_input.click()
            # Wybierz mężcyznę
            driver.find_element_by_xpath('//label[@data-test="register-gendermale"]').click()

        # KROK 6 : Wpisz kod kraju
        driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]').click()
        cc_input = driver.find_element_by_name('phone-number-country-code')
        cc_input.send_keys(valid_country, Keys.RETURN)

        # KROK 7: Wpisz NIEPOPRAWNY nr telefonu
        phone_input = driver.find_element_by_name('digits-phone-number-input')
        phone_input.send_keys(invalid_phone)

        # KROK 8: Wpisz adres email
        email_input = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        email_input.send_keys(valid_email)

        # KROK 9: Wpisz hasło
        password_input = driver.find_element_by_name('password')
        password_input.send_keys(valid_password)

        # KROK 10: Wpisz narodowość
        nationality_input = driver.find_element_by_name('country-select')
        nationality_input.send_keys(valid_country)

        #### UWAGA! TUTAJ BĘDZIE TEST !!!
        # Wyszukaj wszystkie możliwe błędy
        # ..find_elements... zwraca LISTĘ WebElementów
        possible_errors = driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        # !!!!!!!!!!!!! Sprawdź, które są widoczne
        # Pusta lista na widoczne błędy
        visible_errors = []
        # Dla każdego błędu w liście possible_errors
        for error in possible_errors:
            # Jelsi błąd jest widoczny
            if error.is_displayed():
                # Dodaj go do listy widocznych
                visible_errors.append(error)

        # !!!!!!!!!!!!!!!! Sprawdż, czy widoczny jest tylko jeden z nich
        # Czy lista visible_errors zawiera wyłacznie jeden element
        assert len(visible_errors) == 1  # "czysty Python"
        self.assertEqual(len(visible_errors), 1)  # metoda unittestowa (prawie to samo)
        # !!!!!!!!!!!!!!!! Sprawdź, czy treść jest poprawna: "Nieprawidłowy adres e-mail"
        print("Tekst błędu na stronie: ", visible_errors[0].text)
        assert visible_errors[0].text == "Wpisz właściwy numer telefonu"
        self.assertEqual(visible_errors[0].text, "Wpisz właściwy numer telefonu")  # (prawie to samo co czysty Python)

        time.sleep(4)

# Jeśli uruchamiamy z tego pliku
if __name__=="__main__":
    # Włączamy testy
    unittest.main()
