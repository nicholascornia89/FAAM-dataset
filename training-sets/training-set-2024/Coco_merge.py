import os
import copy
import json
from pycocotools.coco import COCO

def merge_cocojson_files(main_dir):
    # Initialize COCO object to hold merged data
    merged_data = COCO()

    # Create a list to store all images and annotations
    images = []
    annotations = []

    # Iterate through all subdirectories and files in the main directory
    for root, dirs, files in os.walk(main_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                # Load COCO annotations from each file
                coco = COCO(file_path)

                # Extend the images and annotations lists
                images.extend(coco.dataset['images'])

                # Update the file_name field in images to include subdirectory
                for img in coco.dataset['images']:
                    #version with full relative path
                    #img['file_name'] = os.path.relpath(os.path.join(root, img['file_name']), main_dir)
                    #version with only filename
                    img['file_name'] = os.path.basename(os.path.join(root, img['file_name']))
                annotations.extend(coco.dataset['annotations'])

    # Update the images and annotations in the merged COCO object
    merged_data.dataset['images'] = copy.deepcopy(images)
    merged_data.dataset['annotations'] = copy.deepcopy(annotations)

    # Update image and annotation IDs to ensure consistency
    merged_data.createIndex()

    # Save merged annotations to a new JSON file
    merged_data_path = os.path.join(main_dir, 'merged_cocojson.json')
    with open(merged_data_path, 'w') as f:
        json.dump(merged_data.dataset, f)

# Specify the main directory containing the subdirectories with cocojson files
main_directory = './'

# Call the function to merge the cocojson files
merge_cocojson_files(main_directory)
