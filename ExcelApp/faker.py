from faker import Faker
fake = Faker()

from .models import *
import random


def generate_random_data(n=20):

    for i in range(0, n):
        Student.objects.create(
            name = fake.name(),
            father_name = fake.name(),
            address = fake.address(),
            age = random.randint(18, 40)
        )

    return True
