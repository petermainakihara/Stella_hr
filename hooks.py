import logging

_logger = logging.getLogger(__name__)

def post_init_hook(env):
    _logger.info("post_init_hook: setting attendance radius to 0.3 km")
    env["res.partner"].sudo().search([]).write({"attendance_radius_km": 0.3})
    _logger.info("post_init_hook: done")

def post_migrate_hook(env):
    _logger.info("post_migrate_hook: setting attendance radius to 0.3 km")
    env["res.partner"].sudo().search([]).write({"attendance_radius_km": 0.3})
    _logger.info("post_migrate_hook: done")