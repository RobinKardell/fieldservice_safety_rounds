from odoo import models, fields, api

class FieldServiceTask(models.Model):
    _inherit = "field.service.task"

    safety_round_ids = fields.One2many('field.service.safety.round', 'task_id', string="Safety Rounds")

    def copy_previous_task(self, previous_task_id):
        previous_task = self.env['field.service.task'].browse(previous_task_id)
        new_task = self.copy()
        for round in previous_task.safety_round_ids:
            new_round = round.copy()
            new_round.task_id = new_task.id
        return new_task

    def generate_safety_round_pdf(self):
        return self.env.ref('fieldservice_safety_rounds.safety_round_report').report_action(self)
