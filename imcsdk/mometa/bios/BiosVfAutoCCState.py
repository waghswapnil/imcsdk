"""This module contains the general information for BiosVfAutoCCState ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfAutoCCStateConsts:
    VP_AUTO_CCSTATE_DISABLED = "Disabled"
    VP_AUTO_CCSTATE_ENABLED = "Enabled"
    _VP_AUTO_CCSTATE_DISABLED = "disabled"
    _VP_AUTO_CCSTATE_ENABLED = "enabled"
    VP_AUTO_CCSTATE_PLATFORM_DEFAULT = "platform-default"


class BiosVfAutoCCState(ManagedObject):
    """This is BiosVfAutoCCState class."""

    consts = BiosVfAutoCCStateConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfAutoCCState", "biosVfAutoCCState", "auto-cc-state", VersionMeta.Version304a, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfAutoCCState", "biosVfAutoCCState", "auto-cc-state", VersionMeta.Version313a, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_auto_cc_state": MoPropertyMeta("vp_auto_cc_state", "vpAutoCCState", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version313a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version313a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version313a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_auto_cc_state": MoPropertyMeta("vp_auto_cc_state", "vpAutoCCState", "string", VersionMeta.Version313a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version313a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAutoCCState": "vp_auto_cc_state", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAutoCCState": "vp_auto_cc_state", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_auto_cc_state = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfAutoCCState", parent_mo_or_dn, **kwargs)

