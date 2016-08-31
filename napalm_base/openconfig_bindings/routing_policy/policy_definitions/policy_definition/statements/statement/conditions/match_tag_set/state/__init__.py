
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-tag-set/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data tag-set conditions
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__tag_set','__match_set_options',)

  _yang_name = 'state'

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
    self.__match_set_options = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INVERT': {}, u'ANY': {}},), default=unicode("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=False)
    self.__tag_set = YANGDynClass(base=ReferenceType(referenced_path='/routing-policy/defined-sets/tag-sets/tag-set/tag-set-name', caller=self._path() + ['tag-set'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=False)

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
      return [u'routing-policy', u'policy-definitions', u'policy-definition', u'statements', u'statement', u'conditions', u'match-tag-set', u'state']

  def _get_tag_set(self):
    """
    Getter method for tag_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_tag_set/state/tag_set (leafref)

    YANG Description: References a defined tag set
    """
    return self.__tag_set
      
  def _set_tag_set(self, v, load=False):
    """
    Setter method for tag_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_tag_set/state/tag_set (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tag_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tag_set() directly.

    YANG Description: References a defined tag set
    """
    try:
      t = YANGDynClass(v,base=ReferenceType(referenced_path='/routing-policy/defined-sets/tag-sets/tag-set/tag-set-name', caller=self._path() + ['tag-set'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tag_set must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=ReferenceType(referenced_path='/routing-policy/defined-sets/tag-sets/tag-set/tag-set-name', caller=self._path() + ['tag-set'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=False)""",
        })

    self.__tag_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tag_set(self):
    self.__tag_set = YANGDynClass(base=ReferenceType(referenced_path='/routing-policy/defined-sets/tag-sets/tag-set/tag-set-name', caller=self._path() + ['tag-set'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=False)


  def _get_match_set_options(self):
    """
    Getter method for match_set_options, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_tag_set/state/match_set_options (oc-pol-types:match-set-options-restricted-type)

    YANG Description: Optional parameter that governs the behaviour of the
match operation.  This leaf only supports matching on ANY
member of the set or inverting the match.  Matching on ALL is
not supported)
    """
    return self.__match_set_options
      
  def _set_match_set_options(self, v, load=False):
    """
    Setter method for match_set_options, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_tag_set/state/match_set_options (oc-pol-types:match-set-options-restricted-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match_set_options is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match_set_options() directly.

    YANG Description: Optional parameter that governs the behaviour of the
match operation.  This leaf only supports matching on ANY
member of the set or inverting the match.  Matching on ALL is
not supported)
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INVERT': {}, u'ANY': {}},), default=unicode("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match_set_options must be of a type compatible with oc-pol-types:match-set-options-restricted-type""",
          'defined-type': "oc-pol-types:match-set-options-restricted-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INVERT': {}, u'ANY': {}},), default=unicode("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=False)""",
        })

    self.__match_set_options = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match_set_options(self):
    self.__match_set_options = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INVERT': {}, u'ANY': {}},), default=unicode("ANY"), is_leaf=True, yang_name="match-set-options", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='oc-pol-types:match-set-options-restricted-type', is_config=False)

  tag_set = property(_get_tag_set)
  match_set_options = property(_get_match_set_options)


  _pyangbind_elements = {'tag_set': tag_set, 'match_set_options': match_set_options, }


