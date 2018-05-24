from functools import partial


class EventBase:

    def __init__(self, sdk):
        """
        Event base prototype
        :param sdk:
        """
        self.sdk = sdk
        self.send = partial(self.sdk.send_text_to_chat, disable_web_page_preview=True)
