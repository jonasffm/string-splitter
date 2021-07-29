# "python, java" ["python","java"]

class TagManipulator:
    def parse_string(self, input):
        return [x.lstrip().rstrip() for x in input.split(",")]


#print(TagManipulator.parse_string("asdf,bsdf, a b c "))
