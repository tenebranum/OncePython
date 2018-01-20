from django.core import mail
from django.test import TestCase,Client
from django.core.urlresolvers import reverse


class ContactAdminFormTests(TestCase):


	def test_email_sent(self):
		client = Client()
		client.login(username="tenebranum",password="kava98banga")
		response = client.post(reverse('contact_admin'), {
								'from_email': 'from@gmail.com',
								'subject': 'test email',
								'message': 'test email message'
								})

		msg = mail.outbox[0].message()
		self.assertEqual(msg.get('subject'),'test email')
		self.assertEqual(msg.get('From'),u'from@gmail.com')
		self.assertEqual(msg.get_payload(),'test email message',)