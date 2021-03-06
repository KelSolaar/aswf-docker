# Copyright (c) Contributors to the aswf-docker Project. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Tests for user settings
"""

import unittest
import tempfile
import os
import logging

from aswfdocker import constants, index


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.index = index.Index()

    def test_iter_images(self):
        packages = list(self.index.iter_images(constants.ImageType.PACKAGE))
        self.assertGreater(len(packages), 15)
        self.assertEqual(packages[0], "clang")

    def test_get_versions(self):
        images = list(self.index.iter_images(constants.ImageType.IMAGE))
        self.assertGreater(len(images), 1)
        self.assertEqual(images[0], "common")
        versions = list(self.index.iter_versions(constants.ImageType.IMAGE, images[0]))
        self.assertGreaterEqual(len(versions), 1)
        self.assertTrue(versions[0].startswith("1."))
