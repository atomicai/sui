import os
from pathlib import Path

from loguru import logger
from quart import Quart, send_from_directory
from quart_cors import cors

app = Quart(
    __name__,
    static_url_path="",
    static_folder=str(Path(os.getcwd()) / "sui" / "dist"),
    template_folder=str(Path(os.getcwd()) / "sui" / "dist"),
)

app = cors(app, allow_origin=["http://127.0.0.1", "https://127.0.0.1"])

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
