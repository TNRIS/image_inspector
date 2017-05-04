# -*- coding: utf-8 -*-

import click
from image_inspector import find_images


@click.command()
@click.argument('image_directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--overwrite/--no-overwrite', default=False, help='Overwrite existing inventory files.')
def inspect(image_directory, overwrite):
    """Console interface for the image-inspector tool"""
    find_images(image_directory, overwrite=overwrite)


if __name__ == "__main__":
    inspect()
