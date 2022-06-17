SECRET_KEY = 'claytinho'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='number1245',
        servidor='localhost',
        database='jogoteca'
)