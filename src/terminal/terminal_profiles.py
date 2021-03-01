import logging

import sys 
import os

sys.path.append("../.")

import git

from tasks import setup_tasks

class DarwinTerminalProfile(setup_tasks.DarwinTaskABC):

    def __init__(self, work_dir):
        super().__init__(work_dir)
        self.GITHUB_URL = "https://github.com/lysyi3m/macos-terminal-themes.git"

    def __install_profiles(self):

        '''
        TODO
        This function will check to make sure the GitHub download contains some files and then installs these profiles
        into MacOS terminal.
        '''
        pass

    def __clone_repo(self):
        
        '''
        This function will clone the Terminal Profiles git repo from GitHub so we can install them
        to the terminal later...
        '''
        git.Repo.clone_from(self.GITHUB_URL, self._working_directory)

    def __setup_terminal_profiles(self):

        response = {}

        try:
            
            self.__clone_repo()
        
        except Exception:
            
            # TODO replace exception with git related exception...
            response['message'] = 'FAILED'
            response['details'] = 'An exception occured.'
            
            logging.error(f'Unable to fetch terminal profiles: { Exception }')
            return response
    
        try:

            self.__install_profiles()
        
        except Exception:
            
            # TODO replace exception with git related exception...
            response['message'] = 'FAILED'
            response['details'] = 'An exception occured.'
            
            logging.error(f'Unable to install terminal profiles: { Exception }')
            return response
    
        response['message'] =  'SUCCESS'
        return response
        
    def do(self) -> {}:
        return self.__setup_terminal_profiles()