import os
from pathlib import Path

import dotenv
from loguru import logger
from quart import Quart, send_from_directory
from quart_cors import cors

dotenv.load_dotenv()

app = Quart(
    __name__,
    static_url_path="",
    static_folder=str(Path(os.getcwd()) / "sui" / "dist"),
    template_folder=str(Path(os.getcwd()) / "sui" / "dist"),
)

app = cors(
    app,
    send_origin_wildcard=False,
    allow_credentials=True,
    allow_origin=[
        f"http://0.0.0.0:{os.environ['SUI_PORT_ALLOW_ORIGIN']}",
        f"http://localhost:{os.environ['SUI_PORT_ALLOW_ORIGIN']}",
        f"http://127.0.0.1:{os.environ['SUI_PORT_ALLOW_ORIGIN']}",
        f"https://0.0.0.0:{os.environ['SUI_PORT_ALLOW_ORIGIN']}",
        f"https://localhost:{os.environ['SUI_PORT_ALLOW_ORIGIN']}",
        f"https://127.0.0.1:{os.environ['SUI_PORT_ALLOW_ORIGIN']}",
    ],
    allow_headers=["*"],
)

logger.info(f"Using static folder path=[{str(Path(os.getcwd()) / 'sui' / 'dist')}]")
logger.info(f"Using template folder path=[{str(Path(os.getcwd()) / 'sui' / 'dist')}]")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
async def main(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        response = await send_from_directory(app.static_folder, path)
    else:
        response = await send_from_directory(app.static_folder, "index.html")
    return response
