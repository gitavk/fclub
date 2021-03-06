from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.main_menu'),
    url(r'^reference/$', 'core.views.reference'),
    url(r'^reports/', include('reports.urls')),

    url(r'^employees/$', 'employees.views.employees', name='employees'),
    url(r'^employees/departmentposions/$', 'employees.views.departmentposions', name='e_departmentposions'),
    
    url(r'^employees/timetable/(?P<year>\d+)/(?P<week>\d+)/(?P<act>\w+)$', 'employees.views.timetable', name='e_timetable'),
    url(r'^employees/visits/(\d+)/$', 'employees.views.visits', name='e_visits'),

    url(r'^employees/timetable/shift$', 'employees.views.shift', name='e_shift'),

    url(r'^employees/note/(\d+)/$', 'employees.views.note', name='e_note'),
    url(r'^employees/online/$', 'employees.views.online', name='e_online'),
    url(r'^employees/comein/(\d+)/$', 'employees.views.comein', name='e_comein'),
    url(r'^employees/card/(\d+)/$', 'employees.views.employee_card', name='e_card'),
    url(r'^employees/change_work/(\d+)/$', 'employees.views.change_work', name='change_work'),
    url(r'^employees/dismiss/$', 'employees.views.dismiss', name='dismiss'),

    url(r'^employees/view/$', 'employees.views.employees', {'act': 'view'},
                            name='e_view'),
    url(r'^employees/add/$', 'employees.views.employees', {'act': 'add'},
                            name='employees_add'),
    url(r'^employees/edit/(\d+)/$', 'employees.views.employees', {'act': 'edit'},
                            name='employees_edit'),
    url(r'^employees/del/(\d+)/$', 'employees.views.employees', {'act': 'del'},
                            name='employees_del'),

    url(r'^employees/department/$', 'employees.views.department', name='department'),
    url(r'^employees/department/add/$', 'employees.views.department', {'act': 'add'},
                            name='department_add'),
    url(r'^employees/department/edit/(\d+)/$', 'employees.views.department', {'act': 'edit'},
                            name='department_edit'),
    url(r'^employees/department/del/(\d+)/$', 'employees.views.department', {'act': 'del'},
                            name='department_del'),

    url(r'^employees/position/$', 'employees.views.position', name='position'),
    url(r'^employees/position/add/$', 'employees.views.position', {'act': 'add'},
                            name='position_add'),
    url(r'^employees/position/edit/(\d+)/$', 'employees.views.position', {'act': 'edit'},
                            name='position_edit'),
    url(r'^employees/position/del/(\d+)/$', 'employees.views.position', {'act': 'del'},
                            name='position_del'),

    url(r'^credit/$', 'finance.views.credit', name='credit'),
    url(r'^credit/(\d+)/$', 'finance.views.credit', name='clnt_credit'),
    url(r'^credit/client/(\d+)/$', 'finance.views.credit', {'b_url': 'person_card'},
                                        name='p_clnt_credit'),
    url(r'^credit/guest/(\d+)/$', 'finance.views.credit', {'b_url': 'r_guest_card'},
                                        name='guest_credit'),
    url(r'^credit/close/$', 'finance.views.close_credit', name='close_credit'),
    url(r'^credit/esc_credit/$', 'finance.views.esc_credit', name='esc_credit'),

    url(r'^reception/$', 'reception.views.reception_menu', name='r_menu'),
    url(r'^reception/clientinvite/$', 'reception.views.clientinvite', 
                                        name='clientinvite'),
    url(r'^reception/prolongation/(\d+)$', 'person.views.prolongation', {'act': 'guest'},
                                        name='p_guest'),
    url(r'^reception/guest/$', 'reception.views.guest', name='r_guest'),
    url(r'^reception/guest/(\d+)/$', 'reception.views.guest', name='r_guest'),
    url(r'^reception/guest/card/(\d+)/$', 'reception.views.guest_card',
                                                name='r_guest_card'),
    url(r'^reception/guest/visit/(\d+)/$', 'reception.views.guest_visit',
                                                name='r_guest_visit'),
    url(r'^reception/guest/(\d+)/inout/$', 'reception.views.guest_card',
                            {'act': 'inout'}, name='r_inout'),

    url(r'^reception/guest/add/$', 'reception.views.guest', {'act': 'add'}, 
                                                name='r_guest_add'),
    url(r'^reception/online/$', 'reception.views.clients_online', name='online'),
    url(r'^reception/reminder/$', 'reception.views.reminder', name='reminder'),
    url(r'^reception/reminder/add/$', 'reception.views.reminder', {'act': 'add'},
                                                name='reminder_add'),
    url(r'^reception/reminder/del/(\d+)/$', 'reception.views.reminder', {'act': 'del'},
                                                name='reminder_del'),
    url(r'^reception/reminder/read/(\d+)/$', 'reception.views.reminder', {'act': 'read'},
                                                name='reminder_read'),

    url(r'^reception/bithday/$', 'reception.views.bithday', name='bithday'),
    url(r'^reception/cashier/$', 'reception.views.cashier', name='cashier'),
    url(r'^reception/login/$', 'reception.views.clients_login', name='client_login'),

    url(r'^ptt/$', 'finance.views.ptt', {'act': None}, name='ptt'),
    url(r'^ptt/card/(\d+)/$', 'finance.views.ptt_card', name='ptt_card'),
    url(r'^ptt/trainer/$', 'finance.views.ptt_trainer', name='ptt_trainer'),
    url(r'^ptt/add/$', 'finance.views.ptt', {'act': 'add'}, name='ptt_add'),
    url(r'^ptt/edit/(\d+)/$', 'finance.views.ptt', {'act': 'edit'}, name='ptt_edit'),
    url(r'^ptt/del/(\d+)/$', 'finance.views.ptt', {'act': 'del'}, name='ptt_del'),

    url(r'^guest/hasinvite/(\d+)$', 'finance.views.hasitinvite', {'act': 'guest'},
                                        name='g_hasitinvite'),
    url(r'^person/hasinvite/(\d+)$', 'finance.views.hasitinvite', {'act': 'client'},
                                        name='c_hasitinvite'),

    url(r'^service/$', 'finance.views.service',
                                        {'act': None}, name='service'),
    url(r'^service/add/$', 'finance.views.service',
                                        {'act': 'add'}, name='service_add'),
    url(r'^service/edit/(\d+)/$', 'finance.views.service',
                                        {'act': 'edit'}, name='service_edit'),
    url(r'^service/del/(\d+)/$', 'finance.views.service',
                                        {'act': 'del'}, name='service_del'),

    url(r'^organizer/$', 'organizer.views.organizer_menu',name='o_menu'),
    url(r'^organizer/(\d+)/$', 'organizer.views.organizer_menu',name='o_menu'),
    url(r'^organizer/guest/$', 'organizer.views.guest', {'act': None}, name='o_guest'),
    url(r'^organizer/guest/edit/(\d+)/$', 'organizer.views.guest', 
                                        {'act': 'edit'}, name='o_guest_edit'),
    url(r'^organizer/note/$', 'organizer.views.note', name='o_note'),
    url(r'^organizer/note/(\d+)/$', 'organizer.views.note', name='o_note_read'),
    url(r'^organizer/note/me/$', 'organizer.views.note_list', name='o_note_list'),
    url(r'^organizer/note/me/all/$', 'organizer.views.note_list', {'full':1},
                                        name='o_note_list_all'),
    url(r'^organizer/note/my/$', 'organizer.views.note_list', {'my':1}, 
                                        name='o_note_my'),
    url(r'^organizer/note/my/all/$', 'organizer.views.note_list', {'my':1, 'full':1},
                                        name='o_note_my_all'),

    url(r'^market/$', 'finance.views.market', name='market'),
    url(r'^market/goods/$', 'finance.views.market_goods', name='market_goods'),
    url(r'^market/add/$', 'finance.views.market', {'act': 'add'}, name='market_add'),
    url(r'^market/edit/(\d+)/$', 'finance.views.market', {'act': 'edit'}, name='market_edit'),
    url(r'^market/del/(\d+)/$', 'finance.views.market', {'act': 'del'}, name='market_del'),
    url(r'^market/view/(\d+)/$', 'finance.views.market', {'act': 'view'}, name='market_view'),

    url(r'^warehouse/$', 'finance.views.warehouse', name='warehouse'),
    url(r'^warehouse/invoice/$', 'finance.views.invoice', {'act': None}, name='invoice'),
    url(r'^warehouse/invoice/add/$', 'finance.views.invoice', {'act': 'add'},
                                        name='invoice_add'),
    url(r'^warehouse/invoice/edit/(\d+)/$', 'finance.views.invoice', {'act': 'edit'},
                                        name='invoice_edit'),
    url(r'^warehouse/invoice/del/$', 'finance.views.invoice', {'act': 'del'},
                                        name='invoice_del'),

    url(r'^warehouse/trash/$', 'finance.views.trash', {'act': None}, name='trash'),
    url(r'^warehouse/trash/add/$', 'finance.views.trash', {'act': 'add'},
                                        name='trash_add'),
    url(r'^warehouse/trash/edit/(\d+)/$', 'finance.views.trash', {'act': 'edit'},
                                        name='trash_edit'),
    url(r'^warehouse/trash/del/$', 'finance.views.trash', {'act': 'del'},
                                        name='trash_del'),
    url(r'^warehouse/trash/g_del/$', 'finance.views.trash_goods_del',
                                        name='trash_g_del'),
    url(r'^warehouse/issuance/$', 'finance.views.issuance', {'act': None}, name='issuance'),
    url(r'^warehouse/issuance/add/$', 'finance.views.issuance', {'act': 'add'},
                                        name='issuance_add'),

    url(r'^warehouse/issuance/del/$', 'finance.views.issuance', {'act': 'del'},
                                        name='issuance_del'),

    url(r'^warehouse/issuance/edit/(\d+)/$', 'finance.views.issuance', {'act': 'edit'},
                                        name='issuance_edit'),
    url(r'^warehouse/goods/$','finance.views.warehouse_goods',name='warehouse_goods'),

    url(r'^fin/$','finance.views.fin_menu',name='fin_menu'),

    url(r'^products/menu/$','finance.views.products_menu',name='products_menu'),
    url(r'^products/goodsbcode/$','finance.views.goods_bar_code',name='p_bar_code'),
    url(r'^products/goods_type/$','finance.views.goods_type',
                                        {'act': None}, name='goods_type'),
    url(r'^products/goods_type/add/$','finance.views.goods_type',
                                        {'act': 'add'}, name='goods_type_add'),
    url(r'^products/goods_type/edit/(\d+)/$','finance.views.goods_type',
                                        {'act': 'edit'}, name='goods_type_edit'),
    url(r'^products/goods_type/del/(\d+)/$','finance.views.goods_type',
                                        {'act': 'del'}, name='goods_type_del'),
    url(r'^products/goods/$','finance.views.goods',
                                        {'act': None}, name='goods'),
    url(r'^products/goods/add/$','finance.views.goods',
                                        {'act': 'add'}, name='goods_add'),
    url(r'^products/goods/edit/(\d+)/$','finance.views.goods',
                                        {'act': 'edit'}, name='goods_edit'),
    url(r'^products/goods/del/(\d+)/$','finance.views.goods',
                                        {'act': 'del'}, name='goods_del'),
    url(r'^products/measure/$','finance.views.measure',
                                        {'act': None}, name='measure'),
    url(r'^products/measure/add/$','finance.views.measure',
                                        {'act': 'add'}, name='measure_add'),
    url(r'^products/measure/edit/(\d+)/$','finance.views.measure',
                                        {'act': 'edit'}, name='measure_edit'),
    url(r'^products/measure/del/(\d+)/$','finance.views.measure',
                                        {'act': 'del'}, name='measure_del'),
    url(r'^products/provider/$','finance.views.provider', {'act': None}, name='provider'),
    url(r'^products/provider/add/$','finance.views.provider',
                                        {'act': 'add'}, name='provider_add'),
    url(r'^products/provider/edit/(\d+)/$','finance.views.provider',
                                        {'act': 'edit'}, name='provider_edit'),
    url(r'^products/provider/goods/(\d+)/$','finance.views.provider_goods',
                                         name='provider_goods'),

    url(r'^person/$', 'person.views.person_menu', {'act': None}, name='p_menu'),
    url(r'^person/search/$', 'person.views.search', name='p_search'),
    url(r'^person/active/$', 'person.views.person_menu',
                            {'act': 'active'}, name='p_active'),
    url(r'^person/inactive/$', 'person.views.person_menu',
                            {'act': 'inactive'}, name='p_inactive'),
    url(r'^person/(\d+)/$', 'person.views.person_menu', {'act': None}, name='p_menu'),
    url(r'^person/active/(\d+)/$', 'person.views.person_menu',
                            {'act': 'active'}, name='p_active'),
    url(r'^person/inactive/(\d+)/$', 'person.views.person_menu',
                            {'act': 'inactive'}, name='p_inactive'),
    url(r'^person/add$', 'person.views.person_add'),
    url(r'^person/prolongation/(\d+)$', 'person.views.prolongation',name='prolongation'),
    url(r'^person/ptt/(\d+)$', 'person.views.client_ptt',name='client_ptt'),
    url(r'^person/card/(\d+)/$', 'person.views.person_card',{'act': None},name='person_card'),
    url(r'^person/photo/(\d+)/$', 'person.views.photo', name='person_photo'),
    url(r'^person/note/(\d+)/$', 'person.views.client_note', name='person_note'),
    url(r'^person/(\d+)/inout/$', 'person.views.person_card',{'act': 'inout'},name='inout'),
    url(r'^person/(\d+)/change_m/$', 'person.views.person_card',{'act': 'change_m'},name='change_m'),
    url(r'^person/(\d+)/(\d+)/$', 'person.views.person_contract', name='pers_cont'),
    url(r'^person/edit/(\d+)/$', 'person.views.person_edit', name='person_edit'),

    url(r'^contract/$', 'contract.views.contract_menu',name='c_menu'),
    url(r'^contract/data/(\d+)/$', 'contract.views.contract_data',name='c_data'),
    url(r'^contract/exchange/(\d+)/$', 'contract.views.exchange',name='c_exchange'),
    url(r'^contract/vdel/(\d+)/$', 'contract.views.visit_del',name='visitdel'),
    url(r'^contract/freeze/(\d+)/$', 'contract.views.contract_freeze',name='contractfreeze'),

    url(r'^contract/freeze_pay/(\d+)/$', 'contract.views.contract_pay_freeze',name='contract_pay_freeze'),

    url(r'^contract/bonus/(\d+)/$', 'contract.views.bonus',name='c_bonus'),
    url(r'^contract/ban/(\d+)/$', 'contract.views.ban',name='c_ban'),
    url(r'^contract/card/(\d+)/$', 'contract.views.card',name='c_card'),
    url(r'^contract/date_start/(\d+)/$', 'contract.views.date_start',name='c_date_start'),
    url(r'^contract/print/(\d+)/$', 'contract.views.print_contract'),
    url(r'^contract/type$', 'contract.views.contract_type', {'act': None}, name='ctype'),
    url(r'^contract/type/all$', 'contract.views.contract_type', {'act': 'all'}, name='ctypeall'),
    url(r'^contract/type/add$', 'contract.views.contract_type', {'act': 'add'}, name='ctypeadd'),
    url(r'^contract/type/edit/(\d+)/$', 'contract.views.contract_type_edit', {'act': None }, name='editcontractt'),
    url(r'^contract/type/hide/(\d+)/$', 'contract.views.contract_type_edit', {'act': 'hide'}, name='hidecontractt'),
    url(r'^contract/type/active/(\d+)/$', 'contract.views.contract_type_edit', {'act': 'active'}, name='activecontractt'),
    url(r'^contract/text$', 'contract.views.contract_text'),
    url(r'^contract/discount$', 'contract.views.contract_discount', {'act': None}, name='discount'),
    url(r'^contract/discountadd$', 'contract.views.contract_discount', {'act': 'add'}, name='discountadd'),
    url(r'^contract/discount/del/$', 'contract.views.contract_discount', {'act': 'del'},
                                        name='discount_del'),
    url(r'^contract/pay_plan$', 'contract.views.pay_plan', {'act': None}, name='pay_plan'),
    url(r'^contract/pay_planadd$', 'contract.views.pay_plan', {'act': 'add'}, name='pay_planadd'),
    url(r'^contract/period$', 'contract.views.contract_period', {'act': None}, name='period'),
    url(r'^contract/periodadd$', 'contract.views.contract_period', {'act': 'add'}, name='periodadd'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page' : '/'} ),
)

if settings.DEBUG:
    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)