from taiga import TaigaAPI
import argparse

parser = argparse.ArgumentParser(description='Create Taiga issue')
parser.add_argument('--user', dest='user')
parser.add_argument('--passwd', dest='passwd')
parser.add_argument('--project', dest='project')

args = parser.parse_args()

api = TaigaAPI()

api.auth(username=args.user, password=args.passwd)

proj =  api.projects.get_by_slug(args.project)

qa_user = ''

for user in api.users.list(project=proj.id):
	if user.username == 'Tobiko':
		print "qa_user will be" + str( user.id)
		qa_user = user.id

issue = proj.add_issue("New env for testing",
				proj.priorities.get(name='High').id,
				proj.issue_statuses.get(name='New').id,
				proj.issue_types.get(name='EnvVerification').id,
				proj.severities.get(name='Minor').id,
				description="Test Me!",
				assigned_to=qa_user
				)
#issue.set_attribute(2552, 'http://otomato.link')
