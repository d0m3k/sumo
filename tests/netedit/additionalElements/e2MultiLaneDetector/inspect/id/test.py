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

# recompute
netedit.rebuildNetwork()

# go to additional mode
netedit.additionalMode()

# select E2
netedit.changeElement("e2MultilaneDetector")

# create E2 with default parameters
netedit.leftClick(referencePosition, 190, 255)
netedit.leftClick(referencePosition, 440, 255)
netedit.typeEnter()

# create second  with default parameters (for ID)
netedit.leftClick(referencePosition, 440, 210)
netedit.leftClick(referencePosition, 190, 210)
netedit.typeEnter()

# go to additional mode
netedit.inspectMode()

# inspect first E2
netedit.leftClick(referencePosition, 320, 255)

# Change parameter id with a non valid value (Duplicated ID)
netedit.modifyAttribute(0, "e2MultilaneDetector_1", True)

# Change parameter id with a non valid value (Invalid ID)
netedit.modifyAttribute(0, "Id with spaces", True)

# Change parameter id with a valid value
netedit.modifyAttribute(0, "correctID", True)

# Check undo redo
netedit.undo(referencePosition, 3)
netedit.redo(referencePosition, 3)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
