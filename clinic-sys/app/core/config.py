# encriptar o passwords do usuário
SECRET_KEY = '123456'

#string conexao
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "clinicsys",
    senha = "123456",
    servidor = "localhost:5435",
    database = "postgres"
)