from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class FormularioReservaTest(LiveServerTestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ejecuta sin abrir navegador
        chrome_options.add_argument("--no-sandbox")  # Necesario en contenedores
        chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemas en entornos limitados
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_formulario_reserva_carga(self):
        self.browser.get(f"{self.live_server_url}/polideportivo/1/cancha/1/reservar/")

        input_nombre = self.browser.find_element(By.NAME, "nombre")
        input_email = self.browser.find_element(By.NAME, "email")
        boton = self.browser.find_element(By.TAG_NAME, "button")

        self.assertTrue(input_nombre.is_displayed(), "El campo 'nombre' no se muestra")
        self.assertTrue(input_email.is_displayed(), "El campo 'email' no se muestra")
        self.assertIn("Reservar", boton.text, "El botón no contiene el texto 'Reservar'")
