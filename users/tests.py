from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User, Payments


class UserTestCase(APITestCase):
    def setUp(self):
        self.user = User(email="teat2@example.com")
        self.user.set_password("12345")
        self.user.save()
        self.client.force_authenticate(user=self.user)


    def test_user_create(self):
        url = reverse("users:register")
        data = {"email": "test5@example.com", "password": "12345"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)


    def test_user_retrieve(self):
        url = reverse("users:user-retrieve", args=(self.user.id,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["email"], self.user.email)


    def test_user_update(self):
        url = reverse("users:user-update", args=(self.user.id,))
        data = {
            "email": "test3@example.com"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["email"], "test3@example.com")


    def test_user_delete(self):
        url = reverse("users:user-delete", args=(self.user.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)


    def test_user_list(self):
        url = reverse("users:user-list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {'id': self.user.id,
             'town': None,
             'avatar': None}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class PaymentsTestCase(APITestCase):
    def setUp(self):
        self.user = User(email="test@example.com")
        self.user.set_password("12345")
        self.user.save()
        self.payments = Payments.objects.create(payment_date="2025-01-25", payment_amount="10000.00", payment_method= "credit_card")
        self.client.force_authenticate(user=self.user)

    def test_payment_create(self):
        url = reverse("users:payments-list")
        data = {
            "payment_date": "2025-02-25",
            "payment_amount": "12000.00",
            "payment_method": "credit_card"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payments.objects.all().count(), 2)


    def test_payment_retrieve(self):
        url = reverse("users:payments-detail", args=(self.payments.id,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["payment_date"], self.payments.payment_date.isoformat())

    def test_payment_update(self):
        url = reverse("users:payments-detail", args=(self.payments.id,))
        data = {
            "payment_date": "2025-03-25",
            "payment_amount": "15000.00",
            "payment_method": "cash"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["payment_amount"], "15000.00")


    def test_user_delete(self):
        url = reverse("users:payments-detail", args=(self.payments.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Payments.objects.all().count(), 0)


    def test_payment_list(self):
        url = reverse("users:payments-list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {'payment_date': '2026-01-05',
             'payment_amount': '10000.00',
             'payment_method': 'credit_card'
             }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)





