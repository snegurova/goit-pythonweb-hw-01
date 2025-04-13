"""Module providing a Vehicle factory."""
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    """Class representing a Vehicle"""
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        """Method starting engine."""


class Car(Vehicle):
    """Class representing a Car Vehicle"""
    def start_engine(self) -> None:
        logger.info("%s %s: Engine is started", self.make, self.model)


class Motorcycle(Vehicle):
    """Class representing a Motorcycle Vehicle"""
    def start_engine(self) -> None:
        logger.info("%s %s: Motor is started", self.make, self.model)


class VehicleFactory(ABC):
    """Class representing a VehicleFactory"""
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        """Method creating car."""

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        """Method creating motorcycle."""


class USVehicleFactory(VehicleFactory):
    """Class representing a US VehicleFactory"""
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(f"{make} {model}", "(US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(f"{make} {model}", "(US Spec)")


class EUVehicleFactory(VehicleFactory):
    """Class representing a EU VehicleFactory"""
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(f"{make} {model}", "(EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(f"{make} {model}", "(EU Spec)")


def main() -> None:
    """Example usage function."""
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle2 = eu_factory.create_motorcycle("Yamaha", "MT-07")

    vehicle1.start_engine()
    vehicle2.start_engine()


if __name__ == "__main__":
    main()
