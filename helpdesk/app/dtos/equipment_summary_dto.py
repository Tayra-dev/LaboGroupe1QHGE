from app.framework.dto import AbstractDTO
from app.models.equipment import Equipment


class EquipmentSummaryDTO(AbstractDTO):

    def __init__(self) -> None:
        self.equipment_id = None
        self.name = None
        self.type = None
        self.serial = None
        self.purchase_date = None

    @staticmethod
    def build_from_entity(entity: Equipment) -> "EquipmentSummaryDTO": # type: ignore
        equipment_dto = EquipmentSummaryDTO()

        equipment_dto.equipment_id = entity.equipment_id
        equipment_dto.name = entity.name
        equipment_dto.type = entity.type
        equipment_dto.serial = entity.serial
        equipment_dto.purchase_date = entity.purchase_date

        return equipment_dto

    def get_json_parsable(self): # type: ignore
        data = dict(self.__dict__)
        return data
