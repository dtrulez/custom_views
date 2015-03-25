# -*- coding: utf-8 -*-

{
    'name': 'Customized Views',
    'version': '1.0',
    'category': 'Notification',
    "sequence": 1,
    'complexity': "easy",
    'summary': 'Removing phoning features from Odoo, and some other customized views',
    'description': """
        This module will by pass the phoning features of odoo.
    """,
    'author': 'YJ',
    'website': 'http://myodoo.space',
    'depends': ["mail","web"],
    'init_xml': [],
    'data': ['webclient_templates.xml'],
    'qweb' : [
	"static/src/xml/announcement.xml"
    ],
    'installable': True,
    #'auto_install': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
