from odoo import models, fields


class Flights(models.Model):

    _name = "travel.flight"
    _description = "Flight"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Flight No.",
        copy=True,
        required=True
    )

    destination = fields.Char(
        string="Destination",
        copy=True,
        required=True
    )

    distance = fields.Float(
        string="Distance",
        copy=True
    )

    cost = fields.Float(
        string="Cost",
        copy=True
    )
