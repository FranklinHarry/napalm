
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import config
import state
import route_selection_options
import default_route_distance
import confederation
import use_multiple_paths
import graceful_restart
import afi_safis
import apply_policy
class global_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp - based on the path /bgp/global. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Global configuration for the BGP router
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__config','__state','__route_selection_options','__default_route_distance','__confederation','__use_multiple_paths','__graceful_restart','__afi_safis','__apply_policy',)

  _yang_name = 'global'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    self._extmethods = False
    self.__graceful_restart = YANGDynClass(base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    self.__use_multiple_paths = YANGDynClass(base=use_multiple_paths.use_multiple_paths, is_container='container', yang_name="use-multiple-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    self.__default_route_distance = YANGDynClass(base=default_route_distance.default_route_distance, is_container='container', yang_name="default-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    self.__afi_safis = YANGDynClass(base=afi_safis.afi_safis, is_container='container', yang_name="afi-safis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    self.__apply_policy = YANGDynClass(base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    self.__route_selection_options = YANGDynClass(base=route_selection_options.route_selection_options, is_container='container', yang_name="route-selection-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    self.__confederation = YANGDynClass(base=confederation.confederation, is_container='container', yang_name="confederation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'bgp', u'global']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /bgp/global/config (container)

    YANG Description: Configuration parameters relating to the global BGP router
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /bgp/global/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters relating to the global BGP router
    """
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /bgp/global/state (container)

    YANG Description: State information relating to the global BGP router
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /bgp/global/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State information relating to the global BGP router
    """
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)


  def _get_route_selection_options(self):
    """
    Getter method for route_selection_options, mapped from YANG variable /bgp/global/route_selection_options (container)

    YANG Description: Parameters relating to options for route selection
    """
    return self.__route_selection_options
      
  def _set_route_selection_options(self, v, load=False):
    """
    Setter method for route_selection_options, mapped from YANG variable /bgp/global/route_selection_options (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_selection_options is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_selection_options() directly.

    YANG Description: Parameters relating to options for route selection
    """
    try:
      t = YANGDynClass(v,base=route_selection_options.route_selection_options, is_container='container', yang_name="route-selection-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_selection_options must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route_selection_options.route_selection_options, is_container='container', yang_name="route-selection-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)""",
        })

    self.__route_selection_options = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_selection_options(self):
    self.__route_selection_options = YANGDynClass(base=route_selection_options.route_selection_options, is_container='container', yang_name="route-selection-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)


  def _get_default_route_distance(self):
    """
    Getter method for default_route_distance, mapped from YANG variable /bgp/global/default_route_distance (container)

    YANG Description: Administrative distance (or preference) assigned to
routes received from different sources
(external, internal, and local).
    """
    return self.__default_route_distance
      
  def _set_default_route_distance(self, v, load=False):
    """
    Setter method for default_route_distance, mapped from YANG variable /bgp/global/default_route_distance (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_route_distance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_route_distance() directly.

    YANG Description: Administrative distance (or preference) assigned to
routes received from different sources
(external, internal, and local).
    """
    try:
      t = YANGDynClass(v,base=default_route_distance.default_route_distance, is_container='container', yang_name="default-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_route_distance must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=default_route_distance.default_route_distance, is_container='container', yang_name="default-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)""",
        })

    self.__default_route_distance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_route_distance(self):
    self.__default_route_distance = YANGDynClass(base=default_route_distance.default_route_distance, is_container='container', yang_name="default-route-distance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)


  def _get_confederation(self):
    """
    Getter method for confederation, mapped from YANG variable /bgp/global/confederation (container)

    YANG Description: Parameters indicating whether the local system acts as part
of a BGP confederation
    """
    return self.__confederation
      
  def _set_confederation(self, v, load=False):
    """
    Setter method for confederation, mapped from YANG variable /bgp/global/confederation (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_confederation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_confederation() directly.

    YANG Description: Parameters indicating whether the local system acts as part
of a BGP confederation
    """
    try:
      t = YANGDynClass(v,base=confederation.confederation, is_container='container', yang_name="confederation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """confederation must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=confederation.confederation, is_container='container', yang_name="confederation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)""",
        })

    self.__confederation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_confederation(self):
    self.__confederation = YANGDynClass(base=confederation.confederation, is_container='container', yang_name="confederation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)


  def _get_use_multiple_paths(self):
    """
    Getter method for use_multiple_paths, mapped from YANG variable /bgp/global/use_multiple_paths (container)

    YANG Description: Parameters related to the use of multiple paths for the
same NLRI
    """
    return self.__use_multiple_paths
      
  def _set_use_multiple_paths(self, v, load=False):
    """
    Setter method for use_multiple_paths, mapped from YANG variable /bgp/global/use_multiple_paths (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_use_multiple_paths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_use_multiple_paths() directly.

    YANG Description: Parameters related to the use of multiple paths for the
same NLRI
    """
    try:
      t = YANGDynClass(v,base=use_multiple_paths.use_multiple_paths, is_container='container', yang_name="use-multiple-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """use_multiple_paths must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=use_multiple_paths.use_multiple_paths, is_container='container', yang_name="use-multiple-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)""",
        })

    self.__use_multiple_paths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_use_multiple_paths(self):
    self.__use_multiple_paths = YANGDynClass(base=use_multiple_paths.use_multiple_paths, is_container='container', yang_name="use-multiple-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)


  def _get_graceful_restart(self):
    """
    Getter method for graceful_restart, mapped from YANG variable /bgp/global/graceful_restart (container)

    YANG Description: Parameters relating the graceful restart mechanism for BGP
    """
    return self.__graceful_restart
      
  def _set_graceful_restart(self, v, load=False):
    """
    Setter method for graceful_restart, mapped from YANG variable /bgp/global/graceful_restart (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_graceful_restart is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_graceful_restart() directly.

    YANG Description: Parameters relating the graceful restart mechanism for BGP
    """
    try:
      t = YANGDynClass(v,base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """graceful_restart must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)""",
        })

    self.__graceful_restart = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_graceful_restart(self):
    self.__graceful_restart = YANGDynClass(base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)


  def _get_afi_safis(self):
    """
    Getter method for afi_safis, mapped from YANG variable /bgp/global/afi_safis (container)

    YANG Description: Address family specific configuration
    """
    return self.__afi_safis
      
  def _set_afi_safis(self, v, load=False):
    """
    Setter method for afi_safis, mapped from YANG variable /bgp/global/afi_safis (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_safis is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_safis() directly.

    YANG Description: Address family specific configuration
    """
    try:
      t = YANGDynClass(v,base=afi_safis.afi_safis, is_container='container', yang_name="afi-safis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """afi_safis must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=afi_safis.afi_safis, is_container='container', yang_name="afi-safis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)""",
        })

    self.__afi_safis = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_afi_safis(self):
    self.__afi_safis = YANGDynClass(base=afi_safis.afi_safis, is_container='container', yang_name="afi-safis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)


  def _get_apply_policy(self):
    """
    Getter method for apply_policy, mapped from YANG variable /bgp/global/apply_policy (container)

    YANG Description: Anchor point for routing policies in the model.
Import and export policies are with respect to the local
routing table, i.e., export (send) and import (receive),
depending on the context.
    """
    return self.__apply_policy
      
  def _set_apply_policy(self, v, load=False):
    """
    Setter method for apply_policy, mapped from YANG variable /bgp/global/apply_policy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_apply_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_apply_policy() directly.

    YANG Description: Anchor point for routing policies in the model.
Import and export policies are with respect to the local
routing table, i.e., export (send) and import (receive),
depending on the context.
    """
    try:
      t = YANGDynClass(v,base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """apply_policy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)""",
        })

    self.__apply_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_apply_policy(self):
    self.__apply_policy = YANGDynClass(base=apply_policy.apply_policy, is_container='container', yang_name="apply-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='container', is_config=True)

  config = property(_get_config, _set_config)
  state = property(_get_state, _set_state)
  route_selection_options = property(_get_route_selection_options, _set_route_selection_options)
  default_route_distance = property(_get_default_route_distance, _set_default_route_distance)
  confederation = property(_get_confederation, _set_confederation)
  use_multiple_paths = property(_get_use_multiple_paths, _set_use_multiple_paths)
  graceful_restart = property(_get_graceful_restart, _set_graceful_restart)
  afi_safis = property(_get_afi_safis, _set_afi_safis)
  apply_policy = property(_get_apply_policy, _set_apply_policy)


  _pyangbind_elements = {'config': config, 'state': state, 'route_selection_options': route_selection_options, 'default_route_distance': default_route_distance, 'confederation': confederation, 'use_multiple_paths': use_multiple_paths, 'graceful_restart': graceful_restart, 'afi_safis': afi_safis, 'apply_policy': apply_policy, }


