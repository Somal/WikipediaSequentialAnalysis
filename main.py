PATH_TO_FILE = 'pagecounts-20160101-000000'
FOLDER_FOR_TMP_FILES = 'tmp'
SPLIT_THRESHOLD = 100


def split(file):
    def get_tmp_file(folder, number):
        """ Creator of temporary files"""
        return open("{}/split{}".format(folder, number), 'w')

    count_of_files = 0
    i = 0
    tmp_file = get_tmp_file(FOLDER_FOR_TMP_FILES, count_of_files)
    for row in file:
        # Recreate file if this is full
        if i == SPLIT_THRESHOLD:
            i = 0
            count_of_files += 1
            tmp_file = get_tmp_file(FOLDER_FOR_TMP_FILES, count_of_files)
        tmp_file.write(row)
        i += 1


if __name__ == '__main__':
    """
    Some pseudo-Hadoop engine for MapReduce implementation testing
    Don't use standard I/O because file can be very large
    """
    input_file = open(PATH_TO_FILE, 'r')
    # Splitting
    split(input_file)
