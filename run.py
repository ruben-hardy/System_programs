#!/usr/bin/python

'''
Usage:
run.py </path/module_info.json>
'''

# Retrieve module settings

import sys
import re
import os
import json
import ftplib
import collections
from analysis_launcher import launcher, convert_stage_to_folder_name
sys.path.append("../../")
sys.path.append("../../job.json")
sys.path.append("/usr/lib/python2.6/site-packages")
import jcf

m = jcf.Module(sys.argv[1])
settings = m.get_module_settings()
working_area = m.get_stage_working_area()
stage = m.get_stage_id()
stage_name = convert_stage_to_folder_name(stage)
pstage = stage
stage = re.sub(r'[^(a-zA-Z: )]', '', stage)
c = working_area.split("/")
cirrusid = c[5]
adj_lines = int(settings.get('line_count', [0])[0])
json_data = ""
pattern_files = []
curdir = []
patterns = settings.get('Pattern_Files', None)
pattern_server = settings.get('Pattern_Server', None)
pattern_repo = pattern_server[0].split(",")
pattern_ftp_creds = str(pattern_repo[2])
pattern_ftp_pwd = ''
pattern_ftp_usr, pattern_ftp_ip = pattern_ftp_creds.split("@")
if ":" in pattern_ftp_usr:
    pattern_ftp_usr, pattern_ftp_pwd = pattern_ftp_usr.split(":")


def copy_patternfiles(address, usr, pwd, patterns_files):
    """
    Download pattern files from ftp server to cirrus local folder
    :return: local paths to pattern files.
    """
    pat_files = []
    try:
        ftp = ftplib.FTP(address, usr, pwd)
        for pattern in patterns_files:
            filename = '/ci/data/autotest/tmp/ftp/{0}'.format(os.path.basename(pattern))
            ftp.retrbinary('RETR {0}'.format(pattern), open(filename, 'wb').write)
            pat_files.append(filename)
        ftp.quit()
    except ftplib.all_errors, msg:
        sys.stderr.write('\nFTP ERROR: {0}'.format(msg))
    if len(patterns_files) != len(pat_files):
        sys.stderr.write('\nERROR: Fail to download some of the pattern file from Repo Server')
        exit(1)
    return pat_files


patterns = copy_patternfiles(pattern_ftp_ip, pattern_ftp_usr, pattern_ftp_pwd, patterns)
if stage == "Testcase: Repo Server Analysis":
    os.popen('rm -rf /ci/data/autotest/tmp/srv')
    repofolder = settings.get('Repo_Folder', None)
    reposerver = settings.get('Repo_Server', None)
    repo = reposerver[0].split(",")
    repo_path = "{0}{1}".format(str(repo[3]), "".join(repofolder))
    ftp_creds = str(repo[2])
    ftp_pwd = ''
    ftp_usr, ftp_ip = ftp_creds.split("@")
    if ":" in ftp_usr:
        ftp_usr, ftp_pwd = ftp_usr.split(":")
    with open('../../job.json') as job_json:
        json_data = json.load(job_json)
    ftp_lst = ['ftp', ftp_ip, ftp_usr, ftp_pwd, repo_path]
    launcher(ftp_lst, patterns, cirrusid, adj_lines[0], stage_name)
elif stage == "Testcase: Cirrus Job Analysis":
    job_ids = settings.get('job_id')
    job_list = job_ids.split(",")
    job_list = list(set(job_list))
    junk = []
    for item in job_list:
        try:
            if type(int(item)) == int:
                continue
            else:
                junk.append(item)
                continue
        except ValueError:
            junk.append(item)
            continue
    if junk:
        sys.stderr.write('ERROR: {0} is not a valid job id'.format(', '.join(junk)))
        exit(1)
    job_list.insert(0, 'job')
    with open('../../job.json') as job_json:
        json_data = json.load(job_json)
    if not patterns:
        sys.stderr.write('No pattern file was selected')
    else:
        launcher(job_list, patterns, cirrusid, adj_lines, stage_name)
        pass
elif stage == "Testcase: Current Job Analysis":
    mode = settings.get('mode', 'one')
    execution_order = {}
    stage_list = []
    with open('../../job.json') as job_json:
        json_data = json.load(job_json)
    if mode == 'one':
        nstage = 1
    else:
        nstage = int(len(json_data['stages']))
    before = collections.deque(maxlen=nstage)
    for key in json_data['stages']:
        if 'Update HWDB' or 'Notify' not in key:
            execution_order[json_data['stages'][key]['order']] = key
        else:
            continue
    for value in execution_order.values():
        if value[10:30] != pstage[10:30]:
            before.append(value)
        else:
            continue
    for stage in list(before):
        stage_list.append(convert_stage_to_folder_name(stage))
    stage_list.insert(0, 'auto')
    launcher(stage_list, patterns, cirrusid, adj_lines, stage_name)
os.popen('rm -rf /ci/data/autotest/tmp/ftp/*')
