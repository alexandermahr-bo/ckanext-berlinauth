# encoding: utf-8

# This is auto-generated code!

import logging
import ckan.plugins as plugins
import ckan.model as model
from ckan.common import c

log = logging.getLogger(__name__)


def activity_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def bulk_update_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def bulk_update_private(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def bulk_update_public(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def config_option_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def config_option_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def config_option_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def current_package_list_with_resources(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def dashboard_activity_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def dashboard_mark_activities_old(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def dashboard_mark_activities_old(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def dashboard_new_activities_count(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def dataset_followee_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def dataset_follower_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def dataset_purge(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def file_upload(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def followee_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def format_autocomplete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def get_site_user(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_autocomplete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_change_state(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_change_state(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_create_rest(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_edit_permissions(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_edit_permissions(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_followee_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_follower_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

@plugins.toolkit.auth_allow_anonymous_access
def group_list(context, data_dict=None):
  return { 'success': True }

@plugins.toolkit.auth_allow_anonymous_access
def group_list_authz(context, data_dict=None):
  return { 'success': True }

def group_list_available(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_member_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_member_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_patch(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_purge(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_revision_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_show_rest(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def group_update_rest(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def help_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def job_cancel(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def job_clear(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def job_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def job_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def license_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def member_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def member_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def member_roles_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_autocomplete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_followee_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_follower_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_list_for_user(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_member_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_member_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_patch(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_purge(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_revision_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def organization_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_autocomplete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_change_state(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_change_state(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_create_default_resource_views(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_create_rest(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

@plugins.toolkit.auth_allow_anonymous_access
def package_list(context, data_dict=None):
  return { 'success': True }

def package_owner_org_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_patch(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_relationship_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_relationship_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_relationship_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_relationship_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_relationships_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_resource_reorder(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_resource_reorder(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_revision_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

@plugins.toolkit.auth_allow_anonymous_access
def package_search(context, data_dict=None):
  return { 'success': True }

@plugins.toolkit.auth_allow_anonymous_access
def package_show(context, data_dict=None):
  return { 'success': True }

def package_show_rest(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def package_update_rest(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def rating_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def request_reset(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_create_default_resource_views(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_patch(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

@plugins.toolkit.auth_allow_anonymous_access
def resource_show(context, data_dict=None):
  return { 'success': True }

def resource_status_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_view_clear(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_view_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_view_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

@plugins.toolkit.auth_allow_anonymous_access
def resource_view_list(context, data_dict=None):
  return { 'success': True }

def resource_view_reorder(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_view_reorder(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_view_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_view_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def resource_view_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def revision_change_state(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def revision_change_state(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def revision_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def revision_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def revision_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def revision_undelete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def send_email_notifications(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

@plugins.toolkit.auth_allow_anonymous_access
def site_read(context, data_dict=None):
  return { 'success': True }

def sysadmin(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def tag_autocomplete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def tag_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def tag_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def tag_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def tag_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def tag_show_rest(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def task_status_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def task_status_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def task_status_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def task_status_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def term_translation_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def term_translation_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_autocomplete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_followee_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_follower_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_generate_apikey(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_generate_apikey(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_invite(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_reset(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def user_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def vocabulary_create(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def vocabulary_delete(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def vocabulary_list(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def vocabulary_show(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def vocabulary_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

def vocabulary_update(context, data_dict=None):
  return { 'success': c.userobj.sysadmin }

class BerlinauthPlugin(plugins.SingletonPlugin):
  plugins.implements(plugins.IAuthFunctions)
  
  def get_auth_functions(self):
    return {
      'activity_create': activity_create ,
      'bulk_update_delete': bulk_update_delete ,
      'bulk_update_private': bulk_update_private ,
      'bulk_update_public': bulk_update_public ,
      'config_option_list': config_option_list ,
      'config_option_show': config_option_show ,
      'config_option_update': config_option_update ,
      'current_package_list_with_resources': current_package_list_with_resources ,
      'dashboard_activity_list': dashboard_activity_list ,
      'dashboard_mark_activities_old': dashboard_mark_activities_old ,
      'dashboard_mark_activities_old': dashboard_mark_activities_old ,
      'dashboard_new_activities_count': dashboard_new_activities_count ,
      'dataset_followee_list': dataset_followee_list ,
      'dataset_follower_list': dataset_follower_list ,
      'dataset_purge': dataset_purge ,
      'file_upload': file_upload ,
      'followee_list': followee_list ,
      'format_autocomplete': format_autocomplete ,
      'get_site_user': get_site_user ,
      'group_autocomplete': group_autocomplete ,
      'group_change_state': group_change_state ,
      'group_change_state': group_change_state ,
      'group_create': group_create ,
      'group_create_rest': group_create_rest ,
      'group_delete': group_delete ,
      'group_edit_permissions': group_edit_permissions ,
      'group_edit_permissions': group_edit_permissions ,
      'group_followee_list': group_followee_list ,
      'group_follower_list': group_follower_list ,
      'group_list': group_list ,
      'group_list_authz': group_list_authz ,
      'group_list_available': group_list_available ,
      'group_member_create': group_member_create ,
      'group_member_delete': group_member_delete ,
      'group_patch': group_patch ,
      'group_purge': group_purge ,
      'group_revision_list': group_revision_list ,
      'group_show': group_show ,
      'group_show_rest': group_show_rest ,
      'group_update': group_update ,
      'group_update': group_update ,
      'group_update_rest': group_update_rest ,
      'help_show': help_show ,
      'job_cancel': job_cancel ,
      'job_clear': job_clear ,
      'job_list': job_list ,
      'job_show': job_show ,
      'license_list': license_list ,
      'member_create': member_create ,
      'member_delete': member_delete ,
      'member_roles_list': member_roles_list ,
      'organization_autocomplete': organization_autocomplete ,
      'organization_create': organization_create ,
      'organization_delete': organization_delete ,
      'organization_followee_list': organization_followee_list ,
      'organization_follower_list': organization_follower_list ,
      'organization_list': organization_list ,
      'organization_list_for_user': organization_list_for_user ,
      'organization_member_create': organization_member_create ,
      'organization_member_delete': organization_member_delete ,
      'organization_patch': organization_patch ,
      'organization_purge': organization_purge ,
      'organization_revision_list': organization_revision_list ,
      'organization_show': organization_show ,
      'organization_update': organization_update ,
      'organization_update': organization_update ,
      'package_autocomplete': package_autocomplete ,
      'package_change_state': package_change_state ,
      'package_change_state': package_change_state ,
      'package_create': package_create ,
      'package_create_default_resource_views': package_create_default_resource_views ,
      'package_create_rest': package_create_rest ,
      'package_delete': package_delete ,
      'package_list': package_list ,
      'package_owner_org_update': package_owner_org_update ,
      'package_patch': package_patch ,
      'package_relationship_create': package_relationship_create ,
      'package_relationship_delete': package_relationship_delete ,
      'package_relationship_update': package_relationship_update ,
      'package_relationship_update': package_relationship_update ,
      'package_relationships_list': package_relationships_list ,
      'package_resource_reorder': package_resource_reorder ,
      'package_resource_reorder': package_resource_reorder ,
      'package_revision_list': package_revision_list ,
      'package_search': package_search ,
      'package_show': package_show ,
      'package_show_rest': package_show_rest ,
      'package_update': package_update ,
      'package_update': package_update ,
      'package_update_rest': package_update_rest ,
      'rating_create': rating_create ,
      'request_reset': request_reset ,
      'resource_create': resource_create ,
      'resource_create_default_resource_views': resource_create_default_resource_views ,
      'resource_delete': resource_delete ,
      'resource_patch': resource_patch ,
      'resource_show': resource_show ,
      'resource_status_show': resource_status_show ,
      'resource_update': resource_update ,
      'resource_update': resource_update ,
      'resource_view_clear': resource_view_clear ,
      'resource_view_create': resource_view_create ,
      'resource_view_delete': resource_view_delete ,
      'resource_view_list': resource_view_list ,
      'resource_view_reorder': resource_view_reorder ,
      'resource_view_reorder': resource_view_reorder ,
      'resource_view_show': resource_view_show ,
      'resource_view_update': resource_view_update ,
      'resource_view_update': resource_view_update ,
      'revision_change_state': revision_change_state ,
      'revision_change_state': revision_change_state ,
      'revision_delete': revision_delete ,
      'revision_list': revision_list ,
      'revision_show': revision_show ,
      'revision_undelete': revision_undelete ,
      'send_email_notifications': send_email_notifications ,
      'site_read': site_read ,
      'sysadmin': sysadmin ,
      'tag_autocomplete': tag_autocomplete ,
      'tag_create': tag_create ,
      'tag_delete': tag_delete ,
      'tag_list': tag_list ,
      'tag_show': tag_show ,
      'tag_show_rest': tag_show_rest ,
      'task_status_delete': task_status_delete ,
      'task_status_show': task_status_show ,
      'task_status_update': task_status_update ,
      'task_status_update': task_status_update ,
      'term_translation_update': term_translation_update ,
      'term_translation_update': term_translation_update ,
      'user_autocomplete': user_autocomplete ,
      'user_create': user_create ,
      'user_delete': user_delete ,
      'user_followee_list': user_followee_list ,
      'user_follower_list': user_follower_list ,
      'user_generate_apikey': user_generate_apikey ,
      'user_generate_apikey': user_generate_apikey ,
      'user_invite': user_invite ,
      'user_list': user_list ,
      'user_reset': user_reset ,
      'user_show': user_show ,
      'user_update': user_update ,
      'user_update': user_update ,
      'vocabulary_create': vocabulary_create ,
      'vocabulary_delete': vocabulary_delete ,
      'vocabulary_list': vocabulary_list ,
      'vocabulary_show': vocabulary_show ,
      'vocabulary_update': vocabulary_update ,
      'vocabulary_update': vocabulary_update ,
    }

