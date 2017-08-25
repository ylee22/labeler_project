import os
import datetime

from django.test import TestCase
from django.utils import timezone

import class_project_1.settings
from .models import Image

import doctestexample

import doctest

MEDIA_ROOT = class_project_1.settings.MEDIA_ROOT


class ImageModelTest(TestCase):
    fixtures = ['labeler_test_data.json']
    caption = "This is only a test"

    def create_image(self, caption=caption):
        return Image.objects.create(file=os.path.join(MEDIA_ROOT, 'images', 'test_image.jpg'),
                                    caption=caption)
                                    # taken_date=timezone.now() - datetime.timedelta(365.25 * 2.5),
                                    # file=open(os.path.join(MEDIA_ROOT, 'images', 'test_image.jpg'), 'rb'),
                                    # uploaded_at=timezone.now()

    def test_image_creation(self):
        image = self.create_image()
        self.assertTrue(isinstance(image, Image))
        # self.assertEqual(image.__unicode__(), image.caption)
        self.assertEqual(self.caption, image.caption)


class DocTest(TestCase):
    def test_doctests(self):
        results = doctest.testmod(doctestexample)
        self.assertEqual(results.failed, 0)