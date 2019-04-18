# Data pipeline and processing file for gelsight experiments
# borrowed heavily from python notebook included in google drive (https://drive.google.com/drive/folders/1wHEg_RR8YAQjMnt9r5biUwo5z3P6bjR3)

import numpy as np
import matplotlib.pyplot as plt
import deepdish as dd
# import progressbar
  
folderIn = 'data/'
fields = [
        'object_name',
        'is_gripping',
        'kinectA_rgb_before',
        'kinectA_rgb_during',
        'kinectA_rgb_after',
        'gelsightA_before',
        'gelsightA_during',
        'gelsightA_after',
        'gelsightB_before',
        'gelsightB_during',
        'gelsightB_after',
    ]

def load_file(namefile='calandra_corl2017_000.h5'):
    # Load data from file
    print('Loading file: %s' % namefile)
    t = dd.io.load(folderIn+namefile)
    n_data = len(t)
    print("N data: %d" % n_data)
    return t

def load_all_files():
    # Load all files (beware of running out ot memory!)
    extension_in = 'h5'
    namefiles = [each for each in os.listdir(folderIn) if each.endswith(extension_in)]
    namefiles.sort()
    print('Number files: %d' % len(namefiles))
    t=[]
    for namefile in namefiles:
        # Load data from file
        print('Loading file: %s' % namefile)
        t = t + dd.io.load(folderIn+namefile)
        n_data = len(t)
        print("N data: %d" % n_data)
    return t

def rotate90(im):
    return np.rot90(im)

def visualize_data(t, idx):
    # Visualize the images from a given experiment
    idx = 1  # index experiment
    experiment = t[idx]

    print('Object: %s' % t[idx][fields[0]])

    if experiment[fields[1]]:
        print('Grasp successful!')
    else:
        print('Grasp failed :(')
        
    # Kinect A
    # Before moving the gripper to the object
    plt.figure()
    plt.imshow(experiment[fields[2]])
    # Just before lift off (after closing the fingers)
    plt.figure()
    plt.imshow(experiment[fields[3]])
    # This is 4 seconds after attempting the lift
    plt.figure()
    plt.imshow(experiment[fields[4]])

    # Gelsight A (Rotated)
    # Before moving the gripper to the object
    plt.figure()
    plt.imshow(experiment[fields[5]])
    # Just before lift off (after closing the fingers)
    plt.figure()
    plt.imshow(experiment[fields[6]])
    # This is 4 seconds after attempting the lift
    plt.figure()
    plt.imshow(experiment[fields[7]])

    # Gelsight B (Rotated)
    # Before moving the gripper to the object
    plt.figure()
    plt.imshow(experiment[fields[8]])
    # Just before lift off (after closing the fingers)
    plt.figure()
    plt.imshow(experiment[fields[9]])
    # This is 4 seconds after attempting the lift
    plt.figure()
    plt.imshow(experiment[fields[10]])


