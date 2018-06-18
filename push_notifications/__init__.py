import pkg_resources


__version__ = pkg_resources.require("django-push-notifications_rubgomez93")[0].version


class NotificationError(Exception):
	pass
