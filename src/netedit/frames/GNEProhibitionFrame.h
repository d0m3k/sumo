/****************************************************************************/
// Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
// Copyright (C) 2001-2019 German Aerospace Center (DLR) and others.
// This program and the accompanying materials
// are made available under the terms of the Eclipse Public License v2.0
// which accompanies this distribution, and is available at
// http://www.eclipse.org/legal/epl-v20.html
// SPDX-License-Identifier: EPL-2.0
/****************************************************************************/
/// @file    GNEProhibitionFrame.h
/// @author  Mirko Barthauer (Technische Universitaet Braunschweig)
/// @date    May 2018
/// @version $Id$
///
// The Widget for remove network-elements
/****************************************************************************/
#ifndef GNEProhibitionFrame_h
#define GNEProhibitionFrame_h

// ===========================================================================
// included modules
// ===========================================================================

#include "GNEFrame.h"

// ===========================================================================
// class declarations
// ===========================================================================
class GNEConnection;
class GNEAttributeCarrier;

// ===========================================================================
// class definitions
// ===========================================================================
/**
 * @class GNEProhibitionFrame
 * The Widget for editing connection foes
 */
class GNEProhibitionFrame : public GNEFrame {
    /// @brief FOX-declaration
    FXDECLARE(GNEProhibitionFrame)

public:

    /// @brief the prohibition status of a connection
    enum ConnStatus {
        UNDEFINED,
        PROHIBITED,
        PROHIBITING
    };

    // ===========================================================================
    // class RelativeToConnection
    // ===========================================================================

    class RelativeToConnection : protected FXGroupBox {

    public:
        /// @brief constructor
        RelativeToConnection(GNEProhibitionFrame* prohibitionFrameParent);

        /// @brief destructor
        ~RelativeToConnection();

        /// @brief update description
        void updateDescription() const;

    private:
        /// @brief pointer to prohibition frame parent
        GNEProhibitionFrame* myProhibitionFrameParent;

        /// @brief the label that shows the currently selected connection
        FXLabel* myConnDescriptionLabel;
    };

    // ===========================================================================
    // class ProhibitionLegend
    // ===========================================================================

    class ProhibitionLegend : protected FXGroupBox {

    public:
        /// @brief constructor
        ProhibitionLegend(GNEProhibitionFrame* prohibitionFrameParent);

        /// @brief destructor
        ~ProhibitionLegend();

        /// @brief get color for non-conflicting pairs of connections
        const RGBColor &getUndefinedColor() const;

        /// @brief get color for waiting connections
        const RGBColor &getProhibitedColor() const;

        /// @brief get color for connections with precedence
        const RGBColor &getProhibitingColor() const;

        /// @brief get color for unregulated conflicts
        const RGBColor &getUnregulatedConflictColor() const;

        /// @brief get color for mutual conflicts
        const RGBColor &getMutualConflictColor() const;

    private:
        /// @brief color for non-conflicting pairs of connections
        RGBColor myUndefinedColor;

        /// @brief color for waiting connections
        RGBColor myProhibitedColor;

        /// @brief color for connections with precedence
        RGBColor myProhibitingColor;

        /// @brief color for unregulated conflicts
        RGBColor myUnregulatedConflictColor;

        /// @brief color for mutual conflicts
        RGBColor myMutualConflictColor;
    };

    // ===========================================================================
    // class Modifications
    // ===========================================================================

    class Modifications : protected FXGroupBox {

    public:
        /// @brief constructor
        Modifications(GNEProhibitionFrame* prohibitionFrameParent);

        /// @brief destructor
        ~Modifications();

    private:
        /// @brief "Save" button
        FXButton* mySaveButton;

        /// @brief "Cancel" button
        FXButton* myCancelButton;
    };

    /**@brief Constructor
     * @brief parent FXHorizontalFrame in which this GNEFrame is placed
     * @brief viewNet viewNet that uses this GNEFrame
     */
    GNEProhibitionFrame(FXHorizontalFrame* horizontalFrameParent, GNEViewNet* viewNet);

    /// @brief Destructor
    ~GNEProhibitionFrame();

    /**@brief handle prohibitions and set the relative colouring
     * @param objectsUnderCursor collection of objects under cursor after click over view
     */
    void handleProhibitionClick(const GNEViewNetHelper::ObjectsUnderCursor& objectsUnderCursor);

    /// @brief show prohibition frame
    void show();

    /// @brief hide prohibition frame
    void hide();

    /// @name FOX-callbacks
    /// @{
    /// @brief Called when the user presses the OK-Button saves any prohibition modifications
    long onCmdOK(FXObject*, FXSelector, void*);

    /// @brief Called when the user presses the Cancel-button discards any prohibition modifications
    long onCmdCancel(FXObject*, FXSelector, void*);

    /// @}

protected:
    /// @brief FOX needs this
    GNEProhibitionFrame() {}
    
    /// @brief build prohibition
    void buildProhibition(GNEConnection* conn, bool mayDefinitelyPass, bool allowConflict, bool toggle);

private:
    /// @brief Relative To Connection
    RelativeToConnection* myRelativeToConnection;

    /// @brief prohibition legend
    ProhibitionLegend* myProhibitionLegend;

    /// @brief Modifications
    Modifications* myModifications;

    /// @brief the connection which prohibits
    GNEConnection* myCurrentConn;

    /// @brief the set of connections which
    std::set<GNEConnection*> myConcernedConns;
};


#endif

/****************************************************************************/

