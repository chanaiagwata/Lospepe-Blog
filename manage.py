from app import create_app,db
from flask_script import Manager,Server
from app.models import User, Blogs, Comment, Quotes, Subscribers
from flask_migrate import Migrate, MigrateCommand




#Creating app instance
app = create_app('development')
  
manager = Manager(app)
manager.add_command('server',Server)

#Initialize Migrate class
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

#Create a shell context
@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User = User, Blogs = Blogs, Comment = Comment, Quotes  = Quotes, Subscribers = Subscribers)

if __name__ == '__main__':
    manager.run()