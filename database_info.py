"""
This module holds all kinds of information regarding the database and it's tables.
"""
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.join(DIR_PATH, "python_wowDB.db")

"""
The table indexes will be defined below this comment. They are:
The number that is associated with the table's column if all the columns are taken
Example: Table has columns X, Y, Z
X would be column number 0
Y - 1
Z - 2
"""

# creature_defualt_xp_rewards table
DBINDEX_CREATURE_DEFAULT_XP_REWARDS_ENTRY = 0
DBINDEX_CREATURE_DEFAULT_XP_REWARDS_LEVEL = 1
DBINDEX_CREATURE_DEFAULT_XP_REWARDS_XP = 2

# creature_template table
DBINDEX_CREATURE_TEMPLATE_ENTRY = 0
DBINDEX_CREATURE_TEMPLATE_NAME = 1
DBINDEX_CREATURE_TEMPLATE_LEVEL = 2
DBINDEX_CREATURE_TEMPLATE_HEALTH = 3
DBINDEX_CREATURE_TEMPLATE_MANA = 4
DBINDEX_CREATURE_TEMPLATE_MIN_DMG = 5
DBINDEX_CREATURE_TEMPLATE_MAX_DMG = 6
DBINDEX_CREATURE_TEMPLATE_QUEST_RELATION_ID = 7

# creatures table
DBINDEX_CREATURES_GUID = 0
DBINDEX_CREATURES_CREATURE_ID = 1
DBINDEX_CREATURES_ZONE = 2
DBINDEX_CREATURES_SUB_ZONE = 3

# level_xp_requirement table
DBINDEX_LEVEL_XP_REQUIREMENT_LEVEL = 0
DBINDEX_LEVEL_XP_REQUIREMENT_XP_REQUIRED = 1

# levelup_stats table
DBINDEX_LEVELUP_STATS_LEVEL = 0
DBINDEX_LEVELUP_STATS_HEALTH = 1
DBINDEX_LEVELUP_STATS_MANA = 2
DBINDEX_LEVELUP_STATS_STRENGTH = 3

# paladin_spells_template table
DBINDEX_PALADIN_SPELLS_TEMPLATE_ID = 0
DBINDEX_PALADIN_SPELLS_TEMPLATE_NAME = 1
DBINDEX_PALADIN_SPELLS_TEMPLATE_RANK = 2
DBINDEX_PALADIN_SPELLS_TEMPLATE_LEVEL_REQUIRED = 3
DBINDEX_PALADIN_SPELLS_TEMPLATE_DAMAGE1 = 4
DBINDEX_PALADIN_SPELLS_TEMPLATE_DAMAGE2 = 5
DBINDEX_PALADIN_SPELLS_TEMPLATE_DAMAGE3 = 6
DBINDEX_PALADIN_SPELLS_TEMPLATE_HEAL1 = 7
DBINDEX_PALADIN_SPELLS_TEMPLATE_HEAL2 = 8
DBINDEX_PALADIN_SPELLS_TEMPLATE_HEAL3 = 9
DBINDEX_PALADIN_SPELLS_TEMPLATE_MANA_COST = 10
DBINDEX_PALADIN_SPELLS_TEMPLATE_COMMENT = 11

# quest_template table
DBINDEX_QUEST_TEMPLATE_ENTRY = 0
DBINDEX_QUEST_TEMPLATE_NAME = 1
DBINDEX_QUEST_TEMPLATE_LEVEL_REQUIRED = 2
DBINDEX_QUEST_TEMPLATE_MONSTER_REQUIRED = 3
DBINDEX_QUEST_TEMPLATE_AMOUNT_REQUIRED = 4
DBINDEX_QUEST_TEMPLATE_ZONE = 5
DBINDEX_QUEST_TEMPLATE_SUB_ZONE = 6
DBINDEX_QUEST_TEMPLATE_XP_REWARD = 7
DBINDEX_QUEST_TEMPLATE_COMMENT = 8