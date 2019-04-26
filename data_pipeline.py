# Data pipeline and processing file for gelsight experiments
# borrowed heavily from python notebook included in google drive (https://drive.google.com/drive/folders/1wHEg_RR8YAQjMnt9r5biUwo5z3P6bjR3)

import numpy as np
import matplotlib.pyplot as plt
import deepdish as dd
import cv2
from os import listdir
from os.path import isfile, join

# import progressbar
  
folderIn = '/Users/rkelly/mit/meng/spring/6.882/project/6.882FinalProject/out_data/'
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
out_dir = 'out_data/'

img_size = 256
# onlyfiles = [f for f in listdir(folderIn) if isfile(join(folderIn, f))]

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

def process_file(t, file_name):
    rgb_before = []
    rgb_during = []
    gelsightA_before = []
    gelsightA_during = []
    gelsightB_before = []
    gelsightB_during = []
    result = []
    for experiment in t:
        rgb_before.append(cv2.resize(experiment[fields[2]], dsize=(img_size, img_size)))
        rgb_during.append(cv2.resize(experiment[fields[3]], dsize=(img_size, img_size)))
        gelsightA_before.append(cv2.resize(experiment[fields[5]], dsize=(img_size, img_size)))
        gelsightA_during.append(cv2.resize(experiment[fields[6]], dsize=(img_size, img_size)))
        gelsightB_before.append(cv2.resize(experiment[fields[8]], dsize=(img_size, img_size)))
        gelsightB_during.append(cv2.resize(experiment[fields[9]], dsize=(img_size, img_size)))
        result.append(experiment[fields[1]])
    np.save(out_dir + 'rgb_before/' + file_name.split('.')[0] + '_rgb_before.npy', rgb_before)
    np.save(out_dir + 'rgb_during/' + file_name.split('.')[0] + '_rgb_during.npy', rgb_during)
    np.save(out_dir + 'gelsightA_before/' + file_name.split('.')[0] + '_gelsightA_before.npy', gelsightA_before)
    np.save(out_dir + 'gelsightA_during/' + file_name.split('.')[0] + '_gelsightA_during.npy', gelsightA_during)
    np.save(out_dir + 'gelsightB_before/' + file_name.split('.')[0] + '_gelsightB_before.npy', gelsightB_before)
    np.save(out_dir + 'gelsightB_during/' + file_name.split('.')[0] + '_gelsightB_during.npy', gelsightB_during)
    np.save(out_dir + 'result/' + file_name.split('.')[0] + '_result.npy', result)


def combine_files(directory):
    path = '/Users/rkelly/mit/meng/spring/6.882/project/6.882FinalProject/out_data/'
    onlyfiles = [f for f in listdir(path+directory) if isfile(join(path+directory, f))]
    combination = []
    for file in onlyfiles:
        combination.append(np.load(path+directory+file))
    out_arr = np.concatenate(combination)
    np.save(out_dir+directory.split('/')[0]+'_all.npy', out_arr)

def visualize_data(t, idx):
    # Visualize the images from a given experiment
    idx = 4  # index experiment
    experiment = t[idx]
    print('test')
    print('Object: %s' % t[idx][fields[0]])

    if experiment[fields[1]]:
        print('Grasp successful!')
    else:
        print('Grasp failed :(')
        
    # Kinect A
    # Before moving the gripper to the object
    plt.figure()
    print(len(experiment[fields[2]]))
    print(len(experiment[fields[2]][0]))
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
    print(len(experiment[fields[5]]))
    print(len(experiment[fields[5]][0]))
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


if __name__ == '__main__':
    # for filename in onlyfiles:
    #     t = load_file(filename)
    #     process_file(t, filename)
    #     del t
    dir_names = ['rgb_before/', 'result/']
    for dir in dir_names:
        combine_files(dir)


