from reflex import Config

port: int = 3306
user: str = "root"
host: str = "127.0.0.1"
password: str = ""
database: str = "grupal"

config = Config(
    app_name="grupal",
    db_url="sqlite:///reflex.db",
)
