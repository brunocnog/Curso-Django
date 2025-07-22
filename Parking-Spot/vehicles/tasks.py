from celery import shared_task
from playwright.sync_api import sync_playwright

from .models import Vehicle


@shared_task
def complete_vehicle_data(license_plate):
    url = 'https://favorite-pig.static.domains/carros/'

    brand = None
    model = None
    color = None

    with sync_playwright as p:
        browser = p.chromium.lunch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('table')
        xpath_expression = f"//table//tr[td[1][normalize-space()='{license_plate}']]"
        row = page.query_selector(xpath_expression)
        if row:
            cells = row.query_selector('td')
            brand = cells[1].inner_text().strip()
            model = cells[2].inner_text().strip()
            color = cells[3].inner_text().strip()
        browser.close()

    if brand and model and color:
        Vehicle.objects.filter(
            license_plate=license_plate,).update(
                brand=brand,
                model=model,
                color=color,
        )
