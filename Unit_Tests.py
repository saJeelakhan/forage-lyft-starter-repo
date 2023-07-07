import unittest
from datetime import datetime

from Battery.NubbinBattery import NubbinBattery
from Battery.SpindlerBattery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestBattery(unittest.TestCase):
    
    def test_nubbin_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(nubbin_battery.needs_service())
        
    def test_nubbin_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(nubbin_battery.needs_service())
    
    def test_spindler_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(spindler_battery.needs_service())
        
    def test_spindler_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(spindler_battery.needs_service())
        
class TestEngine(unittest.TestCase):
    
    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 40000
        last_service_mileage = 500
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet_engine.needs_service())
        
    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 40000
        last_service_mileage = 20000
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet_engine.needs_service())
        
    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 500
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.needs_service())
        
    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 50000
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby_engine.needs_service())
        
    def test_sternman_engine_should_be_serviced(self):
        warning_light_is_on = True
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman_engine.needs_service())
        
    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman_engine.needs_service())
    
class TestModel(unittest.TestCase):
    
    def test_calliope_should_be_serviced(self):
        self.assertTrue(TestBattery.test_spindler_battery_should_be_serviced() or TestEngine.test_capulet_engine_should_be_serviced())
    def test_calliope_should_not_be_serviced(self):
        self.assertFalse(TestBattery.test_spindler_battery_should_not_be_serviced() and TestEngine.test_capulet_engine_should_not_be_serviced())
            
    def test_glissade_should_be_serviced(self):
        self.assertTrue(TestBattery.test_spindler_battery_should_be_serviced() or TestEngine.test_willoughby_engine_should_be_serviced())
    def test_glissade_should_not_be_serviced(self):
        self.assertFalse(TestBattery.test_spindler_battery_should_not_be_serviced() and TestEngine.test_willoughby_engine_should_not_be_serviced())
           
    def test_palindrome_should_be_serviced(self):
        self.assertTrue(TestBattery.test_spindler_battery_should_be_serviced() or TestEngine.test_sternman_engine_should_be_serviced())
    def test_palindrome_should_not_be_serviced(self):
        self.assertFalse(TestBattery.test_spindler_battery_should_not_be_serviced() and TestEngine.test_sternman_engine_should_not_be_serviced())
         
    def test_rorschach_should_be_serviced(self):
        self.assertTrue(TestBattery.test_nubbin_battery_should_be_serviced() or TestEngine.test_willoughby_engine_should_be_serviced())
    def test_rorschach_should_not_be_serviced(self):
        self.assertFalse(TestBattery.test_nubbin_battery_should_not_be_serviced() and TestEngine.test_willoughby_engine_should_not_be_serviced())

    def test_thovex_should_be_serviced(self):
        self.assertTrue(TestBattery.test_nubbin_battery_should_be_serviced() or TestEngine.test_capulet_engine_should_be_serviced())
    def test_thovex_should_not_be_serviced(self):
        self.assertFalse(TestBattery.test_nubbin_battery_should_not_be_serviced() and TestEngine.test_capulet_engine_should_not_be_serviced())
    
        
if __name__ == '__main__':
    unittest.main()

