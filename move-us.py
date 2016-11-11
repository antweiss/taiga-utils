from taiga import TaigaAPI
import argparse

parser = argparse.ArgumentParser(description='Create Taiga issue')
parser.add_argument('--user', dest='user')
parser.add_argument('--passwd', dest='passwd')
parser.add_argument('--project', dest='project')
parser.add_argument('--storyid', dest='storyid')
parser.add_argument('--status', dest='status')


args = parser.parse_args()

api = TaigaAPI()

api.auth(username=args.user, password=args.passwd)

proj =  api.projects.get_by_slug(args.project)

us = proj.list_user_stories().get(ref=int(args.storyid))

us.update(status=proj.list_user_story_statuses().get(name=args.status).id)
