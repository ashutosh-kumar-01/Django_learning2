from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class URLTest(TestCase):
    def test_sampletest(self):
        response = self.client.get('/sampletest/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is a sample test page")
        
    def test_sampletest_content(self):
        response = self.client.get('/sampletest/')
        # self.assertContains(response, "<h1 style='color:blue'>This is a sample test page</h1>")
        self.assertNotContains(response, "<h1 style='color:blue'>This is a sample test page</h1>") 
        
    def test_sampletest_negativeurl(self):
            response = self.client.get('/sampletest/')
            # self.assertContains(response, "<h1 style='color:blue'>This is a sample test page</h1>")
            self.assertEqual(response.status_code, 200)
    
    def test_sampletest_urlname(self):
        url = reverse('st')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_sampletest1_parameter(self):
        url = reverse('st1', args = [24])
        response = self.client.get(url)
        self.assertContains(response, 24)
        
    def test_old_redirect(self):
        response = self.client.get('/old/')
        self.assertRedirects(response=response, expected_url='/new/', status_code=301, target_status_code=200)    
            
                