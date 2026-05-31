from courses.models.lesson import Lesson
from uuid import UUID
from typing import Optional, List
from django.db import transaction 


class LessonService:
    
    @staticmethod 
    def get_all_lessons() -> List[Lesson]:
        return list(Lesson.objects.all())
    
    @staticmethod 
    def get_lesson_by_id(id: UUID) -> Optional[Lesson]:
        try:
            return Lesson.objects.get(id=id)
        except Lesson.DoesNotExist:
            return None

    @staticmethod
    def create_lesson(lesson_data: dict) -> Lesson:
        with transaction.atomic():
            lesson = Lesson.objects.create(**lesson_data)
            return lesson 
    
    @staticmethod 
    def update_lesson(id: UUID, lesson_data: dict) -> Lesson:
        lesson = LessonService.get_lesson_by_id(id)
        if lesson is None:
            raise ValueError(f"Lesson with id {id} does not exists") 
        for key, value in lesson_data.items():
            setattr(lesson, key, value)
        lesson.save()
        return lesson
    
    @staticmethod
    def deactivate_lesson(id: UUID) -> bool:
        lesson = LessonService.get_lesson_by_id(id)
        if lesson is None:
            return False 
        lesson.is_active = False 
        lesson.save()
        return True 
    
