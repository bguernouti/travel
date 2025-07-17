from odoo import models, fields


class Passenger(models.Model):

    _name = "travel.passenger"
    _description = "Travel Passenger"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Name",
        copy=True,
        required=True
    )

    national_id = fields.Char(
        string="National ID",
        copy=True,
        required=True
    )

    phone = fields.Char(
        string="Passenger phone",
        copy=True,
        required=True
    )
