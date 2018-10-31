from abc import ABC, abstractmethod
from command import Command

class UploadingCommand(Command):


    def __init__(self, template_name):
        '''
        (UploadingCommand, str) -> None

        Initializes an uploading command, and injects a specific template
        name to the uploading command
        '''
        Command.__init__(self)
        self._template_name = template_name

class SampleCommand(UploadingCommand):

    def __init__(self, template_name):
        '''
        (TestCommand, str) -> None

        Initializes a test command, and injects a specific template name to
        the test command
        '''
        UploadingCommand.__init__(self, template_name)


    def execute(self):
        '''
        (Command) -> Abstract

        Executes the command
        '''
        print("Hello")


    def executed_properly(self):
        '''
        (Command) -> boolean

        Returns a boolean to determine if this command was executed properly
        '''
        return self._exec_status


if __name__ == "__main__":
    some_command = SampleCommand('template name')
    # get the private template name
    print(some_command._template_name)
    # check not execution status
    print(some_command._exec_status)
    # get the execution
    some_command.execute()
    # set the execution status
    some_command._exec_status = True
    # get the execution status
    print(some_command._exec_status)
