from debug import *

all_master_players = {}
redundant_master_players = {}
for match_group in ents('ModelMatchStub')[0].match_groups:
 level = match_group.level
 for exposure_cnt, priority_item in match_group.match_priority_items.iteritems():
  for match_id in priority_item.match_id_list:
   if match_id not in all_master_players:
    all_master_players[match_id] = []
   all_master_players[match_id].append((level, exposure_cnt))
   if len(all_master_players[match_id]) > 1:
    redundant_master_players[match_id] = all_master_players[match_id]

redundant_master_players


all_slave_players = {}
redundant_slave_players = {}
for match_group in ents('ModelMatchStub')[0].match_groups:
 level = match_group.level
 for gender, match_gender_item in match_group.match_gender_items.iteritems():
  for match_item in match_gender_item.match_item_list:
   praise_rate = match_item.praise_rate
   for exposure_cnt, priority_item in match_item.match_priority_items.iteritems():
    for match_id in priority_item.match_id_list:
     if match_id not in all_slave_players:
      all_slave_players[match_id] = []
     all_slave_players[match_id].append((level, gender, praise_rate, exposure_cnt))
     if len(all_slave_players[match_id]) > 1:
      redundant_slave_players[match_id] = all_slave_players[match_id]

redundant_slave_players

import utils
pid = 'YxreaKigwW5sYjJL'
ents('ModelMatchStub')[0].all_match_units[pid].log_dict()
master_param_list = [1, 0]
slave_param_list = [1, 0, 11, 0]
total_exposure_cnt = 444
daily_exposure_cnt = 50
praise_cnt = 49

master_level = master_param_list[0]
master_exposure_cnt = master_param_list[1]
slave_level = slave_param_list[0]
gender = slave_param_list[1]
slave_praise_rate = slave_param_list[2]
slave_exposure_cnt = slave_param_list[3]

pid in ents('ModelMatchStub')[0].match_groups[master_level].match_priority_items[master_exposure_cnt].match_id_list
pid in ents('ModelMatchStub')[0].match_groups[slave_level].match_gender_items[gender].match_item_list[slave_praise_rate].match_priority_items[slave_exposure_cnt].match_id_list

ents('ModelMatchStub')[0].match_groups[master_level].match_priority_items[master_exposure_cnt].match_id_list.remove(pid)
ents('ModelMatchStub')[0].match_groups[slave_level].match_gender_items[gender].match_item_list[slave_praise_rate].match_priority_items[slave_exposure_cnt].match_id_list.remove(pid)

ents('ModelMatchStub')[0].all_match_units[pid]
ents('ModelMatchStub')[0].all_match_units[pid].total_exposure_cnt
ents('ModelMatchStub')[0].all_match_units[pid].daily_exposure_cnt
ents('ModelMatchStub')[0].all_match_units[pid].praise_cnt
ents('ModelMatchStub')[0].all_match_units[pid].last_exposure_stamp
ents('ModelMatchStub')[0].all_match_units[pid].dirty_attributes

ents('ModelMatchStub')[0].all_match_units[pid].total_exposure_cnt = total_exposure_cnt
ents('ModelMatchStub')[0].all_match_units[pid].daily_exposure_cnt = daily_exposure_cnt
ents('ModelMatchStub')[0].all_match_units[pid].praise_cnt = praise_cnt
ents('ModelMatchStub')[0].all_match_units[pid].last_exposure_stamp = utils.get_time()
ents('ModelMatchStub')[0].all_match_units[pid].dirty_attributes.extend(['praise_cnt', 'daily_exposure_cnt', 'total_exposure_cnt', 'last_exposure_stamp'])
ents('ModelMatchStub')[0].all_match_units[pid].dirty_attributes

true_level = ents('ModelMatchStub')[0].all_match_units[pid].level
ents('ModelMatchStub')[0].match_groups[true_level].reg_match_unit(ents('ModelMatchStub')[0].all_match_units[pid])


all_master_players = {}
redundant_master_players = {}
for match_group in ents('ModelMatchStub')[0].match_groups:
 level = match_group.level
 for exposure_cnt, priority_item in match_group.match_priority_items.iteritems():
  for match_id in priority_item.match_id_list:
   if match_id == pid:
    print level,exposure_cnt


all_slave_players = {}
redundant_slave_players = {}
for match_group in ents('ModelMatchStub')[0].match_groups:
 level = match_group.level
 for gender, match_gender_item in match_group.match_gender_items.iteritems():
  for match_item in match_gender_item.match_item_list:
   praise_rate = match_item.praise_rate
   for exposure_cnt, priority_item in match_item.match_priority_items.iteritems():
    for match_id in priority_item.match_id_list:
     if match_id == pid:
      print level, gender, praise_rate, exposure_cnt


ents('ModelMatchStub')[0].all_match_units[pid].log_dict()