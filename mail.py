# -*- coding: utf-8 -*-

from openerp import models, api
import logging

_logger = logging.getLogger(__name__)

class publisher_warranty_contract(models.Model):
    
    _inherit = 'publisher_warranty.contract'

    @api.one
    def update_notification(self, cron_mode=True):

        _logger.info("No more notifications stuff")

        return True
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
