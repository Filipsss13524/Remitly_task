import pandas as pd
import json


def resource_checker_function(resource_path: str) -> bool:
    """
    Method shall return logical false if an input JSON Resource field contains a single asterisk
    and true in any other case
    :param resource_path: AWS::IAM::Role Policy
    :return:
    """
    try:
        with open(resource_path, 'r') as file:
            data = json.load(file)

            for statement in data["PolicyDocument"]["Statement"]:
                resource = statement["Resource"][0]
                if resource == '*':
                    return False
            else:
                return True

    except FileNotFoundError:
        print("Error in file name in path")
        return True
    except ValueError:
        print("Error - the file is not in json format")
        return True
    except KeyError:
        print("One of the json keys has the wrong name")
        return True


def resource_checker_pandas(resource_path: str) -> bool:
    """
    Method shall return logical false if an input JSON Resource field contains a single asterisk
    and true in any other case using library Pandas DataFrame
    :param resource_path: AWS::IAM::Role Policy
    :return:
    """
    try:
        data = pd.read_json(resource_path)
        data_v1 = pd.json_normalize(data["PolicyDocument"]["Statement"])
        data_v2 = list(data_v1["Resource"][0])
        if any([x == '*' for x in data_v2]):
            return False
        else:
            return True
    except FileNotFoundError:
        print("Error in file name in path")
        return True
    except ValueError:
        print("Error - the file is not in json format")
        return True
    except KeyError:
        print("One of the json keys has the wrong name")
        return True


if __name__ == "__main__":
    path = 'date_v2.json'
    print(resource_checker_function(path))
    print(resource_checker_pandas(path))
