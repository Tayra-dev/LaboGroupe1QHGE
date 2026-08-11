from app import CATEGORIES, app, db
from app.framework.seed import Seedable
from app.models.category import Category


class CategorySeed(Seedable):

    order = 50

    def seed(self):
        for name, description in CATEGORIES:
            if Category.query.filter_by(name=name).first() is not None:
                continue

            app.logger.debug(f"Seed category {name}")
            db.session.add(Category(name=name, description=description))

        db.session.commit()