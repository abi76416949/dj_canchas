from django.test import TestCase
from application.servicios import crear_polideportivo

class CrearPolideportivoTest(TestCase):
    def test_creacion_correcta(self):
        poli = crear_polideportivo("Villa", "Av. Siempre Viva", "999999999")
        self.assertEqual(poli.nombre, "Villa")
        self.assertEqual(poli.ubicacion, "Av. Siempre Viva")
        self.assertEqual(poli.contacto, "999999999")
