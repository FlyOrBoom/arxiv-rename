#!/usr/bin/env python3

import sys
import os
import time
import datetime
import logging
import re
import arxiv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

regex = re.compile(r"^(\d+\.?\d+v\d+).*\.pdf$")
client = arxiv.Client()

class MyEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory: return

        dirname = os.path.dirname(event.src_path)
        basename = os.path.basename(event.src_path)

        match = regex.match(basename)
        if not match: return

        paper_id = match.group(1)
        paper = next(client.results(arxiv.Search(id_list=[paper_id])))

        title = paper.title
        updated = str(paper.updated)[:4]
        author = paper.authors[0].name
        if len(paper.authors) > 1: author += " et al"
        newname = f"{author} {updated} - {title}.pdf".replace("/", "_")

        os.rename(event.src_path, os.path.join(dirname, newname))
        print(f"{paper_id} -> {newname}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    logging.info(f'start watching directory {path!r}')
    observer = Observer()
    observer.schedule(MyEventHandler(), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
