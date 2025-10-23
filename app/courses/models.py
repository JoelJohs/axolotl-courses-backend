from uuid import uuid4
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.users.models import ChapterProgress

class Course(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    title: str
    description: Optional[str] = None
    
    # Relación: Un curso tiene muchas secciones
    sections: List["Section"] = Relationship(back_populates="course")

class Section(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    title: str
    content: Optional[str] = None
    
    # Llave foránea al curso
    course_id: Optional[str] = Field(default=None, foreign_key="course.id")
    
    # Relaciones
    course: Optional[Course] = Relationship(back_populates="sections")
    chapters: List["Chapter"] = Relationship(back_populates="section")

class Chapter(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    title: str
    video_url: Optional[str] = None  # Ruta al video local o URL
    
    # Llave foránea a la sección
    section_id: Optional[str] = Field(default=None, foreign_key="section.id")
    
    # Relaciones
    section: Optional[Section] = Relationship(back_populates="chapters")
    progress: List["ChapterProgress"] = Relationship(back_populates="chapter")
