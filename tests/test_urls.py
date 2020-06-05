from django.test import SimpleTestCase
from django.urls import reverse, resolve
from project.views import index

class TestUrls(SimpleTestCase):
  
  def test_index_url_resolved(self):
    url = reverse('index', args = [])
    print(resolve(url))
    self.assertEquals(resolve(url).func, index)