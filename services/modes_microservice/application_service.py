from services.base_application_service import BaseApplicationService
from services.modes_microservice.database_service import DatabaseService
from services.modes_microservice.lib.location_identifiers import locationIdentifiers
import services.modes_microservice.lib.road_lengths as road_lengths

class ApplicationService(BaseApplicationService, DatabaseService):
    
    def __init__(self):
        DatabaseService.__init__(self, database_url=database_url)
    
    