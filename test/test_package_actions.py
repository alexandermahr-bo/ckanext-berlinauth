# encoding: utf-8

import json
import logging
import unittest
import sys
from ckanapi import RemoteCKAN, CKANAPIError

#class TestPackageActions(unittest.TestCase):
class TestPackageActions():

    def setUp(self):
        self.log = logging.getLogger( __file__ )
        self.test_result = {
            "success": [] ,
            "fail": []
        }
        self.user_agent = "ckan_auth_tester"
        self.ckan_url = "http://datenregister.local:5000"

        self.connections = {
            "user_b": RemoteCKAN(self.ckan_url, user_agent=self.user_agent, apikey="f2e78d22-58eb-4912-af2b-83aa2b3e33a8") ,
            "sysadmin": RemoteCKAN(self.ckan_url, user_agent=self.user_agent, apikey="1bc746a1-06bf-4a7b-9873-2989f099807d") ,
            "user_none": RemoteCKAN(self.ckan_url, user_agent=self.user_agent, apikey="3cbcd4cb-ecdc-4f38-b179-9ca049c58135") ,
            "user_a": RemoteCKAN(self.ckan_url, user_agent=self.user_agent, apikey="39728be6-8de2-4a9f-bb89-c9ed0ed23f3f") ,
            "anonymous": RemoteCKAN(self.ckan_url, user_agent=self.user_agent) ,
        }

        self.packages = {
            "package_noorg": {
                "name": "package_noorg" ,
                "title": "Datensatz No-Org" ,
            } ,
            "package_org_a": {
                "owner_org": "organization_a" ,
                "name": "package_org_a" ,
                "title": "Datensatz A" ,
            } ,
            "package_org_b": {
                "owner_org": "organization_b" ,
                "name": "package_org_b" ,
                "title": "Datensatz B" ,
            } ,
        }

    def _assert_equal(self, actual, expected, method_name):
        if actual == expected:
            self.log.debug("\tTest successful")
            self.test_result['success'].append(method_name)
        else:
            fail_message = "{} (actual) is not {} (expected)".format(actual, expected)
            self.log.debug("\tTest failed: {}".format(fail_message))
            self.test_result['fail'].append({ "method": method_name, "reason": fail_message})

    def test_01_01_create__noorg__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['user_b'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_01_create__noorg__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_01_02_show__noorg__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_b'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_02_show__noorg__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_01_03_update__noorg__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_b'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_03_update__noorg__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_01_04_delete__noorg__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_b'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_04_delete__noorg__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_01_05_create__org_a__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['user_b'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_05_create__org_a__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_01_06_show__org_a__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_b'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_06_show__org_a__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_01_07_update__org_a__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_b'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_07_update__org_a__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_01_08_delete__org_a__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_b'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_08_delete__org_a__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_01_09_create__org_b__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['user_b'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_09_create__org_b__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_01_10_show__org_b__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_b'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_10_show__org_b__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_01_11_update__org_b__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_b'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_11_update__org_b__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_01_12_delete__org_b__user_b(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_b'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_01_12_delete__org_b__user_b')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_01_create__noorg__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['sysadmin'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_01_create__noorg__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_02_show__noorg__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['sysadmin'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_02_show__noorg__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_03_update__noorg__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['sysadmin'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_03_update__noorg__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_04_delete__noorg__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['sysadmin'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_04_delete__noorg__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_05_create__org_a__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['sysadmin'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_05_create__org_a__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_06_show__org_a__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['sysadmin'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_06_show__org_a__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_07_update__org_a__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['sysadmin'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_07_update__org_a__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_08_delete__org_a__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['sysadmin'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_08_delete__org_a__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_09_create__org_b__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['sysadmin'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_09_create__org_b__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_10_show__org_b__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['sysadmin'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_10_show__org_b__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_11_update__org_b__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['sysadmin'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_11_update__org_b__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_02_12_delete__org_b__sysadmin(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['sysadmin'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], True)
        self._assert_equal(result['success'], True, 'test_02_12_delete__org_b__sysadmin')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_01_create__noorg__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['user_none'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_01_create__noorg__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_02_show__noorg__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_none'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_02_show__noorg__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_03_update__noorg__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_none'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_03_update__noorg__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_04_delete__noorg__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_none'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_04_delete__noorg__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_05_create__org_a__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['user_none'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_05_create__org_a__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_06_show__org_a__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_none'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_06_show__org_a__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_07_update__org_a__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_none'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_07_update__org_a__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_08_delete__org_a__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_none'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_08_delete__org_a__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_09_create__org_b__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['user_none'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_09_create__org_b__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_10_show__org_b__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_none'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_10_show__org_b__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_11_update__org_b__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_none'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_11_update__org_b__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_03_12_delete__org_b__user_none(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_none'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_03_12_delete__org_b__user_none')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_01_create__noorg__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['user_a'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_01_create__noorg__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_02_show__noorg__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_a'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_02_show__noorg__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_03_update__noorg__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_a'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_03_update__noorg__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_04_delete__noorg__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_a'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_04_delete__noorg__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_05_create__org_a__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['user_a'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_05_create__org_a__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_06_show__org_a__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_a'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_06_show__org_a__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_07_update__org_a__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_a'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_07_update__org_a__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_08_delete__org_a__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_a'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_08_delete__org_a__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_09_create__org_b__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['user_a'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_09_create__org_b__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_10_show__org_b__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_a'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_10_show__org_b__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_11_update__org_b__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_a'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_11_update__org_b__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_04_12_delete__org_b__user_a(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['user_a'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_04_12_delete__org_b__user_a')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_01_create__noorg__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['anonymous'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_01_create__noorg__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_02_show__noorg__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['anonymous'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_02_show__noorg__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_03_update__noorg__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['anonymous'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_03_update__noorg__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_04_delete__noorg__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_noorg']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['anonymous'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_04_delete__noorg__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_05_create__org_a__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['anonymous'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_05_create__org_a__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_06_show__org_a__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['anonymous'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_06_show__org_a__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_07_update__org_a__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['anonymous'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_07_update__org_a__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_08_delete__org_a__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_a']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['anonymous'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_08_delete__org_a__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_09_create__org_b__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        data['title'] = package['title']
        if 'owner_org' in package:
            data['owner_org'] = package['owner_org']
        try:
            result = self.connections['anonymous'].call_action('package_create', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_09_create__org_b__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_10_show__org_b__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['anonymous'].call_action('package_show', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_10_show__org_b__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_11_update__org_b__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['anonymous'].call_action('package_update', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_11_update__org_b__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        
    def test_05_12_delete__org_b__anonymous(self):
        self.log.setLevel( logging.DEBUG )
        self.log.debug(" start ...")
        package = self.packages['package_org_b']
        data = {
            'id': package['name']
        }
        try:
            result = self.connections['anonymous'].call_action('package_delete', data)
            result = {
                "success": True ,
                "result": result
            }
            self.log.debug("\tsuccess.")
        except CKANAPIError as e:
            print("\tException occured: {}".format(e))
            result = {
                "success": False ,
                "message": e
            }

        # self.assertEqual(result['success'], False)
        self._assert_equal(result['success'], False, 'test_05_12_delete__org_b__anonymous')
        self.log.debug(" ... done")
        self.log.debug(" -----------------------")
        

# if __name__ == '__main__':
    # logging.basicConfig( stream=sys.stderr )
    # unittest.main()

logging.basicConfig( stream=sys.stderr )
tester = TestPackageActions()
tester.setUp()

tester.test_01_01_create__noorg__user_b()
tester.test_01_02_show__noorg__user_b()
tester.test_01_03_update__noorg__user_b()
tester.test_01_04_delete__noorg__user_b()
tester.test_01_05_create__org_a__user_b()
tester.test_01_06_show__org_a__user_b()
tester.test_01_07_update__org_a__user_b()
tester.test_01_08_delete__org_a__user_b()
tester.test_01_09_create__org_b__user_b()
tester.test_01_10_show__org_b__user_b()
tester.test_01_11_update__org_b__user_b()
tester.test_01_12_delete__org_b__user_b()
tester.test_02_01_create__noorg__sysadmin()
tester.test_02_02_show__noorg__sysadmin()
tester.test_02_03_update__noorg__sysadmin()
tester.test_02_04_delete__noorg__sysadmin()
tester.test_02_05_create__org_a__sysadmin()
tester.test_02_06_show__org_a__sysadmin()
tester.test_02_07_update__org_a__sysadmin()
tester.test_02_08_delete__org_a__sysadmin()
tester.test_02_09_create__org_b__sysadmin()
tester.test_02_10_show__org_b__sysadmin()
tester.test_02_11_update__org_b__sysadmin()
tester.test_02_12_delete__org_b__sysadmin()
tester.test_03_01_create__noorg__user_none()
tester.test_03_02_show__noorg__user_none()
tester.test_03_03_update__noorg__user_none()
tester.test_03_04_delete__noorg__user_none()
tester.test_03_05_create__org_a__user_none()
tester.test_03_06_show__org_a__user_none()
tester.test_03_07_update__org_a__user_none()
tester.test_03_08_delete__org_a__user_none()
tester.test_03_09_create__org_b__user_none()
tester.test_03_10_show__org_b__user_none()
tester.test_03_11_update__org_b__user_none()
tester.test_03_12_delete__org_b__user_none()
tester.test_04_01_create__noorg__user_a()
tester.test_04_02_show__noorg__user_a()
tester.test_04_03_update__noorg__user_a()
tester.test_04_04_delete__noorg__user_a()
tester.test_04_05_create__org_a__user_a()
tester.test_04_06_show__org_a__user_a()
tester.test_04_07_update__org_a__user_a()
tester.test_04_08_delete__org_a__user_a()
tester.test_04_09_create__org_b__user_a()
tester.test_04_10_show__org_b__user_a()
tester.test_04_11_update__org_b__user_a()
tester.test_04_12_delete__org_b__user_a()
tester.test_05_01_create__noorg__anonymous()
tester.test_05_02_show__noorg__anonymous()
tester.test_05_03_update__noorg__anonymous()
tester.test_05_04_delete__noorg__anonymous()
tester.test_05_05_create__org_a__anonymous()
tester.test_05_06_show__org_a__anonymous()
tester.test_05_07_update__org_a__anonymous()
tester.test_05_08_delete__org_a__anonymous()
tester.test_05_09_create__org_b__anonymous()
tester.test_05_10_show__org_b__anonymous()
tester.test_05_11_update__org_b__anonymous()
tester.test_05_12_delete__org_b__anonymous()

with open('results.json', 'w') as outfile:
    json.dump(tester.test_result, outfile)
