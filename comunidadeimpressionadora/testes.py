from main import app, database
from models import Usuario, Post

# Rodar esse primeiro
# with app.app_context():
#    database.create_all()

# Segundo
# with app.app_context():
#     usuario = Usuario(username='Everaldo', email='veve@gmail.com', senha='1234')
#     usuario2 = Usuario(username='Debora', email='deb@gmail.com', senha='1234')
#
#     database.session.add(usuario)
#     database.session.add(usuario2)
#
#     database.session.commit()


# Terceiro
# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(id=2).first()
#     print(usuario_teste.username)

# Quarto
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Primeiro post do Everaldo", corpo='Finalmente aq1ui está meu primeiro post')
#     database.session.add(meu_post)
#     database.session.commit()

# # Quinto
# with app.app_context():
#     post = Post.query.first()
#     print(post.autor.email)


with app.app_context():
    database.drop_all()
    database.create_all()

