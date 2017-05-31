# -*- coding: utf-8 -*-
import csv
import os

import exifread


def find_images(base_directory, inventory_file_name="image_inventory",
                filter_extensions=[".tif"], tags=(), flatten_search=False,
                overwrite=False):
    """
    Iterate through a base directory to find all of the tif images in
    that directory and all sub-directories.

    Args:
        base_directory (str): the path to the base directory to traverse
        inventory_file_name (str): the name of the output CSV
        tags (list): named tags to collect, defaults to all
        flatten_search (bool): do NOT traverse sub-directories
        overwrite (bool): remove inventory file if it already exists
    """

    # Create a list of directories to iterate through
    for directory in os.listdir(base_directory):

        # Set a variable to the next directory
        directory_path = os.path.join(base_directory, directory)

        # Create a variable to hold the path of the output CSV
        image_inventory = os.path.join(directory_path,
                                       '{}.csv'.format(inventory_file_name))

        # Check to see if the output file aleady exists and if the overwrite
        # param is set to true
        if os.path.exists(image_inventory) and overwrite:
            os.remove(image_inventory)

        # Iterate through the directory
        for root, dirs, files in os.walk(directory_path):

            # For each file in the directory, check to see if its file
            # extension matches the target file type
            for f in files:
                if os.path.splitext(f)[1].lower() in filter_extensions:

                    # If a matching file is located send it to the metadata
                    # function
                    get_image_metadata(
                        os.path.join(root, f),
                        image_inventory,
                        tags
                    )


def get_image_metadata(file_path, csv_file, named_tags):
    """
    Function accepts an image file path and writes the image's
    tag data to a CSV file.

    Args:
        file_path (str): the path to the image file
        csv_file (str): the path to the output CSV file
        named_tags (list): named tags to collect, defaults to all
    """

    # Open the image file to read the exif data
    with (open(file_path, 'rb')) as image_file:
        tags = exifread.process_file(image_file)

    # Check to see if the file already exists. If it does not
    # we need to mark that it will need a header
    add_header = False if os.path.exists(csv_file) else True

    # Create a set to hold field names and seed with Path
    fields = set()
    fields.add("Path")

    # Check to see if we need to add a header and do so, if necessary
    if add_header:
        if named_tags:
            fields.update(named_tags)
        else:
            fields.update(tags.keys())

    # Since the file already exists get the current field names
    else:
        with open(csv_file, "rb") as header_file:
            csv_reader = csv.reader(header_file)
            fields.update(next(csv_reader, []))

    # Open the CSV file to write the data
    with open(csv_file, "ab") as output_file:
        writer = csv.DictWriter(output_file, list(fields))
        if add_header:
            writer.writeheader()

        # Create a row that we can append data to
        image_data = {"Path": image_file.name}

        # Iterate through the file tags
        for tag in tags.keys():

            # See if we know about this tag, if the user has filtered the tags
            # and if the tag is in the user-defined filter
            if tag in fields and (not named_tags or tag in named_tags):

                # Assign the tag value to the key in the row dictionary
                image_data[tag] = tags[tag]
        writer.writerow(image_data)
