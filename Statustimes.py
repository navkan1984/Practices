#!/usr/bin/python
import os
import subprocess
from operator import itemgetter
import json
import datetime
import fnmatch
from operator import itemgetter

payload = []
queue = '/Users/nakanumu/Documents/queue.properties'
RUPLITE_FLO = '/Users/nakanumu/Documents/u01/APPLTOP/instance/lcm/logs/rupliteflo/'
HLO_DIR = '/Users/nakanumu/Documents/u01/APPLTOP/instance/lcm/logs/hlo/'
ORCH_DIR = '/Users/nakanumu/Documents/u01/APPLTOP/instance/lcm/logs/orchestration/'


def run_command(command):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    result = proc.stdout.read().strip()
    return result


def path_builder(*args):
    return os.path.join(*args)


def tuple_to_datetime(t):
    return datetime.datetime(t[0], t[1], t[2], t[3], t[4], t[5]).strftime("%Y-%m-%dT%H:%M:%S")


def time_taken(start_time, end_time):
    starttime = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
    endtime = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S")
    total_time = endtime - starttime
    return total_time.days * 86400 + total_time.seconds


def format_time(time_in_seconds):
    minutes, sec = divmod(time_in_seconds, 60)
    hr, minutes = divmod(minutes, 60)
    day, hr = divmod(hr, 24)
    return "%02dd:%02dh:%02dm:%02ds" % (day, hr, minutes, sec)


def format_time2(tuple_value):
    return '%02d%02d%02d%02d%02d%02d' % tuple_value


def read_file(filename):
    with open(filename, 'r') as f:
        output = f.read()
    return output



class Schedule(object):

    def __init__(self):
        self.start_time = None
        self.queue = []
        self.metadata = {}
        self.queue_timings = None


class Queue(object):

    def __init__(self):
        self.task_status = None
        self.task_name = None
        self.attempt = None
        self.totalexecinsecs = None
        self.starttime = None
        self.endtime = None
        self.retries = None
        self.total_time = None
        self.total_idle_time = None


def get_update_queue_details(source_queue_loc):

    schedule = Schedule()
    source_content = run_command('cat ' + source_queue_loc)
    schedule.queue_timings = eval(source_content.splitlines()[0].split('=')[1])
    schedule.start_time = schedule.queue_timings[0]
    source_queues = eval(source_content.splitlines()[1].split('=')[1])
    source_metadata_output = eval(source_content.splitlines()[2].split('=')[1])
    for source_queue in source_queues:
        if source_queue[0][0] == schedule.start_time:
            schedule.queue = source_queue[-1]
    schedule.metadata = source_metadata_output[schedule.queue_timings]

    return schedule


def get_flo_plugins(e2e_task):

    hostwise_flo = {}
    flo_timelines = []
    patterns = ['flo.plugin.In*.log', 'flo.plugin.RUP*.log', 'flo.plugin.P*.log']
    flo_folder = path_builder(RUPLITE_FLO, e2e_task)
    if os.path.isdir(flo_folder):
        os.chdir(flo_folder)
        host_dirs = next(os.walk('.'))[1]
        for host in host_dirs:
            current_directory = path_builder(flo_folder, host)
            for flo_file in os.listdir(current_directory):
                for pattern in patterns:
                    if fnmatch.fnmatch(flo_file, pattern):
                        if hostwise_flo.get(host) is None:
                            hostwise_flo.update({host: [path_builder(current_directory, flo_file)]})
                        else:
                            hostwise_flo[host].append(path_builder(current_directory, flo_file))

    for keys, values in hostwise_flo.iteritems():
        values = sorted(values)
        failure_timeline = []
        if len(values) > 1:
            for index, value in enumerate(values):
                timeline = {}
                flo_log = read_file(value)
                flo_output = flo_log.splitlines()
                first_line = flo_output[0].split()[0].strip('[').strip(']').split('.')[0]
                second_line = flo_output[-1].split()[0].strip('[').strip(']').split('.')[0]
                timeline['action_start_time'] = first_line
                timeline['action_end_time'] = second_line
                if index == len(values) - 1:
                    timeline['status'] = 'DONE'
                else:
                    timeline['status'] = 'FAILED'
                timeline['host_name'] = keys
                failure_timeline.append(timeline)

            for index, i in enumerate(failure_timeline):
                if i['status'] == 'FAILED':
                    idle = {}
                    idle_start_time = i['action_end_time']
                    idle_end_time = failure_timeline[index+1]['action_start_time']
                    idle['action_start_time'] = idle_start_time
                    idle['action_end_time'] = idle_end_time
                    idle['status'] = 'IDLE'
                    idle['host_name'] = i['host_name']
                    failure_timeline.append(idle)
            [[failure_timeline = sorted(failure_timeline, key=itemgetter('action_start_time'))]]
            flo_timelines.append(failure_timeline)
        else:
            for value in values:
                timeline = {}
                flo_log = read_file(value)
                flo_output = flo_log.splitlines()
                first_line = flo_output[0].split()[0].strip('[').strip(']').split('.')[0]
                second_line = flo_output[-1].split()[0].strip('[').strip(']').split('.')[0]
                timeline['action_start_time'] = first_line
                timeline['action_end_time'] = second_line
                timeline['status'] = 'DONE'
                timeline['host_name'] = keys
                failure_timeline.append(timeline)
                flo_timelines.append(failure_timeline)

    return flo_timelines


