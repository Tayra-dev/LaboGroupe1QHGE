from abstract_dto import AbstractDTO


class RoleDTO(AbstractDTO):
    def __init__(self):
        self.role_id = None
        self.name = None

    @staticmethod
    def build_from_entity(entity):
        pass

    def get_json_parsable(self):
        pass
