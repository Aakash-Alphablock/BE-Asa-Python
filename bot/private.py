# all methods/services defined in private are supposed to be used within the bot app/service only.
# never call any of the methods of public in private else later it will cause circular import issue.

from bot import dal
from typing import Optional

class BotService():
    def create_new_bot(self, name, description, token, user_id, is_demo_bot):
        bot =  dal.create_new_bot(name, description, token, user_id, is_demo_bot)
        return bot.to_dict()
    
    def get_bot_details(self, bot_id: int) -> Optional[dict]:
        """ Get bot details by bot_id.
        
        Args:
            bot_id (int): Bot id

        Returns:
            dict: Bot model object (Bot details)
        """
        bot = dal.get_bot_details(bot_id)
        if not bot:
            return None
        
        return bot.to_dict()