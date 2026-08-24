from app import app, db
from app.dtos.site_dto import SiteDTO
from app.mappers.site_mapper import SiteMapper
from app.models.site import Site
from app.models.user import User
from app.models.equipment import Equipment
from app.forms.sites.site_form import SiteForm
from app.framework.service.abstract_service import AbstractService
from app.framework.decorators.injectable import injectable

@injectable
class SiteService(AbstractService):

    def find_all(self) -> list[SiteDTO]:
        return [SiteMapper.entity_to_dto(site) 
                for site in Site.query.filter_by(active=True).order_by(Site.site_id).all()]

    def find_one(self, entity_id: int) -> SiteDTO | None:
        site = self.find_one_entity(entity_id)

        return SiteMapper.entity_to_dto(site) if site else None

    def find_one_entity(self, entity_id: int) -> Site | None:
        return Site.query.filter_by(site_id=entity_id).first()

    def find_one_by(self, **kwargs) -> SiteDTO | None:
        site = Site.query.filter_by(**kwargs).first()

        return SiteMapper.entity_to_dto(site) if site else None

    def insert(self, form: SiteForm) -> SiteDTO | None:
        site = Site()
        SiteMapper.form_to_entity(form, site)

        try:
            db.session.add(site)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert site: {e}")
            db.session.rollback()
            return None

        return SiteMapper.entity_to_dto(site)

    def update(self, entity_id: int, form: SiteForm) -> SiteDTO | None:
        site = self.find_one_entity(entity_id)

        if site is None:
            return None

        SiteMapper.form_to_entity(form, site)

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"Update site {entity_id}: {e}")
            db.session.rollback()
            return None

        return SiteMapper.entity_to_dto(site)

    def delete(self, entity_id: int) -> int | None:
        site = self.find_one_entity(entity_id)

        if site is None:
            return None

        try:
            db.session.delete(site)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"Delete site {entity_id}: {e}")
            db.session.rollback()
            return None

        return entity_id

    def assign_user(self, user: User, site_id: int):
        site = self.find_one_entity(site_id)

        if user is None or site is None:
            return None

        if any(site_user.user_id == user.user_id for site_user in site.users):
            return None

        try:
            site.add_user(user)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"Assign {user.name} to {site.name}: {e}")
            db.session.rollback()
            return None

        return site_id

    def remove_user(self, user: User, site_id: int):
        site = self.find_one_entity(site_id)

        if user is None or site is None:
            return None

        if not any(site_user.user_id == user.user_id for site_user in site.users):
            return None

        try:
            site.remove_user(user)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"Remove {user.name} from {site.name}: {e}")
            db.session.rollback()
            return None

        return site_id

    def assign_equipment(self, equipment: Equipment, site_id: int):
        site = self.find_one_entity(site_id)

        if equipment is None or site is None:
            return None

        if any(site_equipment.equipment_id == equipment.equipment_id for site_equipment in site.equipments):
            return None

        try:
            site.add_equipment(equipment)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"Assign {equipment.name} to {site.name}: {e}")
            db.session.rollback()
            return None

        return site_id