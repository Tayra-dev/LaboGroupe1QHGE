from app.framework.dto import AbstractDTO
from app.models.site import Site


class SiteSummaryDTO(AbstractDTO):

    def __init__(self):
        self.site_id = None
        self.name = None
        self.address = None
        self.city = None
        self.users = []
        self.equipments = []

    @staticmethod
    def build_from_entity(entity: Site) -> "SiteSummaryDTO":
        site_dto = SiteSummaryDTO()
        site_dto.site_id = entity.site_id
        site_dto.name = entity.name
        site_dto.address = entity.address
        site_dto.city = entity.city

        return site_dto

    def get_json_parsable(self):
        data = dict(self.__dict__)
        return data