# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Area_construida
                                 A QGIS plugin
 Filtra imóveis segundo parametros de área construida
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-04-21
        copyright            : (C) 2025 by Mauro Alixandrini
        email                : mauro.alixandrini@ufba.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Area_construida class from file Area_construida.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .area_construida import Area_construida
    return Area_construida(iface)
