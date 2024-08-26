from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'John Stones',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_empty_name(self):
        """ Test for empty 'name' field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(),
                         msg="Form is valid despite 'name' field being empty")

    def test_form_invalid_email(self):
        """ Test for missing '@' in email field"""
        form = CollaborateForm({
            'name': 'John Stevens',
            'email': 'test.test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(),
                         msg="Form is valid despite 'email' field missing '@'")

    def test_form_emtpy_message(self):
        """ Test for empty 'message' field"""
        form = CollaborateForm({
            'name': 'Maria Davidson',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(),
                         msg="Form is valid despite 'message' being empty")
