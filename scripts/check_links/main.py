import json
import re

from check_links.config import Config
from check_links.content import Content

if __name__ == "__main__":
    config = Config("config.yaml")
    content = Content(config.content)

    broken_files = {}
    # Check that file exists for every link
    for jupyter_notebook in content.files:
        root_dir = jupyter_notebook.parent
        for cell in json.loads(jupyter_notebook.read_text())["cells"]:
            for word in cell["source"]:
                # If [the name](file.extension) is found, check that the file.extension exists
                for link in re.findall(r"\[(.*?)\]\((.*?)\)", word):
                    target = root_dir / link[1]
                    if not target.exists():
                        broken_files.setdefault(str(jupyter_notebook), []).append(link[1])

    # Print broken links
    for file, links in broken_files.items():
        print(f"Error in {file}: File not found for link(s): {', '.join(links)}")
