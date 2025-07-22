from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Vehicle
from .tasks import complete_vehicle_data


@receiver(post_save, sender=Vehicle)
def complete_vehicle_data_post_save(sender, instance, created, **kwargs):
    if created and not instance.brand or not instance.model or not instance.color:
        complete_vehicle_data.delay(instance.license_plate)
