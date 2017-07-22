import urllib.request
import ssl

cert="/home/carl/work/python_ssl_server/server.pem"
req = urllib.request.Request("https://localhost:1443")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with urllib.request.urlopen(req, context=ctx, data=b'HACKER INFO') as r:
    print(r.read(300))
