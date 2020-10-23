from django.test import TestCase

from caps.models import PlanDocument

class PlanDocumentStartEndEndYearsFromTimePeriodTestCase(TestCase):

    def test_simple_case(self):
        expected = ('2020', '2030')
        actual = PlanDocument.start_and_end_year_from_time_period('2020-2030')
        self.assertEqual(expected, actual)

    def test_no_dates_set_to_none(self):
        expected = (None, None)
        actual = PlanDocument.start_and_end_year_from_time_period('Not yet published')
        self.assertEqual(expected, actual)

    def test_dates_then_text_parsed(self):
        expected = ('2020', '2030')
        actual = PlanDocument.start_and_end_year_from_time_period('2020-2030: "aim to become carbon neutral by 2030, and 80% by 2025."')
        self.assertEqual(expected, actual)


class PlanDocumentDocumentTypeCodeTestCase(TestCase):

    def test_simple_case(self):
        expected = PlanDocument.ACTION_PLAN
        actual = PlanDocument.document_type_code('Action plan')
        self.assertEqual(expected, actual)

    def test_capitalisation_normalised(self):
        expected = PlanDocument.CLIMATE_STRATEGY
        actual = PlanDocument.document_type_code('Climate STraTegy')
        self.assertEqual(expected, actual)

    def test_invalid_entry(self):
        expected = None
        actual = PlanDocument.document_type_code('Something else')
        self.assertEqual(expected, actual)

    def test_whitespace_removed(self):
        expected = PlanDocument.ACTION_PLAN
        actual = PlanDocument.document_type_code('Action plan ')
        self.assertEqual(expected, actual)


class PlanDocumentScopeCodeTestCase(TestCase):

    def test_simple_case(self):
        expected = PlanDocument.COUNCIL_ONLY
        actual = PlanDocument.scope_code('Council only')
        self.assertEqual(expected, actual)

    def test_capitalisation_normalised(self):
        expected = PlanDocument.WHOLE_AREA
        actual = PlanDocument.scope_code('WhOle AreA')
        self.assertEqual(expected, actual)

    def test_invalid_entry(self):
        expected = None
        actual = PlanDocument.scope_code('Something else')
        self.assertEqual(expected, actual)

    def test_whitespace_removed(self):
        expected = PlanDocument.ACTION_PLAN
        actual = PlanDocument.scope_code('Council only ')
        self.assertEqual(expected, actual)

class PlanDocumentStatusCodeTestCase(TestCase):

    def test_simple_case(self):
        expected = PlanDocument.DRAFT
        actual = PlanDocument.status_code('Draft')
        self.assertEqual(expected, actual)

    def test_capitalisation_normalised(self):
        expected = PlanDocument.APPROVED
        actual = PlanDocument.status_code('aPProVed')
        self.assertEqual(expected, actual)

    def test_invalid_entry(self):
        expected = None
        actual = PlanDocument.status_code('Something else')
        self.assertEqual(expected, actual)

    def test_whitespace_removed(self):
        expected = PlanDocument.APPROVED
        actual = PlanDocument.status_code(' Approved')
        self.assertEqual(expected, actual)

class BooleanFromTextTestCase(TestCase):

    def test_simple_case(self):
        expected = False
        actual = PlanDocument.boolean_from_text('N')
        self.assertEqual(expected, actual)

    def test_capitalisation(self):
        expected = True
        actual = PlanDocument.boolean_from_text('y')
        self.assertEqual(expected, actual)

    def test_yes_no(self):
        expected = True
        actual = PlanDocument.boolean_from_text('yes')
        self.assertEqual(expected, actual)

    def test_invalid_entry(self):
        expected = None
        actual = PlanDocument.boolean_from_text('yawp')
        self.assertEqual(expected, actual)
