from flask import url_for
from flask_testing import TestCase

from app import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimals(TestBase):
    def test_animal(self):
        animals = [b"Lion", b"Mouse", b"Cat", b"Horse", b"Snake"]
        response = self.client.get(url_for('animal'))
        self.assertIn(response.data, animals)

    def test_noise_lion(self):
        response = self.client.post(
            url_for('noise'),
            data="Lion",
            follow_redirects=True
        )
        self.assertIn(b'ROAR', response.data)
    
    def test_noise_snake(self):
        response = self.client.post(
            url_for('noise'),
            data="Snake",
            follow_redirects=True
        )
        self.assertIn(b'HISS', response.data)
    
    def test_noise_cat(self):
        response = self.client.post(
            url_for('noise'),
            data="Cat",
            follow_redirects=True
        )
        self.assertIn(b'MEOW', response.data)
    
    def test_noise_horse(self):
        response = self.client.post(
            url_for('noise'),
            data="Horse",
            follow_redirects=True
        )
        self.assertIn(b'NEIGH', response.data)
    
    def test_noise_mouse(self):
        response = self.client.post(
            url_for('noise'),
            data="Mouse",
            follow_redirects=True
        )
        self.assertIn(b'squeak', response.data)