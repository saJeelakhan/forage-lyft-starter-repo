class Car(Serviceable):
    def __init__(self, Engine, Battery, tires):
        engine = Engine
        battery = Battery
        self.tires = tires
        
    @abstractmethod
    def needs_service(self):
        return engine.needs_service() or battery.needs_service() or self.tires.needs_service()
