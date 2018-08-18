import requests
import sys
from urllib.parse import urlparse, parse_qsl

SERVER = "https://mastodon.social"
#SERVER = "http://localhost:8102"

ENDPOINT = SERVER + "/api/v1/timelines/public"
LOCAL = False
target = "&local=true" if LOCAL else ""

crawl_headers = {"User-Agent" : "BoosterOK/0.0.1 (github.com/zhuowei/boosterok)"}

def getquery(urlstr):
    return dict(parse_qsl(urlparse(urlstr).query))

def main(startid, stopId):
    if startid:
        nexturl = ENDPOINT + "?max_id=" + str(startid) + "&limit=40" + target
    else:
        nexturl = ENDPOINT + "?limit=40" + target
    while True:
        print(nexturl)
        req = requests.get(nexturl, headers=crawl_headers)
        req.raise_for_status()
        links = req.links
        outfilename = "timeline_" + getquery(links["prev"]["url"])["since_id"] + "_" + \
            getquery(links["next"]["url"])["max_id"] + ".json"
        with open(outfilename, "wb") as outfile:
            outfile.write(req.content)
        nexturl = links["next"]["url"]
        if int(getquery(links["next"]["url"])["max_id"]) <= stopId:
            print("stopped!", links, stopId)
            input()
            break

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None, int(sys.argv[2]) if len(sys.argv) > 2 else 0)