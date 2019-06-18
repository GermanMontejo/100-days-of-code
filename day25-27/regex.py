import re

def extract_course_times():
    """Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']"""
    flask_course = ('Introduction 1 Lecture 01:47',
                    'The Basics 4 Lectures 32:03',
                    'Getting Technical!  4 Lectures 41:51',
                    'Challenge 2 Lectures 27:48',
                    'Afterword 1 Lecture 05:02')
    timestamps = []
    for course in flask_course:
        timestamp = re.findall(r'[0-9]{2}:[0-9]{2}', course)
        timestamps.append(timestamp[0])

    return timestamps

#print(extract_course_times())

def get_all_hashtags_and_links():
    """Write a regular expression that returns this list:
       ['http://pybit.es/requests-cache.html', '#python', '#APIs']"""
    tweet = ('New PyBites article: Module of the Week - Requests-cache ',
             'for Repeated API Calls - http://pybit.es/requests-cache.html ',
             '#python #APIs')
    
    links_hashtags = []

    for t in tweet:
        lh = re.search(r'http:.*html|#[A-Za-z]*\s#[A-Za-z]*', t)
        if lh != None:
            lh_split = lh.group().split(' ')
            if len(lh_split) > 1:
                for s in lh_split:
                    links_hashtags.append(s)
            else:
                links_hashtags.append(lh.group())

    return links_hashtags

def match_first_paragraph():
    """Write a regular expression that returns  'pybites != greedy' """
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    h = re.search(r'<p>.*?</p>', html)
    return re.sub(r'<\w*>|</\w>', '', h.group())

print(match_first_paragraph())