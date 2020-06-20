# python

import awacs
from troposphere import Template, Parameter


class Lambda(object):

    def __init__(self):
        self.t = Template()

    @staticmethod
    def create_lambda(self, handler, runtime, memory_size, timeout):
        self.t = Template()
        self.t.set_version("2010-09-09")

    def add_memory(self):
        self.t

    def set_timeout(self):
        self.t

    def lambda_execution_role(self):
        self.t

