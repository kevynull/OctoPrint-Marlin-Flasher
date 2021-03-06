import flask
from .base_validator import BaseValidator
from .validators import unsupported


class UnsupportedPlatformValidator(BaseValidator):

	def __init__(self, settings):
		BaseValidator.__init__(self, settings)
		self.__schema = unsupported.UnsupportedSchema()

	def validate_upload(self):
		return self.__schema.validate(flask.request.values)

	def validate_firmware(self):
		return self.__schema.validate(flask.request.values)

	def validate_core_search(self):
		return self.__schema.validate(flask.request.values)

	def validate_lib_search(self):
		return self.__schema.validate(flask.request.values)

	def validate_core_install(self):
		return self.__schema.validate(flask.request.values)

	def validate_lib_install(self):
		return self.__schema.validate(flask.request.values)

	def validate_core_uninstall(self):
		return self.__schema.validate(flask.request.values)

	def validate_lib_uninstall(self):
		return self.__schema.validate(flask.request.values)

	def validate_board_listall(self):
		return self.__schema.validate(flask.request.values)

	def validate_board_details(self):
		return self.__schema.validate(flask.request.values)

	def validate_flash(self):
		return self.__schema.validate(flask.request.values)

	def validate_last_flash_options(self):
		return self.__schema.validate(flask.request.values)
