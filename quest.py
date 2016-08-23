class Quest:
    def __init__(self, quest_name: str, quest_id, xp_reward: int,
                 level_required: int, is_completed: bool = False):
        self.name = quest_name
        self.ID = quest_id
        self.xp_reward = xp_reward
        self.is_completed = is_completed
        self.required_level = level_required

    def update_kills(self):
        """ This method updates the required kills if the quest is a KillQuest"""
        pass

    def _check_if_complete(self):
        """ This method checks if the quest is completed on each new addition and completes it if it is"""
        pass

    def _quest_complete(self):
        self.is_completed = True

    def give_reward(self):
        return self.xp_reward


class KillQuest(Quest):
    """
    Standard kill X of Y quest
    """
    def __init__(self, quest_name: str, quest_id, required_monster: str, xp_reward: int,
                 level_required: int, required_kills: int, is_completed: bool = False):
        super().__init__(quest_name, quest_id, xp_reward, level_required, is_completed)
        self.required_monster = required_monster
        self.required_kills = required_kills
        self.kills = 0

    def __str__(self):
        return (
            "{quest_name} - Requires {required_kills} {monster_name} kills. Rewards {xp_reward} experience."
            .format(quest_name=self.name, required_kills=self.required_kills,
                    monster_name=self.required_monster, xp_reward=self.xp_reward)
                )

    def update_kills(self):
        self.kills += 1
        print("Quest {name}: {kills}/{required_kills} {monster_name} slain.".format(name=self.name,
                                                                                    kills=self.kills,
                                                                                    required_kills=self.required_kills,
                                                                                    monster_name=self.required_monster))
        self._check_if_complete()

    def _check_if_complete(self):
        if self.kills == self.required_kills:
            self._quest_complete()