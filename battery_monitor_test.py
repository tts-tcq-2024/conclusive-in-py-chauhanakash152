import unittest
from battery_monitor import BatteryMonitor

class TestInferBreach(unittest.TestCase):
    
    def setUp(self):
        # Initialize the BatteryMonitor with a cooling type
        self.battery_char_passive = {'coolingType': 'PASSIVE_COOLING'}
        self.monitor_passive = BatteryMonitor(self.battery_char_passive)

        self.battery_char_hi_active = {'coolingType': 'HI_ACTIVE_COOLING'}
        self.monitor_hi_active = BatteryMonitor(self.battery_char_hi_active)

        self.battery_char_med_active = {'coolingType': 'MED_ACTIVE_COOLING'}
        self.monitor_med_active = BatteryMonitor(self.battery_char_med_active)

    def test_too_low_passive(self):
        """Test if temperature below lower limit is classified as TOO_LOW for passive cooling."""
        self.assertEqual(self.monitor_passive.infer_breach(-1), 'TOO_LOW')

    def test_normal_passive(self):
        """Test if temperature within limits is classified as NORMAL for passive cooling."""
        self.assertEqual(self.monitor_passive.infer_breach(20), 'NORMAL')

    def test_too_high_passive(self):
        """Test if temperature above upper limit is classified as TOO_HIGH for passive cooling."""
        self.assertEqual(self.monitor_passive.infer_breach(36), 'TOO_HIGH')

    def test_too_low_hi_active(self):
        """Test if temperature below lower limit is classified as TOO_LOW for high active cooling."""
        self.assertEqual(self.monitor_hi_active.infer_breach(-1), 'TOO_LOW')

    def test_normal_hi_active(self):
        """Test if temperature within limits is classified as NORMAL for high active cooling."""
        self.assertEqual(self.monitor_hi_active.infer_breach(30), 'NORMAL')

    def test_too_high_hi_active(self):
        """Test if temperature above upper limit is classified as TOO_HIGH for high active cooling."""
        self.assertEqual(self.monitor_hi_active.infer_breach(46), 'TOO_HIGH')

    def test_too_low_med_active(self):
        """Test if temperature below lower limit is classified as TOO_LOW for medium active cooling."""
        self.assertEqual(self.monitor_med_active.infer_breach(-1), 'TOO_LOW')

    def test_normal_med_active(self):
        """Test if temperature within limits is classified as NORMAL for medium active cooling."""
        self.assertEqual(self.monitor_med_active.infer_breach(30), 'NORMAL')

    def test_too_high_med_active(self):
        """Test if temperature above upper limit is classified as TOO_HIGH for medium active cooling."""
        self.assertEqual(self.monitor_med_active.infer_breach(41), 'TOO_HIGH')

if __name__ == '__main__':
    unittest.main()
