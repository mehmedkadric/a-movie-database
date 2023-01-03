from django.core.management.base import BaseCommand
from reviews.models import Reviewinfo
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('test2.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                review = Reviewinfo(
                    title=row['title'],
                    author=row['author'],
                    content=row['content']
                )
                review.save()
