from services.base_application_service import BaseApplicationService
from services.modes_microservice.database_service import DatabaseService
from lib import road_identity, road_lengths

class UserResource(BaseApplicationService):

    def __init__(self):
        db = DatabaseService()
    