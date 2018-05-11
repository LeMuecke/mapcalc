import sys
import os
import glob

## This script ensures same number of files in ground-truth and predicted folder.
## When you encounter file not found error, it's usually because you have
## mismatched numbers of ground-truth and predicted files.
## You can use this script to move ground-truth and predicted files that are
## not in the intersection into a backup folder (backup2).
## This will retain only files that have the same name in both folders.

# change directory to the one with the files to be changed
path_to_gt = '../ground-truth'
path_to_pred = '../predicted'
backup_folder = 'backup2' # must end without slash

os.chdir(path_to_gt)
gt_files = glob.glob('*.txt')
if len(gt_files) == 0:
    print("Error: no .txt files found in ground-truth/")
    sys.exit()
os.chdir(path_to_pred)
pred_files = glob.glob('*.txt')
if len(pred_files) == 0:
    print("Error: no .txt files found in predicted/")
    sys.exit()

gt_files = set(gt_files)
pred_files = set(pred_files)
print('total ground-truth files:', len(gt_files))
print('total predicted files:', len(pred_files))
print()

gt_backup = gt_files - pred_files
pred_backup = pred_files - gt_files

def backup(folder, backup_files, backup_folder):
    # non-intersection files (txt format) will be moved to a backup folder
    if not backup_files:
        print('No backup required for', folder)
        return
    os.chdir(folder)
    ## create the backup dir if it doesn't exist already
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    for file in backup_files:
        os.rename(file, backup_folder + '/' + file)
    
backup(path_to_gt, gt_backup, backup_folder)
backup(path_to_pred, pred_backup, backup_folder)
print('total ground-truth backup files:', len(gt_backup))
print('total predicted backup files:', len(pred_backup))

intersection = gt_files & pred_files
print('total intersected files:', len(intersection))
print("Intersection completed!")
