from parameter import Parameter


class Database:
    def __init__(self):
        self.parameters = {}
        self._last_parameter_key = 0

    def add_parameter(self, parameter):
        self._last_parameter_key += 1
        self.parameters[self._last_parameter_key] = parameter
        return self._last_parameter_key

    def delete_parameter(self, parameter_key):
        if parameter_key in self.parameters:
            del self.parameters[parameter_key]

    def get_parameter(self, parameter_key):
        parameter = self.parameters.get(parameter_key)
        if parameter is None:
            return None
        parameter_ = Parameter(parameter.frequency, parameter.power)
        return parameter_

    def get_parameters(self):
        parameters = []
        for parameter_key, parameter in self.parameters.items():
            parameter_ = Parameter(parameter.frequency, parameter.power)
            parameters.append((parameter_key, parameter_))
        return parameters


