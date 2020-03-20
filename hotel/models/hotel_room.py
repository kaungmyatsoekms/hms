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

    class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'hotel.room'

    room_no = fields.Char()
    roomtypemap_code = fields.Char()
    roomview_code = fields.Char()
    roommap_code = fields.Char()
    room_bedtype = fields.Char()
    room_ratecode = fields.Char()
    room_facilitycode = fields.Char()
    room_size = fields.Char()
    room_extension = fields.Char()
    room_image = fields.Binary()
    room_description = fields.Char()