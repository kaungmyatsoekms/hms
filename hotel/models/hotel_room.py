# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression

class HotelRoomType(models.Model):
    _name = 'hotel.roomtype'
    _description = 'hotel.roomtype'

    roomtype_code = fields.Char(string="Code", required=True)
    roomtype_name = fields.Char(string="Name", required=True)
    roomtype_rate = fields.Integer(string="Rate", required=True)
    roomtype_bedqty = fields.Integer(string="Number of Bed", required=True)
    roomtype_totalroom = fields.Integer(string="Total Room")
    roomtype_description = fields.Char(string="Description",required=True)
    roomtype_image = fields.Binary(string="Image")

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'hotel.room'
    # _rec_name = 'roomview_name'

    room_no = fields.Char(string="Room No",required=True)
    roomtypemap_code = fields.Char()
    roomview_id = fields.Many2one('hotel.roomview','Room View')
    roommap_code = fields.Char()
    room_bedtype = fields.Many2one('hotel.bedtype','Bed Type')
    room_ratecode = fields.Char()
    room_facilitycode = fields.Char()
    room_size = fields.Char()
    room_extension = fields.Char()
    room_image = fields.Binary()
    room_description = fields.Char()

class HotelRoomView(models.Model):
    _name='hotel.roomview'
    _description = 'hotel.roomview'
    _rec_name = 'roomview_name'

    roomview_code = fields.Char(required=True)
    roomview_name = fields.Char()
    roomview_description = fields.Char()

class HotelBedType(models.Model):
    _name = 'hotel.bedtype'
    _description = 'hotel.bedtype'
    _rec_name = 'bedtype_name'
    
    bedtype_code = fields.Char()
    bedtype_name = fields.Char(required=True)
    bed_size = fields.Char()

# class HotelRoomAmenitiesType(models.Model):
#     _name = 'hotel.room.amenities.type'
#     _description = 'amenities type'

#     name = fields.Char('Name', size=64, required=True)
#     amenity_id = fields.Many2one('hotel.room.amenities.type','Category')
#     child_id = fields.One2many('hotel.room.amenities.type', 'amenity_id', 'Child Category')

#     @api.multi
#     def name_get(self):
#             def get_names(cat):

#                 res = []
#                 while cat:
#                     res.append(cat.name)
#                     cat = cat.amenity_id
#                     return res
#                 return [(cat.id," / ".join(reversed(get_names(cat)))) for cat in self]

#     @api.model
#     def name_search(self, name, args=None, operator='ilike', limit=100):
#         if not args:
#             args = []
#         if name:
#             # Be sure name_search is symetric to name_get
#             category_names = name.split(' / ')
#             parents = list(category_names)
#             child = parents.pop()
#             domain = [('name', operator, child)]
#             if parents:
#                 names_ids = self.name_search( ' / '.join(parents), args=args,
#                                             operator='ilike', limit=limit)
#                 category_ids = [name_id[o] for name_id in names_ids]

#                 if operator in expression.NEGATIVE_TERM_OPERATORS:
#                     categories = self.search([('id', 'not in', category_ids)])
#                     domain = expression.OR([[('amenity_id', 'in', 
#                                                 categories.ids)], domain])
#                 else:
#                     domain = exprission.AND([[('categ_id', 'in',
#                                                  category_ids)], domain])
#                 for i in range(1, len(category_names)):
#                     domain = [[('name', operator,
#                                 ' / '.join(category_names[-1 - i:]))], domain]
#                     if operator in expression.NEGATIVE_TERM_OPERATORS:
#                         domain = expression.AND(domain)
#                     else:
#                         domain = expression.OR(domain)
#             categories = self.search(expression.AND([domain, args]),
#                                     limit=limit)
#         else:
#             categories = self.search(args, limit=limit)
#         return categories.name_get()            

