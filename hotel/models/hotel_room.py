# -*- coding: utf-8 -*-

from odoo import models, fields, api

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