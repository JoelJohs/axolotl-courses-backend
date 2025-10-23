from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os

load_dotenv()

# URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Función para crear las tablas en la base de datos
def create_db_and_tables():
    # Importar los modelos para que SQLModel.metadata los registre
    import app.users.models  # noqa: F401
    import app.courses.models  # noqa: F401
    
    # Crear todas las tablas
    SQLModel.metadata.create_all(engine)

# Función para obtener una sesión de la base de datos e inyectar dependencias
def get_session():
    with Session(engine) as session:
        yield session