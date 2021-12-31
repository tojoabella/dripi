from services.base_application_service import BaseApplicationService
from services.modes_microservice.database_service import DatabaseService
from services.modes_microservice.lib.location_identifiers import locationIdentifiers
import services.modes_microservice.lib.road_lengths as road_lengths

class ApplicationService(BaseApplicationService, DatabaseService):
    
    def __init__(self):
        #DatabaseService.__init__(self, database_url=database_url)
        pass
    
    @staticmethod
    def get_localities(lat, lon):
        res = locationIdentifiers.get_all_localities(lat, lon)
        res = {'localities': res}
        return res
    
    @staticmethod
    def get_neighborhood(lat, lon):
        res = locationIdentifiers.get_neighborhood(lat, lon)
        res = {'neighborhood': res}
        return res
    
    @staticmethod
    def get_road(lat, lon):
        res = locationIdentifiers.get_neighborhood(lat, lon)
        res = {'neighborhood': res}
        return res
    
    @staticmethod
    def get_roads(lat, lon, format):
        if format:
            if format == 'detailed':
                res = locationIdentifiers.get_all_roads(lat, lon, format)
            elif format == 'None':
                res = locationIdentifiers.get_all_roads(lat, lon)
            else:
                res = "format should be None or 'detailed'"
        else:
            res = locationIdentifiers.get_all_roads(lat, lon)
        res = {'roads': res}
        return res
    
    @staticmethod
    def get_road(lat, lon):
        res = locationIdentifiers.get_road(lat, lon)
        return res
    