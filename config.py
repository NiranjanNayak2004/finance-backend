class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456789@localhost/finance_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret-key"