from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from .models import About
from .forms import CollaborateForm


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content and class"""
        self.about = About(
            title='About Me',
            content='Read about me and my experience.',
            updated_on=datetime.now()
        )
        self.about.save()

    def test_render_about_me_page_with_form(self):
        """
        Verifies get request for about me view, containing
        a collaboration form
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me",
                      response.content,
                      msg="Title not found in response content")
        self.assertIn(b"Read about me and my experience.",
                      response.content,
                      msg="Content not found in response content")
        self.assertIsInstance(response.context['about'],
                              About,
                              msg="About context parameter not an About class"
                              "instance")
        self.assertIsInstance(response.context['collaborate_form'],
                              CollaborateForm,
                              msg="collaborate_form parameter not a "
                              "CollaborateForm class instance")

    def test_successful_collab_request(self):
        """Test for posting a collaboration request"""
        post_data = {
            'name': 'John Stones',
            'email': 'john.stones@email.com',
            'message': 'Hello! Lets meet up!'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within'
            b' 2 working days.',
            response.content
        )
