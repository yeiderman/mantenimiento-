# -*- coding: utf-8 -*-
{
    'name': "Mantenimiento Personalizado",
    'summary': """
        Gestión de mantenimiento de equipos en Odoo.""",
    'description': """
        Este módulo extiende las funcionalidades de mantenimiento de Odoo
        para adaptarse a necesidades específicas de la empresa.
    """,
    'author': "Tu Nombre/Empresa",
    'website': "https://www.tu_sitio_web.com",
    'category': 'Industria',
    'version': '1.0',
    'depends': ['base', 'maintenance'], # Dependencias: 'base' es siempre necesaria, 'maintenance' para extender el módulo existente.
    'data': [
        'security/ir.model.access.csv', # Para definir permisos de seguridad
        'views/mantenimiento_views.xml', # Vistas de la interfaz de usuario
       # 'views/menu.xml', # Menús de la aplicación
        'data/data_demo.xml', # Datos de demostración
    ],
    'demo': [
        # 'demo/demo.xml', # Datos de demostración
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}