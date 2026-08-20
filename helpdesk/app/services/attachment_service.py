from app.framework.service.abstract_service import AbstractService
from app import app, db
from app.models.attachment import Attachment
from app.mappers.attachment_mapper import AttachmentMapper
from app.framework.decorators.injectable import injectable
import os
from flask import current_app

@injectable
class AttachmentService(AbstractService):

    def find_all(self):
        """Toutes les pièces jointes (sous forme de DTO)."""

        try:
            attachments = Attachment.query.all()

            return [AttachmentMapper.entity_to_dto(attachment) for attachment in attachments]

        except Exception as e:
            app.logger.error(f"Error |find all attachment : {e}")   

    def find_one_entity(self, entity_id: int):
        """Une pièce jointe par sa clé primaire, ou None.""" 

        try:
            attachment = db.session.get(Attachment, entity_id)

            if attachment is None:
                return None

            return attachment

        except Exception as e:
            app.logger.error(f"Error |find all attachment : {e}")
            return None 

    def find_one(self, entity_id: int):
        """Un DTO de la pièce jointe par sa clé primaire, ou None."""  

        try:
            attachment = db.session.get(Attachment, entity_id)
            
            if attachment is None:
                return None

            return AttachmentMapper.entity_to_dto(attachment)
        
        except Exception as e:
            app.logger.error(f"Error |find all attachment : {e}")
            return None 

    def find_one_by(self, **kwargs):
        """Une pièce jointe sur base d'un critère (exemple ticket_id)."""   
        try:
            attachment = Attachment.query.filter_by(**kwargs).one_or_none()

            if attachment is None:
                return None

            return AttachmentMapper.entity_to_dto(attachment)
        
        except Exception as e:
            app.logger.error(f"Error |find all attachment : {e}")
            return None 

    def insert(self, data):
        """Crée une pièce jointe à partir d'un formulaire validé."""
        try:
            form= data['form']
            author_id = data['author_id']
            ticket_id = data['ticket_id']

            file_data = form.attachment.data

            if not file_data:
                return None

            filename = file_data.filename

            relative_path = os.path.join("uploads", "attachments", filename)

            upload_folder = os.path.join(current_app.root_path, "uploads", "attachments")
            os.makedirs(upload_folder, exist_ok=True)

            absolute_path = os.path.join(upload_folder, filename)
            file_data.save(absolute_path)

            attachment = Attachment()

            attachment = AttachmentMapper.form_to_entity(
                form,
                attachment,
                author_id,
                ticket_id,
                relative_path 
            )

            db.session.add(attachment)
            db.session.commit()

            return AttachmentMapper.entity_to_dto(attachment)

        except Exception as e:
            app.logger.error(f"Error | insert attachement: {e}")
            db.session.rollback()
            return None  

    def update(self, entity_id: int, data):
        """Met à jour une pièce jointe existante."""

        try:
            attachment =  db.session.get(Attachment, entity_id)

            if attachment is None:
                return None

            form = data['form']
            author_id = data['author_id']
            ticket_id = data['ticket_id']

            attachment = AttachmentMapper.form_to_entity(form, attachment, author_id, ticket_id)

            db.session.commit()

            return AttachmentMapper.entity_to_dto(attachment) 
        
        except Exception as e:
            app.logger.error(f"Error | update attachement: {e}")
            db.session.rollback()
            return None  

    def delete(self, entity_id: int):
        """Supprime une pièce."""
        try:
            attachment = db.session.get(Attachment, entity_id)

            if attachment is None:
                return None

            db.session.delete(attachment)
            db.session.commit()

            app.logger.debug(f"La pièce jointe {entity_id} a bien été supprimée.")
            return True
        
        except Exception as e:
            app.logger.error(f"Error | delete attachement: {e}")
            db.session.rollback()
            return None  