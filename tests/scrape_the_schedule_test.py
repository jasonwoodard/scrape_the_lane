import unittest

import team_schedule_scraper as tss

'''
Using this unit test framework

https://docs.python.org/3/library/unittest.html
'''


class TestTeamScheduleScraper(unittest.TestCase):

    # This is called before EVERY test below. So each time the test is using a fresh object that has no 'bleed' from
    # previous test runs.  This is key for classes that can maintain state within the instance, in this case that would
    # be the HTML document which we're not testing here. Regardless, we rule that possibility out.
    def setUp(self):
        self.TEAM_ID = 42

        # We create an instance of the object being tested.  Since TeamScheduleScraper immediately calls into
        # kitchen.get_soup in __init__ we HAVE to pass an Html document. Lucky for us <html> is the smallest
        # valid HTML document there is.
        #
        # Next level: The way to make the class more testable is to:
        #  Make a 'get_soup' function on TestScheduleScraper that is called before work that requires the soup, i.e.
        #  make the constructor not take action based on dependencies. Since in this case we just want to test a
        #  helper method, we don't really need to get a beautiful soup object.  This kind of testable thought
        #  becomes more important as you invest in testing, but it helps with keeping your programs 'loosely coupled'.
        self.scraper_being_tested = tss.TeamScheduleScraper('<html>', self.TEAM_ID)

    def test_win_loss_parse(self):
        tested = self.scraper_being_tested

        # Tuple, first value input, second value correct output
        no_paren = '0 - 1', (0, 1, None, None)
        with_paren = '1 - 0 (2 - 0)', (1, 0, 2, 0)

        # Test run with no parenthesis
        result1 = tested._get_win_loss_record(no_paren[0])
        self.assertEqual(no_paren[1], result1)

        # Test run with parenthesis
        result2 = tested._get_win_loss_record(with_paren[0])
        self.assertEqual(with_paren[1], result2)

    # This is here to show you a VERY basic test.  The base class has 'assertions' that provide rich error messages
    # when they fail, e.g. "In test test_one_plus_one expected 2, but actual was 3".  This lets you pinpoint the problem
    # very quickly.
    def test_one_plus_one(self):
        self.assertEquals(1 + 1, 2, 'One plus one DO NOT equal 2?')
        self.assertNotEquals(1 + 2, 2, 'This error only shows if the test fails.')


if __name__ == '__main__':
    unittest.main()
