# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hotel(models.Model):
    _name = 'hotel.hotel'
    _description = 'hotel.hotel'

    name = fields.Char()
    value = fields.Integer()

class HotelFloor(models.Model):
    _name = 'hotel.floor'
    _description = 'hotel.floor'

    name = fields.Char()
    floor_number = fields.Char()
    no_of_room = fields.Char()
    building_id = fields.Char()

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# class Property(models.Model):
#     _name = 'property.property'
#     _description = 'property property'

#     property_code = fields.Char()
#     property_name = fields.Char()
#     address1 = fields.Char()
#     address2 = fields.Char()
#     address3 = fields.Char()
#     country_id = fields.Char()
#     state_id = fields.char()
#     city_id = fields.Char()
#     telephone = fields.Char()
#     fax = fields.Char()
#     email = fields.Char()
#     website = fields.Char()
#     social_media_links = fields.Char()
#     no_of_room = fields.Integer(size=4)
#     proprety_license = fields.Char()
#     property_rating = fields.Char()
#     property_logo = fields.binary()
#     property_photo = fields.binary()