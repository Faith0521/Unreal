#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2026/3/3 09:39
# @Author : yinyufei
# @File : ToolLaunchers.py
# @Project : Unreal
# coding=utf-8

import unreal
from UnrealUtils import (run_editor_utility_widget, _run)


def launch_actor_manager_tool():
    bp_path = '/Game/BlueprintDemostration/UtilityWidget/BP_UWidget_ActorManager.BP_UWidget_ActorManager'
    run_editor_utility_widget(bp_path)
    return bp_path


#######################################################################
# copy the following code to your script
#######################################################################
from UnrealUtils import _run

if __name__ == '__main__':
    unreal.log(_run(locals()))
