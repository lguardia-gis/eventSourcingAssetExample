from eventsourcing.application import Application
from domain import Asset

class AssetManager(Application):
    def register_asset(self, name):
        asset = Asset(name=name)
        self.save(asset)
        return asset.id

    def get_asset(self, asset_id):
        asset = self.repository.get(asset_id)
        return {"name": asset.name, "stoppage_causes": list(asset.stoppage_causes)}

    def add_stoppage_cause(self, asset_id, cause):
        asset = self.repository.get(asset_id)
        asset.add_stoppage_cause(cause)
        self.save(asset)
