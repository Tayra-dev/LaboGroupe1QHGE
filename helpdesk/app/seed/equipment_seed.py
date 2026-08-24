from app import app, db
from app.framework.seed.seedable import Seedable
from app.models.user import User
from app.models.equipment import Equipment
from app.models.site import Site
from app.seed import EQUIPMENT

class EquipmentSeed(Seedable):
    order = 60

    def seed(self):
        for name, type, serial, purchase_date, site_name, user_name in EQUIPMENT:
            if Equipment.query.filter_by(name=name).first():
                app.logger.debug(f"Seed equipment {name}: déjà présent")
                continue

            equipment = Equipment(
                name=name,
                type=type,
                serial=serial,
                purchase_date=purchase_date
            )



            # User
            user = User.query.filter_by(name=user_name).first()

            if user is None:
                app.logger.warning(f"Seed equipment {name}: user {user_name} absent")
                continue

            equipment.add_user(user)


            # Site
            site = Site.query.filter_by(name=site_name).first()

            if site is None:
                app.logger.warning(f"Seed equipment {name}: site {site_name} absent")
                continue

            equipment.add_site(site)

            db.session.add(equipment)
            app.logger.debug(f"Seed equipment {name}")

        db.session.commit()