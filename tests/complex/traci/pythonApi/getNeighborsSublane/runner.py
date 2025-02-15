#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2008-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    runner.py
# @author  Michael Behrisch
# @author  Jakob Erdmann
# @author  Daniel Krajzewicz
# @date    2011-03-04
# @version $Id$


from __future__ import print_function
from __future__ import absolute_import
import os
import sys

SUMO_HOME = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "..")
sys.path.append(os.path.join(os.environ.get("SUMO_HOME", SUMO_HOME), "tools"))
if len(sys.argv) > 1:
    import libsumo as traci  # noqa
    traci.vehicle.addFull = traci.vehicle.add
    traci.vehicle.add = traci.vehicle.addLegacy
else:
    import traci  # noqa
    traci._vehicle.VehicleDomain.addFull = traci._vehicle.VehicleDomain.add
    traci._vehicle.VehicleDomain.add = traci._vehicle.VehicleDomain.addLegacy
import sumolib  # noqa


def step():
    s = traci.simulation.getTime()
    traci.simulationStep()
    return s


egoID = "ego"


def printNeighInfo():
    print("Neigh infos for ego:")
    rightFollowers = traci.vehicle.getRightFollowers(egoID)
    print("  rightFollowers:\n  %s" % sorted(rightFollowers))
    rightLeaders = traci.vehicle.getRightLeaders(egoID)
    print("  rightLeaders:\n  %s" % sorted(rightLeaders))
    leftFollowers = traci.vehicle.getLeftFollowers(egoID)
    print("  leftFollowers:\n  %s" % sorted(leftFollowers))
    leftLeaders = traci.vehicle.getLeftLeaders(egoID)
    print("  leftLeaders:\n  %s" % sorted(leftLeaders))
    rightFollowersBlocking = traci.vehicle.getRightFollowers(egoID, True)
    print("  rightFollowers (only blocking):\n  %s" % sorted(rightFollowersBlocking))
    rightLeadersBlocking = traci.vehicle.getRightLeaders(egoID, True)
    print("  rightLeaders (only blocking):\n  %s" % sorted(rightLeadersBlocking))
    leftFollowersBlocking = traci.vehicle.getLeftFollowers(egoID, True)
    print("  leftFollowers (only blocking):\n  %s" % sorted(leftFollowersBlocking))
    leftLeadersBlocking = traci.vehicle.getLeftLeaders(egoID, True)
    print("  leftLeaders (only blocking):\n  %s" % sorted(leftLeadersBlocking))
    sys.stdout.flush()


traci.start([sumolib.checkBinary('sumo'), "-c", "sumo.sumocfg"])
# ~ traci.init(port=12345)

for i in range(1):
    print("step", step())

for vehID in traci.vehicle.getIDList():
    traci.vehicle.changeLaneRelative(vehID, 0, 999)

for i in range(2):
    print("step", step())

while egoID in traci.vehicle.getIDList():
    printNeighInfo()
    print("step", step())
step()
# done
traci.close()
