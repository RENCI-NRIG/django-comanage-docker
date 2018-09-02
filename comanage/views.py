from django.shortcuts import render

from .models import IsMemberOf, LdapOther


def ldap_attributes(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
    else:
        user_id = 0
    ismemberof = IsMemberOf.objects.filter(membershipismemberof__user_id=user_id).order_by('value')
    ldapother = LdapOther.objects.filter(membershipldapother__user_id=user_id).order_by('attribute', 'value')
    return render(request, 'login.html', {'isMemberOf': ismemberof, 'LDAPOther': ldapother})


def group_list(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
    else:
        user_id = 0
    membership = IsMemberOf.objects.filter(membershipismemberof__user_id=user_id).order_by('value')
    return render(request, 'login.html', {'isMemberOf': membership})


def ldap_other_list(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
    else:
        user_id = 0
    membership = LdapOther.objects.filter(membershipldapother__user_id=user_id).order_by('attribute', 'value')
    return render(request, 'login.html', {'LDAPOther': membership})
