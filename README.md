# SELENIUM WEBDRIVER PYTHON BINDINGS


### 1. Instalation and configuration:

   ```
   ### A. Instalujemy pakiet Selenium
   $ Pip Installs Packages

   # sprawdzamy wersje pip   
   $ Pip --version

   # instalacja menadżera pip (w razie jego braku) należy wykonać jako superużytownik:
   $ sudo apt install python3-pip

   # Instalacja Selenium:
   $ pip3 install selenium

   ### B. Pakiet Selenium do współpracy z przeglądarką potrzebuje sterownika:
   Chrome   -   [https://sites.google.com/a/chromium.org/chromedriver/downloads)    
   Opera    -   [https://github.com/operasoftware/operachromiumdriver/releases)
   Firefox  -   [https://github.com/mozilla/geckodriver/releases)
   Safari   -   [https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
   IE       -   [https://selenium-release.storage.googleapis.com/index.html)

   # Chrome potrzebuje sterownika o nazwie chromedriver.

   # Po ściągnięciu archiwum dostosowanego do systemu operacyjnego, rozpakowujemy je:
   $ unzip chromedriver_linux64.zip

   # Następnie przenosimy rozpakowany plik do katalogu /usr/local/bin/ :
   $ mv chromedriver /usr/local/bin

   # W celu instalacji pozostałych sterowników postępujemy analogicznie.

   ```

### 2. Run test:

   ```
   # Uruchamiamy test z nazwę pliku: python3 <nazwa_pliky.py>
   $ python3 selenju-P574.py
   ```

### 3. Documentacja

- [https://selenium-python.readthedocs.io/)
