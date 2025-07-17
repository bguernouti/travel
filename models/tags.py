from odoo import models, fields


class Tags(models.Model):

    """
    <record model="ir.model" id="travel.xml_id">
      <field name="name">travel.vehicle.tags</field>
      <field name="description">Vehicle Tags</field>
    </record>
    """

    # name = travel.vehicle.tags IT WILL BE => travel.model_travel_vehicle_tags
    _name = "travel.vehicle.tags"
    _description = "Vehicle Tags"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Name",
        copy=True,
        required=True
    )

    color = fields.Integer(
        string="Color",
        help="This field uses the color widget",
        copy=True,
        default=1
    )
