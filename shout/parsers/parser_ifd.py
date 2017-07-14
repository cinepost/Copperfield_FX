from pyparsing import Word, alphas
from parser_base import ParserBase


class ParserIFD(ParserBase):

	exit_token = 'ray_quit'
	command = Word( 'ray_' + alphas )

	def __init__(self):
		super(ParserIFD, self).__init__()