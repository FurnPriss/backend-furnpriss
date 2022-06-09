from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
class Registration(APITestCase):
    def test_success(self):
        data = {
            "username": "c2228f2105",
            "email": "c2228f2105@gmail.com",
            "password": "bangkitacademy"
        }
        request = self.client.post("/api/sys-regis/", data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_empty_field(self):
        data = {
            "username": "c2228f2105",
            "email": "",
            "password": "bangkitacademy"
        }
        request = self.client.post("/api/sys-regis/", data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_email_duplicate(self):
        data = {
            "username": "c2228f2105",
            "email": "c2228f2105@gmail.com",
            "password": "bangkitacademy"
        }
        request = self.client.post("/api/sys-regis/", data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

class GenerateCode(APITestCase):
    def test_success(self):
        data = {
            "email": "ccc23@gmail.com",
            "password": "bangkitacademy2022",
            "confirm_password": "bangkitacademy2022"
        }
        request = self.client.post("/api/sys-reset-psw/", data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_empty_field(self):
        data = {
            "email": "ccc23@gmail.com",
            "password": "",
            "confirm_password": ""
        }
        request = self.client.post("/api/sys-reset-psw/", data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_psw_not_same(self):
        data = {
            "email": "ccc23@gmail.com",
            "password": "bangkitacademy2022",
            "confirm_password": "bangkitacademy2020"
        }
        request = self.client.post("/api/sys-reset-psw/", data, format="json")
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_email_not_found(self):
        data = {
            "email": "akhfzz23@gmail.com",
            "password": "bangkitacademy2022",
            "confirm_password": "bangkitacademy2022"
        }
        request = self.client.post("/api/sys-reset-psw/", data)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)
