from app.framework.mapper import AbstractMapper
from app.models.site import Site
from app.dtos.site_dto import SiteDTO
from app.forms.sites.site_form import SiteForm

class SiteMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(entity: Site) -> SiteDTO:
        return SiteDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, entity: Site) -> Site:
        if isinstance(form, SiteForm):
            entity.name = form.name.data
            entity.address = form.address.data
            entity.city = form.city.data

        return entity