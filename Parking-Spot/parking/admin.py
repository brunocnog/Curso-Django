from django.contrib import admin
from parking.models import ParkingRecord, ParkingSpot
from vehicles.models import Vehicle


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_occupied']
    search_fields = ['spot_number']
    list_filter = ['is_occupied']


@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'parking_spot', 'entry_time', 'exit_time']
    search_fields = ['vehicle__license_plate', 'parking_spot__spot_number']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        is_editing = request.resolver_match.url_name.endswith('change')

        if db_field.name == "parking_spot" and not is_editing:
            # Só mostra vagas que não estão ocupadas
            kwargs["queryset"] = ParkingSpot.objects.filter(is_occupied=False)

        elif db_field.name == 'vehicle' and not is_editing:
            # Pega IDs dos veículos que já estão estacionados (sem horário de saída)
            vehicle_is_parked = ParkingRecord.objects.filter(
                exit_time__isnull=True).values_list('vehicle_id', flat=True)
            # Mostra apenas veículos que não estão atualmente estacionados
            kwargs["queryset"] = Vehicle.objects.exclude(
                id__in=vehicle_is_parked)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
