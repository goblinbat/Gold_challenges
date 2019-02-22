"""
Broken worse than before
Giving up and working on challenge 5
"""

from . import badge_repo
import unittest
 

class ChallengeFourTests(unittest.TestCase):
    def setUp():
        badge_repo.BadgeRepo.create_badge(2, '6')
    
    def test_badge_repo_Badgerepo_create_badge_should_add_badge_to_list(self):
        # Arrange
        self.badgeid = 1
        self.dors = ['3']

        # Act
        badge_repo.BadgeRepo.create_badge(self.badgeid, self.dors)
        actual = len(badge_repo.badges)
        expected = 2

        # Assert
        self.assertEqual(actual, expected)

    def test_badge_repo_badgerepo_view_badges_should_return_list(self):
        # Arrange
        testlist = badge_repo.BadgeRepo.view_badges()

        # Act
        actual = len(testlist)
        expected = 1

        # Assert
        self.assertEqual(actual, expected)

    def test_badge_repo_badgerepo_add_door_should_add_item_to_badge_item_in_list(self):
        # Arrange
        self.bagid = 2
        self.new_door = '9'

        # Act + Assert
        self.assertTrue(badge_repo.BadgeRepo.add_door(self.bagid, self.new_door))

    def test_badge_repo_BadgeRepo_delete_door_should_remove_item_from_badge_item_in_list(self):
        pass
    
    def test_badge_repo_BadgeRepo_delete_badge_should_remove_badge_item_from_list(self):
        pass

    def tearDown():
        badge_repo.badges = []
