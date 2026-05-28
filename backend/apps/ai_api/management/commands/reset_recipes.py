"""
Wipe the Recipe table and re-seed it from fixtures/initial_recipes.json.

Run manually:
    python manage.py reset_recipes

Scheduled nightly via host cron on the EC2 — see deploy notes for the crontab entry.
"""
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.ai_api.models import Recipe


class Command(BaseCommand):
    help = "Delete all Recipe rows and reload from initial_recipes fixture."

    def handle(self, *args, **options):
        with transaction.atomic():
            deleted, _ = Recipe.objects.all().delete()
            self.stdout.write(f"Deleted {deleted} Recipe rows.")
            call_command("loaddata", "initial_recipes", verbosity=1)
        self.stdout.write(self.style.SUCCESS("Recipe table reset complete."))
