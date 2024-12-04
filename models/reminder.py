from odoo import models, fields, api

class SafetyReminder(models.Model):
    _name = "field.service.safety.reminder"
    _description = "Reminder for Actions Requiring Follow-Up"

    task_id = fields.Many2one('field.service.task', string="Field Service Task")
    action_required = fields.Text(string="Action Required")
    due_date = fields.Date(string="Due Date")

    @api.model
    def send_reminders(self):
        reminders = self.search([('due_date', '<=', fields.Date.today())])
        for reminder in reminders:
            # Send reminder logic
            pass
