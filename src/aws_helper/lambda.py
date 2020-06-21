# python

import awacs
from troposphere.constants import NUMBER
from troposphere import Template, Parameter, Ref, Join
from troposphere.awslambda import Function, Code, MEMORY_VALUES

from troposphere-helper import InvalidRuntimeError


class Lambda(object):

    def __init__(self):
        self.t = Template()
        self.Timeout = None
        self.Memory = None

    def create(self, id, handler, runtime, memory_size, code, timeout):
        self.t = Template()
        self.t.set_version('2010-09-09')
        self.add_resource(Function(
            id,
            Handler=handler,
            Runtime=runtime,
            Code=Code(
                ZipFile=Join("", code)
            ),
            Timeout=Ref(timeout is not None or self.get_timeout is not None)
        ))

    def set_memory_size(self):
        self.Memory = self.t.add_parameter(
            'LambdaMemorySize',
            Type=NUMBER,
            Description='Amount of memory allocated to this Lambda function',
            Default='128',
            AllowedValues=MEMORY_VALUES
        )

    def set_timeout(self):
        self.t

    def get_timeout(self):
        return

    def set_lambda_execution_role(self):
        self.t

    class Runtime(object):
        RUNTIMES = [
            ''
        ]

        def validate(self, runtime):
            for r in self.RUNTIMES:
                if r == runtime:
                    return r
                else:
                    raise Exception
