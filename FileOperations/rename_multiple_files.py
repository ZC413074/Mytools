import os


def rename_slash_blackslash(path_input, slash_in_path=r'\\', slash_in_outpath='/'):
    """
    replace the "\" or "\\" in path name to "/" 

    Parameters
    ----------

    path_input       : file path of files that need to be rename.

    slash_in_path    : "\\" or r"\\" in input path name.

    slash_in_outpath : '/' in output path name .

    Tips
    ----------
    the path_input need to be unescaped.When we add a letter 'r' in the beginning  of the path_input, the path input will be unescaped,
    such as path_input=r"G:\data\test_20210618\reconstruction_image".

    """
    path_output = path_input.replace(slash_in_path, slash_in_outpath)
    return path_output


def covert_str_filename_to_num_name(path_input, path_output, digit_width):
    """
    Read file names from input file, which is ordered in lexicographical order. Then rename the file by the number in in lexicographical order.
    Finally, 0 is added to the beginning of the name, when the digital width of name is smaller than defined digital width.

    Parameters
    ----------

    path_input : file path of files that need to be rename.

    path_output : file path of files to store, whoes files renamed.

    digit_width : the width of digit.

    """
    raw_names = os.listdir(path_input)
    image_format = str(raw_names[0][-4:])
    for i in range(len(raw_names)):
        os.rename(os.path.join(path_input, str(
            raw_names[i])), os.path.join(path_output, str(i).rjust(digit_width, '0')+image_format))


def read_all_files(path_input, format='.txt'):
    """
    Read all file names from input file path, which is specified in a specific format.

    Parameters
    ----------

    path_input : file path of files that need to be read.

    format     : the format of files to be read.

    """
    file_names = []
    raw_names = os.listdir(path_input)
    full_name = [os.path.join(path_input, name) for name in raw_names]
    for i in range(len(full_name)):
        if os.path.splitext(full_name[i])[1] == format:
            file_names.append(full_name[i])
    return file_names


if __name__ == "__main__":

    ########### covert_str_filename_to_num_name #########
    path_input = r"G:\data\test_20210728\reconstruction_image--"
    path_input = rename_slash_blackslash(path_input,'\\', '/')
    print("input name:",path_input)
    path_output=path_input
    print("output name:",path_output)
    covert_str_filename_to_num_name(path_input, path_input, 4)

    ########### read_all_files #########
    #path_input = r"F:\SVN\Personal_folder\zc\实验数据\test_20210714\2\1"
    #path_input = rename_slash_blackslash(path_input,'\\', '/')
    #print("input name:",path_input)
    #names = read_all_files(path_input, '.bmp')
    #print(names)


# A = [x for x in raw_names if x>=5000 and x<=5010]
# B = [x for x in raw_names if x>=5011 and x<=5100]
# C = [x for x in raw_names if x>=5101 and x<=6000]
# D = [x for x in raw_names if x>=6001 and x<=8707]
# A=sorted(A)
# B=sorted(B)
# C=sorted(C)
# D=sorted(D)
# for i in range(len(D)):
#     os.rename(os.path.join(path_input,str(D[i])+'.bmp'), os.path.join(path_input,"{:0>4}".format(str(i))+'.bmp'))
# for i in range(len(C)):
#     os.rename(os.path.join(path_input,str(C[i])+'.bmp'), os.path.join(path_input,"{:0>4}".format(str(i+len(D)))+'.bmp'))
# for i in range(len(B)):
#     os.rename(os.path.join(path_input,str(B[i])+'.bmp'), os.path.join(path_input,"{:0>4}".format(str(i+len(D)+len(C)))+'.bmp'))
# for i in range(len(A)):
#     os.rename(os.path.join(path_input,str(A[i])+'.bmp'), os.path.join(path_input,"{:0>4}".format(str(i+len(D)+len(C)+len(B)))+'.bmp'))
