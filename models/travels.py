from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Travels(models.Model):

    _name = "travel.travel"
    _description = "Travel"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Travel No.",
        copy=False,
        required=True
    )

    flight_id = fields.Many2one(
        comodel_name="travel.flight",
        ondelete="restrict",
        string="Related flight",
        copy=True,
        required=True
    )

    scheduled_start = fields.Date(
        string="Scheduled start",
        copy=True,
        required=True
    )

    deadline_start = fields.Date(
        string="Deadline start",
        help="The deadline to start the travel",
        copy=True
    )

    scheduled_end = fields.Date(
        string="Scheduled end",
        copy=True,
        required=True
    )

    deadline_end = fields.Date(
        string="Deadline end",
        help="Deadline to complete the travel",
        copy=True,
        required=True
    )

    first_driver_id = fields.Many2one(
        comodel_name="travel.vehicle.drivers",
        ondelete="restrict",
        string="First driver",
        copy=True,
        required=True
    )

    second_driver_id = fields.Many2one(
        comodel_name="travel.vehicle.drivers",
        ondelete="restrict",
        string="Second driver",
        copy=True,
        required=True
    )

    vehicle_id = fields.Many2one(
        comodel_name="travel.vehicle",
        ondelete="restrict",
        string="Vehicle",
        domain=[('state', '!=', 'fail_repair')],
        copy=True,
        required=True
    )

    started_at = fields.Datetime(
        string="Started date",
        copy=True
    )

    ended_at = fields.Datetime(
        string="Ended date",
        copy=True
    )

    ticket_ids = fields.One2many(
        comodel_name="travel.ticket",
        inverse_name="travel_id",
        string="Tickets",
        copy=True
    )

    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("scheduled", "Scheduled"),
            ("running", "Running"),
            ("end", "Terminated"),
            ("cancel", "Cancel")
        ],
        string="State",
        copy=True,
        default="draft"
    )

    flight_destination = fields.Char(string="Flight Destination", related="flight_id.destination")

    @api.model_create_multi
    def create(self, vals_list):
        for rec in vals_list:
            rec['name'] = self.env['ir.sequence'].next_by_code('travel.travel')
        return super(Travels, self).create(vals_list)

    def schedule_travel(self):
        """
        This method responsible for scheduling the travel
        """

        if len(self.ticket_ids) < 2:
            raise ValidationError("Travel cannot be scheduled with less than 2 passengers")

        self.state = "scheduled"

        return

    def launch_travel(self):
        """
        This method responsible for launching the travel
        """
        self.state = "running"
        self.started_at = fields.Datetime.now()
        return

    def cancel_travel(self):
        """
        This method responsible for canceling the travel
        """
        self.state = "cancel"

    def travel_completed(self):
        """
        This method complete the travel
        """
        self.state = "end"
        self.ended_at = fields.Datetime.now()
        return

    @api.onchange('first_driver_id')
    def _onchange_first_driver(self):
        print("ok")
        pass
