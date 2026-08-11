from app import PRIORITIES, app, db
from app.framework.seed import Seedable
from app.models.priority import Priority


class PrioritySeed(Seedable):

    order = 60

    def seed(self):
        for name, level, delay_hours in PRIORITIES:
            if Priority.query.filter_by(name=name).first() is not None:
                continue

            app.logger.debug(f"Seed priority {name}")
            db.session.add(Priority(name=name, level=level, delay_hours=delay_hours))

        db.session.commit()