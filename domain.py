from eventsourcing.domain import Aggregate, event

class Asset(Aggregate):
    @event("Equipment")
    def __init__(self, name):
        self.name = name
        self.stoppage_causes = []

    @event("StoppageCause")
    def add_stoppage_cause(self, cause):
        self.stoppage_causes.append(cause)
