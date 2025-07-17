from odoo import models, fields, api


class Vehicles(models.Model):
    _name = "travel.vehicle"
    _description = "Travel Vehicle"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name", copy=True, readonly=True)

    image = fields.Image(string="Image", copy=False)

    manufacturer = fields.Char(string="Manufacturer", copy=True, required=True)

    model = fields.Char(string="Model", copy=True, required=True)

    color = fields.Char(string="Color", copy=True, required=True)

    year = fields.Date(string="Release date", copy=True, required=True)

    capacity = fields.Float(string="Capacity (kg)", copy=True, required=True)

    type_id = fields.Many2one(
        comodel_name="travel.vehicle.types",
        ondelete="restrict",
        string="Vehicle type",
        copy=True,
        required=True
    )

    fuel_type_id = fields.Many2one(
        comodel_name="travel.vehicle.fuel.types",
        ondelete="restrict",
        string="Vehicle Fuel type",
        copy=True,
        required=True
    )

    in_repair_count = fields.Integer(
        string="In repair count",
        copy=True,
        default=0
    )

    successful_repairs_count = fields.Integer(
        string="Successful repairs count",
        copy=True,
        default=0
    )

    fail_repairs_count = fields.Integer(
        string="Failed repairs count",
        copy=True,
        default=0
    )

    tags = fields.Many2many(
        comodel_name="travel.vehicle.tags",
        string="Tags",
        copy=True
    )

    drivers = fields.Many2many(
        comodel_name="travel.vehicle.drivers",
        string="Authorized drivers",
        copy=True
    )

    travels_count = fields.Integer(
        string="Travels count",
        compute="_compute_travels_count"
    )

    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("used", "Used"),
            ("damaged", "Damaged"),
            ("repair", "In-Repair"),
            ("fail_repair", "Repair Failed"),
            ("broken", "Broken")
        ],
        string="State",
        copy=True,
        default="new"
    )

    def create(self, vals_list):
        for rec in vals_list:
            rec['name'] = rec['manufacturer'] + " " + rec['model']
        return super(Vehicles, self).create(vals_list)

    def write(self, vals_list):

        manufacturer = self.manufacturer
        model = self.model

        if "manufacturer" in vals_list.keys():
            manufacturer = vals_list['manufacturer']

        if "model" in vals_list.keys():
            model = vals_list['model']

        vals_list['name'] = manufacturer + " " + model

        return super(Vehicles, self).write(vals_list)

    def read(self, fields=..., load=...):
        return super(Vehicles, self).read(fields, load)

    def send_to_repair(self):
        self.in_repair_count += 1
        self.state = 'repair'
        return

    def successful_repair(self):
        self.successful_repairs_count += 1
        self.state = "used"
        return

    def failed_repair(self):
        self.fail_repairs_count += 1
        self.state = "fail_repair"
        return

    def related_travels(self):
        # action = self.env["ir.actions.act_window"]._for_xml_id("travel.action_window_travel")
        # action['context'] = {}
        # action['domain'] = [("vehicle_id", "=", self.id)]

        action = {
            'type': 'ir.actions.act_window',
            'name': f'{self.name} - Related Travels',
            'view_mode': 'list, from',
            'views': [(False, 'list'), (False, 'form')],
            'res_model': 'travel.travel',
            'domain': [("vehicle_id", "=", self.id)]
        }

        return action

    def _compute_travels_count(self):

        for vehicle in self:
            # There is at least 3 ways

            # Recover the count as (Query)
            count = self.env['travel.travel'].search_count([("vehicle_id", "=", vehicle.id)])

            # Assign the value
            vehicle.travels_count = count
