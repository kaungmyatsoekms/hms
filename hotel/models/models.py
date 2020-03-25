# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class Property(models.Model):
    _name = 'property.property'
    _description = 'property.property'

    name = fields.Char(string='Hotel Name', required=True)
    code = fields.Char(string='Hotel Code', required=True)
    address1 = fields.Char(string='Address', required=True)
    address2 = fields.Char(string='Address2', required=True)
    address3 = fields.Char(string='Address3', required=True)
    city_id = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', 'State', domain="[('country_id', '=', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', required=True)
    zip = fields.Char(string='Zip', change_default=True)
    phone = fields.Char(string='Phone')
    fax = fields.Char(string='Fax')
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')
    sociallink = fields.Char(string='Social Media Link')
    no_of_room = fields.Integer(string='Total Rooms')
    property_license = fields.Char()
    property_rating = fields.Selection(
        [('one','*'),
         ('two','**'),
         ('three','***'),
         ('four','****'),
         ('five','*****'),
        ]
    )
    note = fields.Text()
    property_logo = fields.Binary(string='Logo')
    property_image = fields.Binary(string='Image')
    # is_group = fields.Boolean(string="Is a Group", default=False,
    #     help="Check if the contact is a group, otherwise it is a hotel")
    # user_type = fields.Selection(string='User Type',
    #     selection=[('hotel','Hotel'),('group','Group')],
    #     compute='-compute_user_type')inverse='_write_user_type'

class HotelBuilding(models.Model):
    _name = 'hotel.building'
    _description = 'hotel.building'

    building_code = fields.Char(string="Building Code", required=True)
    building_name = fields.Char(string="Building Name", required=True)
    building_type = fields.Char(string="Building Type", required=True)
    building_location = fields.Char(string="Location", required=True)
    building_description = fields.Char( string="Description", required=True)
    