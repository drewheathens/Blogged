from app import *
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Article,Comment

app = create_app('s')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)
'''
adds the db instance and models to the shell session
'''

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Article = Article, Comment = Comment)
if __name__ == '__main__':
    manager.run()
