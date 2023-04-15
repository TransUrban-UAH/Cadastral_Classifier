# -*- coding: utf-8 -*-
"""
 This script initializes the plugin, making it known to QGIS.
"""

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load cadastral_classifier class from file cadastral_classifier.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .cadastral_classifier import cadastral_classifier
    return cadastral_classifier(iface)
