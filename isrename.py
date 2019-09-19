import os

def get_new_sequence(files,rename,pad,start=1):
    '''
    input:
        files is a list of full file paths to rename
        pad is the number of digits to pad the new sequence
        start is the first frame of new sequence
    returns a list. each element is another list containing [file dir, old name, new name, True/False if renamed]
    '''
    count = start
    renamed_files = []
    for item in files:
        dir, fname = os.path.split(item)
        base, ext = os.path.splitext(fname)
        renamed = rename+str(count).zfill(pad)+ext
        rename_full_path = (os.path.join(dir,renamed))
        renamed_files.append([dir,fname,renamed,False])
        count +=1
    return renamed_files

def get_dir_endswith(dir,ext):
    '''
    input:
        dir: directory containing files or folders
        ext: ending part of a folder or file, such as extension
    returns:
        sorted list of files that end with ext
    '''
    files = []
    for file in os.listdir(dir):
        if file.endswith(ext):
            files.append(os.path.join(dir,file))
    files = sorted(files)
    return files


def rename_files_and_folders(sequence_to_rename):
    '''
     sequence_to_rename is a list. Each element is another list containing [file dir, old name, new name, True/False if renamed]
     returns nothing, but modifies the sequence_to_rename
    '''
    for i in sequence_to_rename:
        current_name = os.path.join(i[0],i[1])
        new_name = os.path.join(i[0],i[2])
        if not os.path.exists(new_name):
            os.rename(current_name, new_name)
            if os.path.exists(new_name):
                i[3] = True
    print ("naming finished")


def check_rename_successful(sequence_to_rename):
    '''
    input is a sequence_to_rename [str "directory",str "Origial Name",str "New Name",True/False if successful]
    '''
    for i in sequence_to_rename:
        if i[3] == False:
            return False
    return True

user_folder = input("directory: ")
user_input_ext = input("file extension: ")
user_input_name = input("target name: ")
user_input_pad = input("padding")


files = get_dir_endswith(user_folder,user_input_ext)
sequence_to_rename = get_new_sequence(files,user_input_name,int(user_input_pad))
rename_files_and_folders(sequence_to_rename)
if check_rename_successful(sequence_to_rename):
    print ("rename successfull")
else:
    print ("some files were not able to be renamed")
