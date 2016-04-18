#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
'equip' related mix-ins for high-level interface.
"""

import hszinc

class EquipMixin(object):
    """
    A mix-in used for entities that carry the 'equip' marker tag.
    """

    def get_site(self, callback=None):
        """
        Retrieve an instance of the site this 'equip' entity belongs to.
        """
        return self._session.get_entity([self.tags['siteRef'].name],
                callback=callback)

    def find_entity(self, filter_expr=None, limit=None, callback=None):
        """
        Retrieve the entities that are linked to this equip.
        This is a convenience around the session find_entity method.
        """
        equip_ref = hszinc.dump_scalar(self.id)
        if filter_expr is None:
            filter_expr = 'equipRef==%s' % equip_ref
        else:
            filter_expr = '(equipRef==%s) and (%s)' % (equip_ref, filter_expr)
        return self._session.find_entity(filter_expr, limit, callback)
