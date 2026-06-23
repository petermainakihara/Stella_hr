import logging
_logger = logging.getLogger(__name__)

def post_init_hook(env):
    # Skip heavy work if the registry is already ready (e.g., during normal startup)
    if env.registry.ready:
        _logger.info("post_init_hook: skipped (registry already ready)")
        return
    _logger.info("post_init_hook: start")
    # Limit the search to avoid long queries during installation
    partners = env["res.partner"].search([
        ("attendance_radius_km", "<", 30.0),
    ], limit=1000)
    if partners:
        partners.write({"attendance_radius_km": 30.0})
    _logger.info("post_init_hook: end")