from odoo import models, fields

class SafetyRound(models.Model):
    _name = "field.service.safety.round"
    _description = "Safety Round for Field Service"

    name = fields.Char(string="Description", required=True)
    task_id = fields.Many2one('field.service.task', string="Field Service Task", ondelete="cascade")
    checks = fields.One2many('field.service.safety.check', 'round_id', string="Checks")

class SafetyCheck(models.Model):
    _name = "field.service.safety.check"
    _description = "Safety Check for Round"

    round_id = fields.Many2one('field.service.safety.round', string="Safety Round", ondelete="cascade")
    item = fields.Char(string="Item", required=True)
    location = fields.Char(string="Location", help="Where is the item located?")
    status = fields.Selection([('ok', 'OK'), ('issue', 'Issue')], string="Status", required=True)
    action_required = fields.Text(string="Action Required", help="What action needs to be taken?")
    comments = fields.Text(string="Comments")
    image = fields.Binary(string="Image", attachment=True, help="Optional image of the inspected item")
    map_url = fields.Char(string="Map URL", help="Link to map showing location")
