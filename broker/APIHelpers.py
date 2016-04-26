
class RPCParameterHelper(object):
    # a helper function
    # receives a string with parameters and returns an array with the two parameters required
    @staticmethod
    def splitParameters(parameterString):
        return str.split(parameterString, "&")