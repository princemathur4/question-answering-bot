from flask import Blueprint, jsonify
from modules.exceptions import RootException
import traceback

base_bp = Blueprint('ErrorHandler', __name__)


@base_bp.app_errorhandler(Exception)
def base_error(e):
    try:
        raise e
    except RootException as er:
        print({
            'error_code': er.error_code,
            'error_message': er.error_message,
            'internal_err_message': er.internal_err_message
        })
        return jsonify({'status': False, 'error_message': er.internal_err_message, 'error_code': er.error_code}), er.http_code
    except Exception as er:
        print(traceback.format_exc())
        return jsonify({'status': False, 'error_message': "Something went wrong"}), 500
