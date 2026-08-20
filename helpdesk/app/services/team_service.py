from app import app, db
from sqlalchemy.exc import SQLAlchemyError
from app.framework.decorators.injectable import injectable
from app.framework.injector import Scope
from app.framework.service.abstract_service import AbstractService
from app.models.team import Team
from app.dtos.team_dto import TeamDTO
from app.mappers.team_mapper import TeamMapper
from app.forms.teams.team_form import TeamCreationForm


@injectable(scope=Scope.SCOPED)
class TeamService(AbstractService):
    def find_all(self) -> list[TeamDTO]:
        try:
            teams = Team.query.filter_by(active=True).order_by(Team.team_id).all()
        except SQLAlchemyError as e:
            db.session.rollback()
            app.logger.error(f"Erreur lors de la sélection de toutes les équipes: {e}")
            return []
        else:
            return [TeamMapper.entity_to_dto(team) for team in teams]

    def find_one(self, team_id: int) -> TeamDTO:
        pass

    def find_one_by(self, **kwargs) -> TeamDTO:
        pass

    def insert(self, form: TeamCreationForm) -> TeamDTO | None:
        try:
            team = Team()
            TeamMapper.form_to_entity(form, team)
            
        except SQLAlchemyError as e:
            db.session.rollback()
            app.logger.error(f"Erreur lors de la création de l'équipe: {e}")

    def update(self, team_id: int, data) -> TeamDTO | None:
        pass

    def delete(self, team_id: int) -> int | None:
        pass