def parse_queue(queue):
    current_schedule = get_update_queue_details(queue)
    q = Queue()
    total_time = []
    start_time = tuple_to_datetime(current_schedule.queue_timings[0])
    pre_e2e_start_time = format_time2(current_schedule.queue_timings[0])
    for tasks in current_schedule.queue:
        pre_e2e_task_details = {}
        e2e_task_details = {}
        q.task_name = tasks[0]
        q.task_status = tasks[-1]
        q.attempt = current_schedule.metadata[q.task_name]['attempt']
        q.retries = 0 if q.attempt == 1 else int(q.attempt - 1)
        f_starttime = tuple_to_datetime(current_schedule.metadata[q.task_name]['starttime'])
        q.starttime = format_time2(current_schedule.metadata[q.task_name]['starttime'])
        if 'endtime' in current_schedule.metadata[q.task_name]:
            f_endtime = tuple_to_datetime(current_schedule.metadata[q.task_name]['endtime'])
            q.endtime = format_time2(current_schedule.metadata[q.task_name]['endtime'])
            f_totalexecinsecs = format_time(time_taken(f_starttime, f_endtime))
            q.total_time = time_taken(f_starttime, f_endtime)
            q.totalexecinsecs = current_schedule.metadata[q.task_name]['totalexecinsecs']
            q.total_idle_time = q.total_time - int(q.totalexecinsecs)
        else:
            sys.exit(0)
        if 'SETCTXT' in q.task_name and not any(d.get('name') == "PRE E2E START" for d in payload):
            initial_buffer_time = time_taken(start_time, f_starttime)
            total_time.append(initial_buffer_time)
            pre_e2e_task_details['name'] = "PRE E2E START"
            pre_e2e_task_details['status'] = "DONE"
            pre_e2e_task_details["total_time"] = initial_buffer_time
            pre_e2e_task_details["start_time"] = pre_e2e_start_time
            pre_e2e_task_details["total_exec_time"] = 0
            pre_e2e_task_details["elapsed_time"] = initial_buffer_time
            pre_e2e_task_details["end_time"] = q.starttime
            pre_e2e_task_details["flo_plugin_timelines"] = []
            pre_e2e_task_details["reattempts"] = 0
            pre_e2e_task_details["total_idle_time"] = initial_buffer_time
            payload.append(pre_e2e_task_details)
        total_time.append(current_schedule.metadata[q.task_name]['totalexecinsecs'])
        elapsed_time = time_taken(start_time, f_endtime)
        e2e_task_details['name'] = q.task_name
        e2e_task_details['start_time'] = q.starttime
        e2e_task_details['end_time'] = q.endtime
        e2e_task_details['total_time'] = q.total_time
        e2e_task_details['total_idle_time'] = q.total_idle_time
        e2e_task_details['reattempts'] = q.retries
        e2e_task_details['total_exec_time'] = q.totalexecinsecs
        e2e_task_details['status'] = q.task_status
        e2e_task_details['elapsed_time'] = elapsed_time
        current_flo_plugins = get_flo_plugins(q.task_name)
        print current_flo_plugins
        e2e_task_details['flo_plugin_timelines'] = current_flo_plugins
        payload.append(e2e_task_details)
    json_data = json.dumps(payload, default=lambda o: o.__dict__, indent=4)
    with open("/Users/nakanumu/Documents/FJA/timeline.json", "w") as f:
        f.write(json_data)


parse_queue(queue)