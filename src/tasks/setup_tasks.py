from abc import ABC, abstractmethod

import platform
import logging

import shutil

import os
from os import path


class WrongPlatformException(Exception):
    pass


class DirectoryAlreadyExistsException(Exception):
    pass


class TaskABC(ABC):

    '''
    This is an abstract class to define the makeup of a task.
    '''

    @abstractmethod
    def __init__(self, work_dir):

        '''
        The constructor takes a working directory in as a parameter.
        This provides a location where we can download & manipulate any files, programs etc.
        '''

        self._PLATFORM = ""

        if work_dir is not "":
            self._working_directory = work_dir
        else:
            self._working_directory = "/setup"

    def __check_platform(self, target_os):

        '''
        This function will throw an exception if the target platform is not valid.
        '''

        if self._PLATFORM != target_os :
            raise WrongPlatformException(f'This task supports: { self._PLATFORM }, the target OS is: { target_os }')


    def __check_working_directory(self):

        '''
        This function will see if the working directory exists.  If it doesn't, it will create one.
        '''

        if not path.exists(self._working_directory):
            os.mkdir(self._working_directory)
            logging.info(f'Creating working directory: { self._working_directory }')
        else:
            logging.fatal(f'Working directory { self._working_directory } already exists!  Unable to continue with confidence...')
            raise DirectoryAlreadyExistsException(f'Please delete working directory: { self._working_directory }')

    def do(self) -> {}:

        '''
        This function should check whether or not we are running on the correct target platform.
        '''

        self.__check_platform(platform.system())
        self.__check_working_directory()


class LinuxTaskABC(TaskABC):

    '''
    This abstract class will be the case class for all Linux-specific logic.
    '''

    def __init__(self, work_dir):
        super().__init__(work_dir)
        self._PLATFORM = "Linux"

    @abstractmethod
    def do(self) -> {}:
        return super().do()


class DarwinTaskABC(TaskABC):

    '''
    This abstract class will be the case class for all MacOS-specific logic.
    '''

    def __init__(self, work_dir):
        super().__init__(work_dir)
        self._PLATFORM = "Darwin"

    @abstractmethod
    def do(self) -> {}:
        return super().do()