import unittest
import button
import sound


def mockPlay():
  return True

sound.play = mockPlay

class ButtonTest(unittest.TestCase):
    def testShouldPlaySoundWhenPressed(self):
        self.assertTrue(button.pressed())