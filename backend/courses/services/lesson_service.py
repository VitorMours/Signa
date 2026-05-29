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
        return Lesson.objects.get(id=id)
    
    
    @staticmethod
    def create_lesson(lesson_data: dict) -> Lesson:
        with transaction.atomic():
            lesson = Lesson.objects.create(**lesson_data)
            return lesson 
    
    @staticmethod 
    def update_lesson() -> Lesson:
        pass 
    

    @staticmethod
    def delete_lesson() -> bool:
        pass 
    
