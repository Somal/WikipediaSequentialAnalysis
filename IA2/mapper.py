import os
import sys

EXCEPTED_TAGS = ['Media:',
                 'Special:',
                 'Talk:',
                 'User:',
                 'User_talk:',
                 'Project:',
                 'Project_talk:',
                 'File:',
                 'File_talk:',
                 'MediaWiki:',
                 'MediaWiki_talk:',
                 'Template:',
                 'Template_talk:',
                 'Help:',
                 'Help_talk:',
                 'Category:',
                 'Category_talk:',
                 'Portal:',
                 'Wikipedia:',
                 'Wikipedia_talk:', ]

EXCEPTED_EXTENSTIONS = ['.jpg', '.gif', '.png', '.JPG', '.GIF', '.PNG', '.txt', '.ico']
EXCEPTED_TITLES = ['404_error/',
                   'Main_Page',
                   'Hypertext_Transfer_Protocol',
                   'Search']
for line in sys.stdin:
    line = line.strip()
    if line[:2].lower() == 'en':
        try:
            project_name, page_title, number_of_access, total_data = line.split()

            tags_including = False
            for tag in EXCEPTED_TAGS:
                if page_title.startswith(tag):
                    tags_including = True
                    break

            if not tags_including:
                if not page_title.split(':')[-1][0].islower():
                    extension_including = False
                    for ext in EXCEPTED_EXTENSTIONS:
                        if page_title.endswith(ext):
                            extension_including = True
                            break

                    if not extension_including:
                        title_including = False
                        for title in EXCEPTED_TITLES:
                            if page_title == title:
                                title_including = True
                                break

                        if not title_including:
                            file_name = os.environ['mapreduce_map_input_file"']
                            date, time = file_name.split()[1:]
                            date = date[-2:]
                            print("{}\t{}".format(page_title, number_of_access))
        except:
            pass
