import os


def create_index_file(startpath, index_file):
    # os.walk
    # Generate a 3-tuple (dirpath, dirnames, filenames) by walking the tree either top-down or bottom-up.
    # - dirpath is a string, the path to the directory.
    # - dirnames is a list of the names of the subdirectories in dirpath (excluding '.' and '..').
    # - filenames is a list of the names of the non-directory files in dirpath.
    #
    # Note that the names in the lists contain no path components.
    # To get a full path (which begins with top) to a file or directory in dirpath, do:
    #   os.path.join(dirpath, name).

    for root, dirs, files in os.walk(startpath):

        # ignore files starting with '.'
        # files = [f for f in files if not f[0] == '.']

        # ignore directories starting with '.'
        dirs[:] = [d for d in dirs if not d[0] == '.']

        level = root.replace(startpath, '').count(os.sep) - 1
        indent = ' ' * 2 * level

        dir_path = os.path.basename(root)
        # if NOT ROOT directories:
        if dir_path != '.':
            # WRITE the Directory name
            #  bold     index_file.write('\n{}**{}**\n'.format(indent, dir_path))
            #  as a heading
            index_file.write('\n{}### {}\n'.format(indent, dir_path))
            # set the indent amount
            subindent = ' ' * 2 * (level + 1)
            # WRITE the filename
            for f in files:
                index_file.write('{}- [{}]({})\n'.format(subindent, f[:-3].replace('-', ' '), f[:-3]))
        # ROOT directory '.'
        else:
            for f in files:
                # don't link to '_Sidebar.md' or 'Home.md' in the sidebar
                if f == '_Sidebar.md':
                    continue
                if f == 'Home.md':
                    continue
                # WRITE the filename
                # bold
                index_file.write('{}- **[{}]({})**\n'.format('', f[:-3].replace('-', ' '), f[:-3]))


outputFile = open('_Sidebar.md', 'w')
create_index_file(".", outputFile)
outputFile.close()
