import unittest

from room import Room, Office, LivingSpace


class TestRoom(unittest.TestCase):
    """Unit tests for the Room class"""

    def setUp(self):
        self.room = Room()

        self.room.create_room({
            "<room_name>": ["LivingSpace1"],
            "Living": True,
            "Office": False
        })
        """Create sample living space"""
        self.room.create_room({
            "<room_name>": ["Office1"],
            "Living": False,
            "Office": True
        })
        self.office1 = self.room.offices[0]

    def test_office_subclass_of_room(self):
        """Tests if class Office is a subclass of class Room"""
        self.assertTrue((issubclass(Office, Room)),
                        msg='Class Office should be a subclass of Room')

    def test_livingspace_subclass_of_room(self):
        """Tests if class LivingSpace is a subclass of Room"""
        self.assertTrue((issubclass(LivingSpace, Room)),
                        msg='Class LivingSpace should be a subclass of Room')

    def test_create_room(self):
        """Test creation of rooms"""
        # Check rooms created added to relevant lists
        self.assertEqual(2, len(self.room.rooms))
        self.assertEqual(1, len(self.room.livingspaces))
        self.assertEqual(1, len(self.room.offices))

        """Validates that duplicate rooms are not added"""
        self.room.create_room({
            "<room_name>": ["Office1"],
            "Living": False,
            "Office": True
        })
        # Duplicate rooms not added to any list
        self.assertEqual(2, len(self.room.rooms))
        self.assertEqual(1, len(self.room.offices))

    def test_office_has_capacity_of_6(self):
        """Ensure office has a capacity of 6"""
        self.office = Office()
        self.assertEqual(6, self.office.max_occupancy)
        pass

    def test_livingspace_has_capacity_of_4(self):
        self.livingspace = LivingSpace()
        self.assertEqual(4, self.livingspace.max_occupancy)
        """Ensure livingspace has a capacity of 4"""
        pass

    def test_print_room():
        """Tests for the print_room function"""
        pass


if __name__ == '__main__':
    unittest.main()
