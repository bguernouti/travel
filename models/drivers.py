from odoo import models, fields

class Drivers(models.Model):

    _name = "travel.vehicle.drivers"
    _description = "Vehicle driver"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Name",
        copy=True,
        required=True
    )

    image = fields.Image(
        string="Image",
        copy=False
    )

    license_number = fields.Char(
        string="Driver license number",
        copy=False,
        required=True
    )

    email = fields.Char(
        string="Driver email",
        copy=False,
        required=True
    )

    hire_date = fields.Date(
        string="Hire date",
        copy=True,
        required=True
    )
