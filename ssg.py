import typer
from ssg.site import site
import ssg.parsers


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest, }
    Site(**config).build()

typer.run(main)    
