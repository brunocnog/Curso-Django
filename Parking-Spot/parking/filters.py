from dj_rql.filter_cls import AutoRQLFilterClass

from parking.models import ParkingRecord, ParkingSpot


class ParkingSpotFiltersClass(AutoRQLFilterClass):
    MODEL = ParkingSpot
    

class ParkingRecordFiltersClass(AutoRQLFilterClass):
    MODEL = ParkingRecord
    FILTERS = (
        {
            'filter': 'license_plate',
            'source': 'vehicle__license_plate',
        },
    )