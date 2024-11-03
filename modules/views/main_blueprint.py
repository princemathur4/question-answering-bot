from flask import Blueprint, request, jsonify
from modules.exceptions import InvalidRequestPayload
from modules.controllers.question_controller import QuestionController

main_bp = Blueprint('main', __name__)


@main_bp.route('/answer-questions', methods=['POST'])
def answer_questions():
    document_file = request.files.get('document_file')
    validate_document_file(document_file)

    questions_file = request.files.get('questions_file')
    validate_questions_file(questions_file)

    answers = QuestionController().process_for_answers(document_file, questions_file)

    return jsonify({"results": answers})


def validate_document_file(document_file):
    if not document_file:
        raise InvalidRequestPayload(error_message="No file for document received for upload")

    filename = document_file.filename
    if not filename.lower().endswith('.pdf'):
        raise InvalidRequestPayload(error_message="This file format is not supported. Supported file format: '.pdf'")


def validate_questions_file(questions_file):
    if not questions_file:
        raise InvalidRequestPayload(error_message="No file for questions received for upload")

    filename = questions_file.filename
    if not filename.lower().endswith('.json'):
        raise InvalidRequestPayload(error_message="This file format is not supported. Supported file format: '.json'")
