from core.services.base_model_service import BaseModelService
from resume.models import EducationInstitute, ProfessionalInstitute, Institute


class InstituteService(BaseModelService):
    model_class = Institute

    def update_delete_project_ranking(self, user, is_added=True):
        educational_institute_service = EducationInstituteService()
        educational_institutes = educational_institute_service.all(user=user)
        for educational_institute in educational_institutes:
            if is_added:
                educational_institute.institute.total_projects += 1
            else:
                if educational_institute.institute.total_projects > 0:
                    educational_institute.institute.total_projects -= 1
            educational_institute.institute.save()
        return

    def add_ranking_values(self, institute):
        institute = (
            self.get_model_class().objects.filter(id=institute.institute.id).first()
        )
        if institute.institute_type == "university":
            institute.total_members += 1
            institute.total_graduates += 1
        else:
            institute.total_members += 1
        institute.save()
        return

    def remove_ranking_values(self, institute):
        institute = (
            self.get_model_class().objects.filter(id=institute.institute.id).first()
        )
        if institute.institute_type == "university":
            institute.total_members -= 1
            institute.total_graduates -= 1
        else:
            institute.total_members -= 1
        institute.save()
        return

    def update_or_delete_gpa(self, educational_institute, is_added=True):
        institute = (
            self.get_model_class()
            .objects.filter(id=educational_institute.institute.id)
            .first()
        )
        if is_added:
            institute.total_gpa += 1
        else:
            institute.total_gpa -= 1
        institute.save()

    def get_current_gpa(self, educational_institute):
        institute = self.get_model_class().objects.filter(id=educational_institute.id).first()
        return institute.total_gpa

    def update_or_delete_publication(self, educational_institute, is_added=True):
        institute = (
            self.get_model_class()
            .objects.filter(
                id=educational_institute.institute.id, institute_type="university"
            )
            .first()
        )
        if institute:
            if is_added:
                institute.total_publications += 1
            else:
                if institute.total_publications > 0:
                    institute.total_publications -= 1
            institute.save()

    def update_or_delete_job_placement(self, user, is_added=True):
        educational_institute_service = EducationInstituteService()
        educational_institutes = educational_institute_service.all(user=user)
        for educational_institute in educational_institutes:
            institute = (
                self.get_model_class()
                .objects.filter(
                    id=educational_institute.institute.id, institute_type="university"
                )
                .first()
            )
            if institute:
                if is_added:
                    institute.total_job_placement += 1
                else:
                    if institute.total_job_placement > 0:
                        institute.total_job_placement -= 1
                institute.save()

    def add_batch_publication(self, user, is_added):
        educational_institute_service = EducationInstituteService()
        educational_institutes = educational_institute_service.all(user=user)
        for educational_institute in educational_institutes:
            self.update_or_delete_publication(educational_institute, is_added)


class EducationInstituteService(BaseModelService):
    model_class = EducationInstitute
    institute_service = InstituteService()

    def update_or_create_instance(self, validated_data_list, user, **kwargs):
        for validated_data in validated_data_list:
            previous_gpa = 0
            validated_data["user"] = user
            if validated_data.get("id"):
                previous_data = self.get_model_class().objects.filter(id=validated_data.get("id")).first()
                if previous_data:
                    previous_gpa = previous_data.result

            instance, created = self.get_model_class().objects.update_or_create(
                id=validated_data.get("id"), defaults=validated_data
            )
            if created:
                self.institute_service.add_ranking_values(instance)
                if instance.result == int(5):
                    self.institute_service.update_or_delete_gpa(instance)
            else:
                current_gpa = instance.result
                if int(previous_gpa) == 5 and int(current_gpa) < 5:
                    self.institute_service.update_or_delete_gpa(instance, is_added=False)
                elif int(previous_gpa) < 5 and int(current_gpa) == 5:
                    self.institute_service.update_or_delete_gpa(instance, is_added=True)


class ProfessionalInstituteService(BaseModelService):
    model_class = ProfessionalInstitute
    institute_service = InstituteService()

    def update_or_create_instance(self, validated_data_list, user, **kwargs):
        for validated_data in validated_data_list:
            validated_data["user"] = user
            instance, created = self.get_model_class().objects.update_or_create(
                id=validated_data.get("id"), defaults=validated_data
            )
            if created:
                self.institute_service.update_or_delete_job_placement(user, is_added=True)
