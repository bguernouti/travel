from odoo import models, fields


class Ticket(models.Model):

    _name = "travel.ticket"
    _description = "Travel ticket"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Ticket No",
        copy=True,
        required=True
    )

    travel_id = fields.Many2one(
        comodel_name="travel.travel",
        ondelete="restrict",
        string="Related travel",
        copy=True,
        required=True
    )

    passenger_id = fields.Many2one(
        comodel_name="travel.passenger",
        ondelete="restrict",
        string="Passenger",
        copy=True,
        required=True
    )

    seat_no = fields.Integer(
        string="Seat No",
        copy=True,
        required=True
    )

    price = fields.Float(
        string="Price",
        copy=True
    )

    travel_destination = fields.Char(string="Destination", related="travel_id.flight_destination")
    travel_state = fields.Selection(string="Travel State", related="travel_id.state")
