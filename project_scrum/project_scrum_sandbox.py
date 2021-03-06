# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.tools.translate import _

class projectScrumSandbox(osv.osv):
    _name = 'project.scrum.sandbox'
    
    _columns = {
        'role_id': fields.many2one('project.scrum.role', "As", required=True),
        'name' : fields.char('I want', size=128, required=True),
        'for_then' : fields.char('For', size=128, required=True),
        'project_id': fields.many2one('project.project', "Project", required=True, domain=[('is_scrum', '=', True)]),
        'developer_id': fields.many2one('res.users', 'Developer'),
    }
    
    _defaults = {
        'developer_id': lambda self, cr, uid, context: uid,
    }
