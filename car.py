class Car(Serviceable):
    def __init__(self, Engine, Battery):
        engine = Engine
        battery = Battery
        
    @abstractmethod
    def needs_service(self):
        return engine.needs_service() or battery.needs_service()
