from dj_rql.filter_cls import AutoRQLFilterClass

from vehicles.models import VehicleType, Vehicle


class VehicleTypeFiltersClass(AutoRQLFilterClass):
    MODEL = VehicleType


class VehicleFiltersClass(AutoRQLFilterClass):
    MODEL = Vehicle
