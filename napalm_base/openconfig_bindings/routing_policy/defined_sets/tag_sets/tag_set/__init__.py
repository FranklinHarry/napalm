
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import config
import state
class tag_set(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/defined-sets/tag-sets/tag-set. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of tag set definitions.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__tag_set_name','__config','__state',)

  _yang_name = 'tag-set'

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
    self.__tag_set_name = YANGDynClass(base=ReferenceType(referenced_path='../config/tag-set-name', caller=self._path() + ['tag-set-name'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="tag-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

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
      return [u'routing-policy', u'defined-sets', u'tag-sets', u'tag-set']

  def _get_tag_set_name(self):
    """
    Getter method for tag_set_name, mapped from YANG variable /routing_policy/defined_sets/tag_sets/tag_set/tag_set_name (leafref)

    YANG Description: Reference to the tag set name list key
    """
    return self.__tag_set_name
      
  def _set_tag_set_name(self, v, load=False):
    """
    Setter method for tag_set_name, mapped from YANG variable /routing_policy/defined_sets/tag_sets/tag_set/tag_set_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tag_set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tag_set_name() directly.

    YANG Description: Reference to the tag set name list key
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=ReferenceType(referenced_path='../config/tag-set-name', caller=self._path() + ['tag-set-name'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="tag-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tag_set_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=ReferenceType(referenced_path='../config/tag-set-name', caller=self._path() + ['tag-set-name'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="tag-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)""",
        })

    self.__tag_set_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tag_set_name(self):
    self.__tag_set_name = YANGDynClass(base=ReferenceType(referenced_path='../config/tag-set-name', caller=self._path() + ['tag-set-name'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="tag-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /routing_policy/defined_sets/tag_sets/tag_set/config (container)

    YANG Description: Configuration data for tag sets
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /routing_policy/defined_sets/tag_sets/tag_set/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for tag sets
    """
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /routing_policy/defined_sets/tag_sets/tag_set/state (container)

    YANG Description: Operational state data for tag sets
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /routing_policy/defined_sets/tag_sets/tag_set/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for tag sets
    """
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

  tag_set_name = property(_get_tag_set_name, _set_tag_set_name)
  config = property(_get_config, _set_config)
  state = property(_get_state, _set_state)


  _pyangbind_elements = {'tag_set_name': tag_set_name, 'config': config, 'state': state, }


