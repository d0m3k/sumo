#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# go to additional mode
netedit.additionalMode()

# select parkingArea
netedit.changeElement("parkingArea")

# change reference to center
netedit.changeDefaultValue(10, "reference center")

# create parkingArea in mode "reference center"
netedit.leftClick(referencePosition, 250, 250)

# change to move mode
netedit.moveMode()

# move parkingArea to right
netedit.moveElement(referencePosition, 150, 300, 250, 300)

# go to inspect mode
netedit.inspectMode()

# inspect parkingArea
netedit.leftClick(referencePosition, 350, 300)

# block additional
netedit.modifyBoolAttribute(14, False)

# change to move mode
netedit.moveMode()

# try to move parkingArea to right (must be blocked)
netedit.moveElement(referencePosition, 250, 300, 350, 300)

# go to inspect mode
netedit.inspectMode()

# inspect parkingArea
netedit.leftClick(referencePosition, 350, 300)

# unblock additional
netedit.modifyBoolAttribute(14, False)

# change to move mode
netedit.moveMode()

# move parkingArea to right (must be allowed)
netedit.moveElement(referencePosition, 250, 300, 350, 300)

# Check undos and redos
netedit.undo(referencePosition, 5)
netedit.redo(referencePosition, 5)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
