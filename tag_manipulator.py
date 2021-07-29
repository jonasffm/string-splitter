# "python, java" ["python","java"]

class TagManipulator:
    def parse_string(self, input):
        return [x.lstrip().rstrip() for x in input.split(",") if not x.strip() == ""]
