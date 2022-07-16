from django.core.management.base import BaseCommand, CommandError
import faker
from app1.models import Branch
from faker import Faker
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Create Branch objects'

    def handle(self, *args, **options):
        
        user = User.objects.first()
        fake = Faker()
        

        for _ in range(10):
            Branch.objects.create(
                branch_name = fake.name(),
                location = fake.country(),
                supervisor = user,
                branch_id = fake.random_number(digits=6),

                )

        self.stdout.write(self.style.SUCCESS('Successfully created new branches'))


