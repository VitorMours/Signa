from typing import List, Optional

from courses.models.course import Course 
from courses.serializers.course_serializer import CourseSerializer
from django.db import transaction
from uuid import UUID 

class CourseService:
    
    
    @staticmethod 
    @transaction.atomic
    def create_course(course_data: dict) -> Course:
        course = Course.objects.create(**course_data)
        return course 
    
    @staticmethod 
    def get_all_courses() -> List[Course]:
        return list(Course.objects.all())
    
    @staticmethod   
    def get_course_by_id(uuid: UUID) -> Optional[Course] | None:
        try:
            return Course.objects.filter(id=uuid).first()
        except Course.DoesNotExist:
            return None
    
    @staticmethod 
    @transaction.atomic
    def update_course(uuid: UUID, new_data) -> None:
        try:
            course =  Course.objects.filter(id=uuid).first()
            for key, value in new_data.items():
                setattr(course, key, value)
            course.save()
            return course
        except Course.DoesNotExist:
            return ValueError("This Course does not exists") 
    
    @staticmethod 
    @transaction.atomic
    def deactivate_course(uuid: UUID) -> None:
        try:
            course =  Course.objects.filter(id=uuid).first()
            course.is_active = False
            course.save()
            return course
        except Course.DoesNotExist:
            return ValueError("This Course does not exists") 
    