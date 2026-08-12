from app.dtos.team_dto import TeamDTO
from app.framework.mapper import AbstractMapper
from app.models.team import Team
from app.forms.teams.team_form import TeamForm


class TeamMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(team: Team) -> TeamDTO:
        return TeamDTO.build_from_entity(team)

    @staticmethod
    def form_to_entity(form, team: Team) -> Team:
        if isinstance(form, TeamForm):
            team.name = form.name.data
            team.description = form.name.description
        return team
