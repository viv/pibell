import unittest
import button
import listener

def pressed():
  return True

button.pressed = pressed

class ListonerTest(unittest.TestCase):
    def testShouldNotifyWhenButtonPressed(self):
        self.assertTrue(listener.checkBell())