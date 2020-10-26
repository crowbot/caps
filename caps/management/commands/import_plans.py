# -*- coding: future_fstrings -*-
from os.path import join
from datetime import date
import math

import pandas as pd

from caps.models import Council, PlanDocument

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

from django.conf import settings

class Command(BaseCommand):
    help = 'Imports data from data/plans into the database'

    def handle(self, *args, **options):

        df = pd.read_csv(settings.PROCESSED_CSV)
        for index, row in df.iterrows():
            council, created = Council.objects.get_or_create(
                name = row['council'],
                slug = PlanDocument.council_slug(row['council']),
                authority_code = PlanDocument.char_from_text(row['authority_code']),
                authority_type = PlanDocument.char_from_text(row['authority_type']),
                country = Council.country_code(row['country']),
                whatdotheyknow_id = PlanDocument.integer_from_text(row['wdtk_id']),
                mapit_area_code = PlanDocument.char_from_text(row['mapit_area_code']),
                website_url = PlanDocument.char_from_text(row['website_url']),
            )
            print(row)

            if not pd.isnull(row['url']):
                plan_filename = PlanDocument.plan_filename(row['council'], row['url'])
                document_file = open(join(settings.PLANS_DIR, plan_filename), "rb")
                file_object = File(document_file)
                (start_year, end_year) = PlanDocument.start_and_end_year_from_time_period(row['time_period'])
                plan_document = PlanDocument.objects.get_or_create(
                    url=row['url'],
                    url_hash=PlanDocument.make_url_hash(row['url']),
                    council = council,
                    defaults = {
                                'date_first_found': PlanDocument.date_from_text(row['date_retrieved']),
                                'date_last_found': date.today(),
                                'start_year': start_year,
                                'end_year': end_year,
                                'document_type': PlanDocument.document_type_code(row['type']),
                                'scope': PlanDocument.scope_code(row['scope']),
                                'status': PlanDocument.status_code(row['status']),
                                'well_presented': PlanDocument.boolean_from_text(row['well_presented']),
                                'baseline_analysis': PlanDocument.boolean_from_text(row['baseline_analysis']),
                                'notes': PlanDocument.char_from_text(row['notes']),
                                'file_type': PlanDocument.char_from_text(row['file_type']),
                                'charset': PlanDocument.char_from_text(row['charset']),
                                'text': PlanDocument.char_from_text(row['text']),
                                'file': file_object
                                }
                )


                print(file_object)
                # plan_document.file.save(plan_filename, file_object, save=True)
