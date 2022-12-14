import logging
from django.conf import settings
from pubnub.models.consumer.v3.channel import Channel
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException

from DATN.apps.user.models import CreateUserModel
from DATN.config.settings.base import PUBNUB_PUBLISH_KEY, PUBNUB_SUBSCRIBE_KEY, PUBNUB_SECRET, SERVER_PUBNUB_UUID

logger = logging.getLogger(__name__)
pnconfig = PNConfiguration()
pnconfig = PNConfiguration()
pnconfig.publish_key = PUBNUB_PUBLISH_KEY
pnconfig.subscribe_key = PUBNUB_SUBSCRIBE_KEY
pnconfig.secret_key = PUBNUB_SECRET
pnconfig.uuid = SERVER_PUBNUB_UUID

pubnub = PubNub(pnconfig)

class PubNubService:
    DEFAULT_NOTIFICATION_TTL = 60 # 60 minutes

    @staticmethod
    def get_notification_token_for_user(user: CreateUserModel, ttl: int = DEFAULT_NOTIFICATION_TTL):
        envalope = pubnub.grant_token() \
            .channels([Channel.id(user.get_notification_channel_name()).read().delete()]) \
            .ttl(ttl) \
            .authorized_uuid(user.get_notification_channel_name()) \
            .sync()
        token = envalope.result.token
        token_payload = pubnub.parse_token(token)

        return {
            "exp_timestamp": token_payload["timestamp"],
            "token": token,
            "ttl": token_payload["ttl"],
        }
    @staticmethod
    def send_notification_to_user(user: CreateUserModel, message):
        try:
            pubnub.publish() \
            .channel(user.get_notification_channel_name()) \
            .message(message) \
            .use_post(use_post=True) \
            .sync()
        except PubNubException as e:
            logger.error(e)