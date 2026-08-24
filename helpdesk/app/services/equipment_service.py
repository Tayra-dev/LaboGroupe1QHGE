from app.framework.service.abstract_service import AbstractService
from app.framework.decorators.injectable import injectable
from app.dtos.equipment_dto import EquipmentDTO
from app.mappers.equipment_mapper import EquipmentMapper
from app.models.equipment import Equipment
from app import db, app

@injectable
class EquipmentService(AbstractService):

    def find_all(self) -> list[EquipmentDTO]:
        return [EquipmentMapper.entity_to_dto(equipement) 
                for equipement in Equipment.query.filter_by(active=True).order_by(Equipment.equipment_id).all()]

    def find_one(self, entity_id: int) -> EquipmentDTO | None:
        equipment = self.find_one_entity(entity_id)

        return EquipmentMapper.entity_to_dto(equipment) if equipment else None

    def find_one_entity(self, entity_id: int) -> Equipment | None:
        return Equipment.query.filter_by(equipment_id=entity_id).first()

    def find_one_by(self, **kwargs) -> EquipmentDTO | None:
        equipment = Equipment.query.filter_by(**kwargs).first()

        return EquipmentMapper.entity_to_dto(equipment) if equipment else None

    def insert(self, form):
        return super().insert(form)

    def update(self, entity_id: int, form):
        return super().update(entity_id, form)

    def delete(self, entity_id: int):
        site = self.find_one_entity(entity_id)
        
        if site is None:
            return None

        try:
            db.session.delete(site)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"Delete equipment {entity_id}: {e}")
            db.session.rollback()
            return None

        return entity_id