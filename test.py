import os
from unittest import TestCase
from application import AssetManager
from domain import Asset

class Test(TestCase):
    def test_application(self):
        os.environ["PERSISTENCE_MODULE"] = "eventsourcing.sqlite"
        os.environ["SQLITE_DBNAME"] = "EnterpriseGIS_assets.sqlite"
        app = AssetManager()

        kiln_id = app.register_asset(name="Kiln")
        kiln_details = app.get_asset(kiln_id)
        self.assertEqual(kiln_details["name"], "Kiln")
        self.assertEqual(kiln_details["stoppage_causes"], [])

        app.add_stoppage_cause(kiln_id, "Mechanical Failure")
        kiln_details = app.get_asset(kiln_id)
        self.assertEqual(kiln_details["stoppage_causes"], ["Mechanical Failure"])

        clinker_id = app.register_asset(name="Clinker")
        clinker_details = app.get_asset(clinker_id)
        self.assertEqual(clinker_details["name"], "Clinker")
        self.assertEqual(clinker_details["stoppage_causes"], [])

        app.add_stoppage_cause(clinker_id, "Electrical Failure")
        clinker_details = app.get_asset(clinker_id)
        self.assertEqual(clinker_details["stoppage_causes"], ["Electrical Failure"])

        # Simulate restart
        del app

        app = AssetManager()

        # Verify persistence
        kiln_details = app.get_asset(kiln_id)
        self.assertEqual(kiln_details["name"], "Kiln")
        self.assertEqual(kiln_details["stoppage_causes"], ["Mechanical Failure"])

        clinker_details = app.get_asset(clinker_id)
        self.assertEqual(clinker_details["name"], "Clinker")
        self.assertEqual(clinker_details["stoppage_causes"], ["Electrical Failure"])
