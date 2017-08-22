import unittest
from rpc.notifications import send_email, send_sms
from nameko.rpc import rpc
from unittest.mock import MagicMock, patch
from src.main import SendgridService
