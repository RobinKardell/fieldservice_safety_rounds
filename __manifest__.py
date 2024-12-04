{
    'name': "Field Service Safety Rounds",
    'summary': "Add safety rounds and checks for field service tasks, with PDF generation, reminders, and reporting.",
    'description': """
        This module extends Field Service tasks to include safety rounds,
        allowing users to track inspections, generate PDF reports, and get reminders
        for actions requiring follow-up.
    """,
    'author': "Your Name",
    'version': '16.0.1.0',
    'depends': ['fieldservice', 'base', 'web'],
    'data': [
        'views/field_service_task_views.xml',
        'views/safety_round_views.xml',
        'views/report_templates.xml',
        'reports/safety_round_report.xml',
        'data/ir_cron_data.xml',
    ],
    'assets': {
        'web.assets_backend': [],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}