class Config:
    SECRET_KEY = "MsrtUhjdShdjIhjC6gh4hjhAhkLfdL"

class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 8082
    
config = {
    "development" : DevelopmentConfig
}