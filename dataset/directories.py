import os

CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
EGOHANDS_DATASET_URL = 'http://vision.soic.indiana.edu/egohands_files/egohands_data.zip'
EGOHANDS_DIR = rf'{CURRENT_DIR_PATH}/egohands'
EGOHANDS_DATA_DIR = rf'{EGOHANDS_DIR}/_LABELLED_SAMPLES'

ANNOTATIONS_DIR = rf'{CURRENT_DIR_PATH}/annotations'
AUGMENTED_EGOHANDS_DIR = rf'{EGOHANDS_DIR}/_AUGMENTED_SAMPLES'
AUGMENTED_ANNOTATIONS_DIR = rf'{ANNOTATIONS_DIR}/_AUGMENTED_SAMPLES'

INPUT_IMG_DIR = rf"{EGOHANDS_DIR}/_LABELLED_SAMPLES"
GROUND_TRUTH_DIR = rf"{ANNOTATIONS_DIR}/_GROUND_TRUTH_DISJUNCT_HANDS"
WEIGHT_MAPS_DIR = rf"{ANNOTATIONS_DIR}/_WEIGHT_MAPS"
INPUT_IMG_DIR_640_360 = rf"{INPUT_IMG_DIR}_640_360"
GROUND_TRUTH_DIR_640_360 = rf"{GROUND_TRUTH_DIR}_640_360"
WEIGHT_MAPS_DIR_640_360 = rf"{WEIGHT_MAPS_DIR}_640_360"
BALANCED_WEIGHT_MAPS_DIR_640_360 = rf"{WEIGHT_MAPS_DIR_640_360}_BALANCED"

AUG_INPUT_IMG_DIR = rf"{AUGMENTED_EGOHANDS_DIR}/_LABELLED_SAMPLES"
AUG_GROUND_TRUTH_DIR =  rf"{AUGMENTED_ANNOTATIONS_DIR}/_GROUND_TRUTH_DISJUNCT_HANDS"
AUG_WEIGHT_MAPS_DIR = rf"{AUGMENTED_ANNOTATIONS_DIR}/_WEIGHT_MAPS"

AUG_INPUT_IMG_DIR_640_360 = rf"{AUG_INPUT_IMG_DIR}_640_360"
AUG_GROUND_TRUTH_DIR_640_360 =  rf"{AUG_GROUND_TRUTH_DIR}_640_360"
AUG_WEIGHT_MAPS_DIR_640_360 = rf"{AUG_WEIGHT_MAPS_DIR}_640_360"
BALANCED_AUG_WEIGHT_MAPS_DIR_640_360 = rf"{AUG_WEIGHT_MAPS_DIR_640_360}_BALANCED"
    
