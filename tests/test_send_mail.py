# from send_email import send_email
# from app import mail
#
#
# def test_send(app):
#
#     with mail.record_messages() as outbox:
#         send_email('testing', 'tieto.library@gmail.com', ['tieto.library@gmail.com'], 'test', 'test')
#         assert len(outbox) == 1
#         msg = outbox[0]
#         assert msg.subject == "testing"
