import requests, argparse

# sort experiments in reverse chronological order
def reverse_sort():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_id", help="paste the project ID as the first argument")
    parser.add_argument("token", help="paste your Optimizely v2 REST API token as the second argument")
    args = parser.parse_args()
    project_id = args.project_id
    token = args.token

    experiment_list = requests.get("https://api.optimizely.com/v2/experiments?project_id=%s" % project_id, headers={'Authorization': 'Bearer %s' % token})

    if experiment_list.status_code == 200:
        experiments_json = experiment_list.json()
        sorted_experiments = sorted(experiments_json, key=lambda k: k['id'], reverse=True)
        for exp in sorted_experiments:
            print(exp['name'], exp['id'])

reverse_sort()
