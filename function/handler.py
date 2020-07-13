import json

from fs.onedatafs import OnedataFS

BLOCK_SIZE = 262144


def handle(req: bytes):
    """handle a request to the function
    Args:
        req (str): request body
    """
    args = json.loads(req)

    odfs = OnedataFS(args["host"], args["accessToken"],
                     force_direct_io=True,
                     insecure=True)

    with odfs.open(args["filePath"], 'r') as f:
        data = json.load(f)

    return json.dumps({"json": data})
