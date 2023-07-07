class Car(Serviceable):
    def __init__(self, Engine, Battery):
        engine = Engine
        battery = Battery
        
    @abstractmethod
    def needs_service():
        return engine.needs_service() and battery.needs_service()
