from data_generator import CACDDataset
from HYPERPARAMETERS import TRAIN_CSV_PATH, IMAGE_PATH, TEST_CSV_PATH, BATCH_SIZE
from models.old_school import OldSchoolMethod
import numpy as np
import time

def run():
    print('Start main')
    # Train
    s = time.time()
    train_dataset = CACDDataset(csv_path=TRAIN_CSV_PATH, img_dir=IMAGE_PATH)
    print('X y train cargados:', np.round(time.time()-s),'s')

    # Test
    s = time.time()
    test_dataset = CACDDataset(csv_path=TEST_CSV_PATH, img_dir=IMAGE_PATH)
    print('X y test cargados:', np.round(time.time()-s),'s')

    s = time.time()
    OldSchoolMethod().run(train_dataset, test_dataset)
    print('Fin Old School Method:', np.round(time.time()-s),'s')

    



if __name__ == '__main__':
    run()