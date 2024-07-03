from bot import models
from typing import Optional

def create_new_bot(name: str, description: str, token: str, user_id:int, is_demo_bot: bool) -> models.Bot:
    """Create new bot.
    
    Args:
        name (str): Bot name
        description (str): Bot description
        token (str): Bot token
        user_id (int): User id
        is_demo_bot (bool): Is demo bot

    Returns:
        models.Bot: Bot model object

    """
    return models.Bot.objects.create(
        name=name,
        description=description,
        token=token,
        user_id=user_id,
        is_demo_bot=is_demo_bot
    )

def get_bot_details(bot_id: int) -> Optional[models.Bot]:
    """ Get bot details by bot_id.

    Args:
        bot_id (int): Bot id

    Returns:
        models.Bot: Bot model object
    
    """
    return models.Bot.objects.filter(id=bot_id).last()