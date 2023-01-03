from django.core.management.base import BaseCommand
from reviews.models import Reviewinfo
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('reviewsALL.csv',  encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                review = Reviewinfo(
                    title=row['Title'],
                    author=row['Author'],
                    content=row['Content']
                )
                review.save()
