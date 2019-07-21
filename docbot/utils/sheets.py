import os
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

'''Get Sheet by ID'''
gcloud_sheet_animals = os.environ['GCLOUD_SHEET_ANIMALS']


def microchip_lookup(animal_name):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        './docbot/utils/gauth.json', scope)
    gc = gspread.authorize(credentials)
    animal_sheet = gc.open_by_key(gcloud_sheet_animals)
    worksheets = animal_sheet.worksheets()

    try:
        # Look up animal in list of worksheets
        animal_microchip = 'No microchip found for animal ' + animal_name
        for sheet in worksheets:
            # Cats
            if sheet.title == "Cats":
                criteria_re = re.compile(".*({}).*".format(animal_name), flags=re.IGNORECASE)
                cell = sheet.find(criteria_re)
                if cell != None:
                    cell_row_number = cell.row
                    animal_microchip_val = sheet.cell(cell_row_number, 6).value
                    if animal_microchip_val != "":
                        animal_microchip = animal_microchip_val
                    return animal_microchip
            # Dogs
            if sheet.title == "Dogs":
                criteria_re = re.compile(".*({}).*".format(animal_name), flags=re.IGNORECASE)
                cell = sheet.find(criteria_re)
                if cell != None:
                    cell_row_number = cell.row
                    animal_microchip_val = sheet.cell(cell_row_number, 7).value
                    if animal_microchip_val != "":
                        animal_microchip = animal_microchip_val
                        return animal_microchip
    except:
        print("Error looking for " + animal_name)
    finally:
        return animal_microchip
