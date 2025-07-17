from odoo import models, fields


class Types(models.Model):

    _name = "travel.vehicle.types"
    _description = "Vehicle Types"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Name",
        copy=True,
        required=True
    )

    color = fields.Char(
        string="Color",
        help="This field uses the 2nd color widget",
        copy=True,
        default="#FFFFFF"
    )

    description = fields.Text(
        string="Description",
        copy=True
    )
