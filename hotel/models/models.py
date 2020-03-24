# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class Property(models.Model):
    _name = 'property.property'
    _description = 'property.property'

    name = fields.Char(string='Hotel Name', required=True)
    code = fields.Char(string='Hotel Code', required=True)
    address1 = fields.Char(string='Address1', required=True)
    address2 = fields.Char(string='Address2', required=True)
    address3 = fields.Char(string='Address3', required=True)
    city_id = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', 'State', domain="[('country_id', '=', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', required=True)
    phone = fields.Char(string='Phone')
    fax = fields.Char(string='Fax')
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')
    sociallink = fields.Char(string='Social Media Link')
    no_of_room = fields.Integer(string='Total Number of Rooms')
    property_license = fields.Char(string='Property License')
    property_rating = fields.Selection(
        [('one','One Star'),
         ('two','Two Star;'),
         ('three','Three Star'),
         ('four','Four Star'),
         ('five','Five Star'),
        ]
    )
    property_logo = fields.Binary(string='Logo')
    property_image = fields.Binary(string='Image')

class HotelBuilding(models.Model):
    _name = 'hotel.building'
    _description = 'hotel.building'

    building_code = fields.Char(string="Building Code", required=True)
    building_name = fields.Char(string="Building Name", required=True)
    building_type = fields.Char(string="Building Type", required=True)
    building_location = fields.Char(string="Location", required=True)
    building_description = fields.Char( string="Description", required=True)
    