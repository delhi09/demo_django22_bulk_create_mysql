import csv
import os

from demo.models import Food
from django.conf import settings
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class SampleView(View):
    def get(self, request, *args, **kwargs):
        food_list = []
        with open(
            os.path.join(settings.BASE_DIR, "menu.csv"), encoding="utf-8", mode="r"
        ) as f:
            reader = csv.DictReader(f)
            for row in reader:
                food_list.append(Food(name=row["料理名"], price=row["値段"]))
        saved_foods = Food.objects.bulk_create(food_list)
        for saved_food in saved_foods:
            print(saved_food.id, saved_food.name, saved_food.price)
        cursor = connection.cursor()
        cursor.execute("truncate menu")

        return render(request, "index.html")
