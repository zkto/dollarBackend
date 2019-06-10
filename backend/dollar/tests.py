from django.test import TestCase
from dollar.models import DollarClp
from django.utils import timezone



# models test
class DollarTest(TestCase):

    def create_dollar(self, title="only a test", body="yes, this is only a test"):
        return DollarClp.objects.create(title=title, body=body, created_at=timezone.now())

    def test_whatever_creation(self):
        w = self.create_dollar()
        self.assertTrue(isinstance(w, DollarClp))
        self.assertEqual(w.__unicode__(), w.title)


