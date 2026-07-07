from django.test import TestCase
from django.urls import reverse

from .models import Recipie


class RecipeFlowTests(TestCase):
    def test_update_page_renders_existing_recipe_details(self):
        recipe = Recipie.objects.create(
            name="Pasta",
            description="Creamy pasta",
        )

        response = self.client.get(reverse('update_recipie', args=[recipe.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pasta")
        self.assertContains(response, "Creamy pasta")

    def test_delete_recipe_removes_it_and_redirects(self):
        recipe = Recipie.objects.create(
            name="Salad",
            description="Fresh salad",
        )

        response = self.client.post(reverse('delete_recipie', args=[recipe.id]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Recipie.objects.filter(id=recipe.id).exists())
