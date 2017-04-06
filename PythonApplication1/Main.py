import pprint

from db import db
from googleapiclient.discovery import build

query = "SELECT id, jobID, sentence FROM jobs"
a = db(query)

def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="AIzaSyAGQn6AtJjd1oIkh7eQnrQHiX1l_2eN8Jk")

  res = service.cse().list(
      q='technology',
      cx='002695577753650021296:clmhjicmmhm',
    ).execute()
  pprint.pprint(res)

main()