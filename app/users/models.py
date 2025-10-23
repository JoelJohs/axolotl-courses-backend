from datetime import datetime
from uuid import uuid4
from typing import TYPE_CHECKING, Optional, List
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Text

if TYPE_CHECKING:
    from app.courses.models import Chapter

class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relaciones
    chapter_progress: List["ChapterProgress"] = Relationship(back_populates="user")
    profile: Optional["UserProfile"] = Relationship(back_populates="user", sa_relationship_kwargs={"uselist": False})

class UserProfile(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    user_id: str = Field(foreign_key="user.id")
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    
    # Relación
    user: Optional[User] = Relationship(back_populates="profile")

class ChapterProgress(SQLModel, table=True):
    """
    Tabla puente para la relación muchos-a-muchos entre User y Chapter.
    Guarda el progreso de un usuario en un capítulo específico.
    """
    user_id: str = Field(foreign_key="user.id", primary_key=True)
    chapter_id: str = Field(foreign_key="chapter.id", primary_key=True)
    is_completed: bool = Field(default=False)
    notes: Optional[str] = Field(default=None, sa_column=Column(Text))
    
    # Relaciones
    user: Optional["User"] = Relationship(back_populates="chapter_progress")
    chapter: Optional["Chapter"] = Relationship(back_populates="progress")
