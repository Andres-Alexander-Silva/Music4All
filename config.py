class Config:
    SECRET_KEY = "MsrtUhjdShdjIhjC6gh4hjhAhkLfdL"

class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 8082
    MYSQL_HOST = "54.147.25.136"
    MYSQL_USER = "test"
    MYSQL_PASSWORD = "test1_*"
    MYSQL_DB = "Music4All"
    
config = {
    "development" : DevelopmentConfig
}