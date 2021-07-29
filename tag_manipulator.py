# "python, java" ["python","java"]

def TagManipulator(input):

    return [x.lstrip().rstrip() for x in input.split(",")]


print(TagManipulator("asdf,bsdf, a b c "))
