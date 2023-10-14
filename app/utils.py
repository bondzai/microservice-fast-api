import time

class Utils:

    def __init__(self) -> None:
        pass

    def performance_monitor(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Function '{func.__name__}' took {elapsed_time:.6f} seconds to execute.")
            return result

        return wrapper

    def custom_filters(self, input_data, search_keyword):
        result = []
        search_columns = ["a", "b"]

        for project in input_data:
            for key, value in project.items():
                if key in search_columns:
                    if search_keyword.lower() in str(value).lower():
                        result.append(project)
                        break

        return result
