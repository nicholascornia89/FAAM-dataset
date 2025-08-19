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

    # Create a list and integer index to map old and new image ids
    id_values_list = []

    id_value = 1

    annotation_value = 1

    # Iterate through all subdirectories and files in the main directory
    for root, dirs, files in os.walk(main_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                # Load COCO annotations from each file
                print(f"Loading COCO data from {file}... ")
                coco = COCO(file_path)

                # Update the file_name field in images to include subdirectory
                for img in coco.dataset["images"]:
                    # version with full relative path
                    # img['file_name'] = os.path.relpath(os.path.join(root, img['file_name']), main_dir)
                    # version with only filename
                    img["file_name"] = os.path.basename(
                        os.path.join(root, img["file_name"])
                    )
                    # record old and new id in list
                    id_values_list.append({"old_id": img["id"], "new_id": id_value})
                    # assign new id value
                    img["id"] = id_value
                    id_value += 1

                    # print(img)
                    # input()

                # Extend the images and annotations lists
                images.extend(coco.dataset["images"])

                # Update annotations to point to the new image ids
                for ann in coco.dataset["annotations"]:
                    # update annotation value
                    ann["id"] = annotation_value
                    annotation_value += 1
                    # update image_id
                    query = list(
                        filter(lambda x: x["old_id"] == ann["image_id"], id_values_list)
                    )
                    # print(ann)
                    # print(query)
                    # input()
                    ann["image_id"] = query[0]["new_id"]

                # Extend annotations list
                annotations.extend(coco.dataset["annotations"])

                # Refresh id values list
                id_values_list = []

    # Update the images and annotations in the merged COCO object
    merged_data.dataset["images"] = copy.deepcopy(images)
    merged_data.dataset["annotations"] = copy.deepcopy(annotations)

    # Update image and annotation IDs to ensure consistency not working
    merged_data.createIndex()

    # Save merged annotations to a new JSON file
    merged_data_path = os.path.join(main_dir, "merged_cocojson.json")
    with open(merged_data_path, "w") as f:
        json.dump(merged_data.dataset, f, indent=2)


# Specify the main directory containing the subdirectories with cocojson files
main_directory = "./"

# Call the function to merge the cocojson files
merge_cocojson_files(main_directory)
