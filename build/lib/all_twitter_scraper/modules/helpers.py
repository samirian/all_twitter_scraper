from .constants import *


class User_Agent_Rotator:
	def __init__(self):
		self.__index = 0

	def get_user_agent(self):
		user_agent = USER_AGENTS[self.__index]
		self.__index = (self.__index + 1) % len(USER_AGENTS)
		return user_agent
