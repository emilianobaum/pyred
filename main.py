from lib import redminelib
from json import load


class RT():

    def load_config(self):
        with open("config/configuration.json") as fp:
            data = load(fp)
            
        return data["redmine"], data["telegram"]
    def __init__(self):
        redmine, telegram = self.load_config()
        conn = redminelib.Redmine(redmine["host"], (redmine["user"], redmine["passwd"]))
        print("CONN: ",conn)
        print(conn.getProjects())

RT()