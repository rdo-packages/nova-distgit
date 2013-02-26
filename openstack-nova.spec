%global with_doc %{!?_without_doc:1}%{?_without_doc:0}

Name:             openstack-nova
Version:          2013.1
Release:          0.7.g3%{?dist}
Summary:          OpenStack Compute (nova)

Group:            Applications/System
License:          ASL 2.0
URL:              http://openstack.org/projects/compute/
Source0:          https://launchpad.net/nova/grizzly/grizzly-3/+download/nova-2013.1.g3.tar.gz

Source1:          nova.conf
Source3:          nova-tgt.conf
Source6:          nova.logrotate

Source10:         openstack-nova-api.service
Source11:         openstack-nova-cert.service
Source12:         openstack-nova-compute.service
Source13:         openstack-nova-network.service
Source14:         openstack-nova-objectstore.service
Source15:         openstack-nova-scheduler.service
Source18:         openstack-nova-xvpvncproxy.service
Source19:         openstack-nova-console.service
Source20:         openstack-nova-consoleauth.service
Source25:         openstack-nova-metadata-api.service
Source26:         openstack-nova-conductor.service
Source27:         openstack-nova-cells.service
Source28:         openstack-nova-spicehtml5proxy.service

Source21:         nova-polkit.pkla
Source23:         nova-polkit.rules
Source22:         nova-ifc-template
Source24:         nova-sudoers

#
# patches_base=2013.1.g3
#
Patch0001: 0001-Ensure-we-don-t-access-the-net-when-building-docs.patch

BuildArch:        noarch
BuildRequires:    intltool
BuildRequires:    python-sphinx
BuildRequires:    python-setuptools
BuildRequires:    python-netaddr
BuildRequires:    openstack-utils

Requires:         openstack-nova-compute = %{version}-%{release}
Requires:         openstack-nova-cert = %{version}-%{release}
Requires:         openstack-nova-scheduler = %{version}-%{release}
Requires:         openstack-nova-api = %{version}-%{release}
Requires:         openstack-nova-network = %{version}-%{release}
Requires:         openstack-nova-objectstore = %{version}-%{release}
Requires:         openstack-nova-conductor = %{version}-%{release}
Requires:         openstack-nova-console = %{version}-%{release}
Requires:         openstack-nova-cells = %{version}-%{release}


%description
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

%package common
Summary:          Components common to all OpenStack Nova services
Group:            Applications/System

Requires:         python-nova = %{version}-%{release}

Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units
Requires(pre):    shadow-utils

%description common
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains scripts, config and dependencies shared
between all the OpenStack nova services.


%package compute
Summary:          OpenStack Nova Virtual Machine control service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}
Requires:         curl
Requires:         iscsi-initiator-utils
Requires:         iptables iptables-ipv6
Requires:         vconfig
Requires:         python-libguestfs
Requires:         libvirt >= 0.9.6
Requires:         libvirt-python
Requires:         openssh-clients
Requires:         rsync
Requires:         lvm2
Requires:         python-cinderclient
Requires(pre):    qemu-kvm

%description compute
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling Virtual Machines.


%package network
Summary:          OpenStack Nova Network control service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}
Requires:         vconfig
Requires:         radvd
Requires:         bridge-utils
Requires:         dnsmasq
Requires:         dnsmasq-utils

%description network
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling networking.


%package scheduler
Summary:          OpenStack Nova VM distribution service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description scheduler
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the service for scheduling where
to run Virtual Machines in the cloud.


%package cert
Summary:          OpenStack Nova certificate management service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description cert
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for managing certificates.


%package api
Summary:          OpenStack Nova API services
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description api
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing programmatic access.

%package conductor
Summary:          OpenStack Nova Conductor services
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description conductor
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing database access for
the compute service

%package objectstore
Summary:          OpenStack Nova simple object store service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description objectstore
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service providing a simple object store.


%package console
Summary:          OpenStack Nova console access services
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}
Requires:         python-websockify

%description console
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing
console access services to Virtual Machines.

%package cells
Summary:          OpenStack Nova Cells services
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description cells
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova Cells service providing additional 
scaling and (geographic) distribution for compute services.

%package -n       python-nova
Summary:          Nova Python libraries
Group:            Applications/System

Requires:         openssl
# Require openssh for ssh-keygen
Requires:         openssh
Requires:         sudo

Requires:         MySQL-python

Requires:         python-paramiko

Requires:         python-qpid
Requires:         python-kombu
Requires:         python-amqplib

Requires:         python-eventlet
Requires:         python-greenlet
Requires:         python-iso8601
Requires:         python-netaddr
Requires:         python-lxml
Requires:         python-anyjson
Requires:         python-boto
Requires:         python-cheetah
Requires:         python-ldap
Requires:         python-stevedore

Requires:         python-memcached

Requires:         python-sqlalchemy
Requires:         python-migrate

Requires:         python-paste-deploy
Requires:         python-routes
Requires:         python-webob

Requires:         python-glanceclient >= 1:0
Requires:         python-quantumclient >= 1:2
Requires:         python-novaclient
Requires:         python-oslo-config
Requires:         python-pyasn1

%description -n   python-nova
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains the nova Python library.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Compute
Group:            Documentation

Requires:         %{name} = %{version}-%{release}

BuildRequires:    systemd-units
BuildRequires:    graphviz

# Required to build module documents
BuildRequires:    python-boto
BuildRequires:    python-eventlet
BuildRequires:    python-routes
BuildRequires:    python-sqlalchemy
BuildRequires:    python-webob
# while not strictly required, quiets the build down when building docs.
BuildRequires:    python-migrate, python-iso8601

%description      doc
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains documentation files for nova.
%endif

%prep
%setup -q -n nova-%{version}.g3

%patch0001 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete

find nova -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i '/setuptools_git/d' setup.py

sed -i s/LOCALBRANCH:LOCALREVISION/%{release}/ nova/version.py

%build
%{__python} setup.py build

# Move authtoken configuration out of paste.ini
openstack-config --del etc/nova/api-paste.ini filter:authtoken admin_tenant_name
openstack-config --del etc/nova/api-paste.ini filter:authtoken admin_user
openstack-config --del etc/nova/api-paste.ini filter:authtoken admin_password
openstack-config --del etc/nova/api-paste.ini filter:authtoken auth_host
openstack-config --del etc/nova/api-paste.ini filter:authtoken auth_port
openstack-config --del etc/nova/api-paste.ini filter:authtoken auth_protocol
openstack-config --del etc/nova/api-paste.ini filter:authtoken signing_dir

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

pushd doc

%if 0%{?with_doc}
SPHINX_DEBUG=1 sphinx-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo
%endif

# Create dir link to avoid a sphinx-build exception
mkdir -p build/man/.doctrees/
ln -s .  build/man/.doctrees/man
SPHINX_DEBUG=1 sphinx-build -b man -c source source/man build/man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 build/man/*.1 %{buildroot}%{_mandir}/man1/

popd

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/buckets
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/instances
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/keys
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/networks
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/tmp
install -d -m 755 %{buildroot}%{_localstatedir}/log/nova

# Setup ghost CA cert
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 755 nova/CA/*.sh %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 644 nova/CA/openssl.cnf.tmpl %{buildroot}%{_sharedstatedir}/nova/CA
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA/{certs,crl,newcerts,projects,reqs}
touch %{buildroot}%{_sharedstatedir}/nova/CA/{cacert.pem,crl.pem,index.txt,openssl.cnf,serial}
install -d -m 750 %{buildroot}%{_sharedstatedir}/nova/CA/private
touch %{buildroot}%{_sharedstatedir}/nova/CA/private/cakey.pem

# Install config files
install -d -m 755 %{buildroot}%{_sysconfdir}/nova
install -p -D -m 640 %{SOURCE1} %{buildroot}%{_sysconfdir}/nova/nova.conf
install -d -m 755 %{buildroot}%{_sysconfdir}/nova/volumes
install -p -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/tgt/conf.d/nova.conf
install -p -D -m 640 etc/nova/rootwrap.conf %{buildroot}%{_sysconfdir}/nova/rootwrap.conf
install -p -D -m 640 etc/nova/api-paste.ini %{buildroot}%{_sysconfdir}/nova/api-paste.ini
install -p -D -m 640 etc/nova/policy.json %{buildroot}%{_sysconfdir}/nova/policy.json

# Install version info file
cat > %{buildroot}%{_sysconfdir}/nova/release <<EOF
[Nova]
vendor = Fedora Project
product = OpenStack Nova
package = %{release}
EOF

# Install initscripts for Nova services
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_unitdir}/openstack-nova-api.service
install -p -D -m 755 %{SOURCE11} %{buildroot}%{_unitdir}/openstack-nova-cert.service
install -p -D -m 755 %{SOURCE12} %{buildroot}%{_unitdir}/openstack-nova-compute.service
install -p -D -m 755 %{SOURCE13} %{buildroot}%{_unitdir}/openstack-nova-network.service
install -p -D -m 755 %{SOURCE14} %{buildroot}%{_unitdir}/openstack-nova-objectstore.service
install -p -D -m 755 %{SOURCE15} %{buildroot}%{_unitdir}/openstack-nova-scheduler.service
install -p -D -m 755 %{SOURCE18} %{buildroot}%{_unitdir}/openstack-nova-xvpvncproxy.service
install -p -D -m 755 %{SOURCE19} %{buildroot}%{_unitdir}/openstack-nova-console.service
install -p -D -m 755 %{SOURCE20} %{buildroot}%{_unitdir}/openstack-nova-consoleauth.service
install -p -D -m 755 %{SOURCE25} %{buildroot}%{_unitdir}/openstack-nova-metadata-api.service
install -p -D -m 755 %{SOURCE26} %{buildroot}%{_unitdir}/openstack-nova-conductor.service
install -p -D -m 755 %{SOURCE27} %{buildroot}%{_unitdir}/openstack-nova-cells.service
install -p -D -m 755 %{SOURCE28} %{buildroot}%{_unitdir}/openstack-nova-spicehtml5proxy.service

# Install sudoers
install -p -D -m 440 %{SOURCE24} %{buildroot}%{_sysconfdir}/sudoers.d/nova

# Install logrotate
install -p -D -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-nova

# Install pid directory
install -d -m 755 %{buildroot}%{_localstatedir}/run/nova

# Install template files
install -p -D -m 644 nova/cloudpipe/client.ovpn.template %{buildroot}%{_datarootdir}/nova/client.ovpn.template
install -p -D -m 644 %{SOURCE22} %{buildroot}%{_datarootdir}/nova/interfaces.template

# Install rootwrap files in /usr/share/nova/rootwrap
mkdir -p %{buildroot}%{_datarootdir}/nova/rootwrap/
install -p -D -m 644 etc/nova/rootwrap.d/* %{buildroot}%{_datarootdir}/nova/rootwrap/

# Older format. Remove when we no longer want to support Fedora 17 with master branch packages
install -d -m 755 %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d
install -p -D -m 644 %{SOURCE21} %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla
# Newer format since Fedora 18
install -d -m 755 %{buildroot}%{_sysconfdir}/polkit-1/rules.d
install -p -D -m 644 %{SOURCE23} %{buildroot}%{_sysconfdir}/polkit-1/rules.d/50-nova.rules

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/nova-debug
rm -fr %{buildroot}%{python_sitelib}/nova/tests/
rm -fr %{buildroot}%{python_sitelib}/run_tests.*
rm -f %{buildroot}%{_bindir}/nova-combined
rm -f %{buildroot}/usr/share/doc/nova/README*

# We currently use the equivalent file from the novnc package
rm -f %{buildroot}%{_bindir}/nova-novncproxy

%pre common
getent group nova >/dev/null || groupadd -r nova --gid 162
if ! getent passwd nova >/dev/null; then
  useradd -u 162 -r -g nova -G nova,nobody -d %{_sharedstatedir}/nova -s /sbin/nologin -c "OpenStack Nova Daemons" nova
fi
exit 0

%pre compute
usermod -a -G qemu nova
exit 0

%post compute
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post network
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post scheduler
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post cert
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post api
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post conductor
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post objectstore
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%post console
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post cells
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun compute
if [ $1 -eq 0 ] ; then
    for svc in compute; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun network
if [ $1 -eq 0 ] ; then
    for svc in network; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun scheduler
if [ $1 -eq 0 ] ; then
    for svc in scheduler; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun cert
if [ $1 -eq 0 ] ; then
    for svc in cert; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun api
if [ $1 -eq 0 ] ; then
    for svc in api metadata-api; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun objectstore
if [ $1 -eq 0 ] ; then
    for svc in objectstore; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun conductor
if [ $1 -eq 0 ] ; then
    for svc in conductor; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun console
if [ $1 -eq 0 ] ; then
    for svc in console consoleauth xvpvncproxy; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi
%preun cells
if [ $1 -eq 0 ] ; then
    for svc in cells; do
        /bin/systemctl --no-reload disable openstack-nova-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-nova-${svc}.service > /dev/null 2>&1 || :
    done
fi

%postun compute
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in compute; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun network
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in network; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun scheduler
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in scheduler; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun cert
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in cert; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun api
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in api metadata-api; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun objectstore
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in objectstore; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun conductor
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in conductor; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun console
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in console consoleauth xvpvncproxy; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi
%postun cells
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in cells; do
        /bin/systemctl try-restart openstack-nova-${svc}.service >/dev/null 2>&1 || :
    done
fi

%files
%doc LICENSE
%{_bindir}/nova-all

%files common
%doc LICENSE
%dir %{_sysconfdir}/nova
%{_sysconfdir}/nova/release
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/nova.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/api-paste.ini
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/rootwrap.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-nova
%config(noreplace) %{_sysconfdir}/sudoers.d/nova
%config(noreplace) %{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla
%config(noreplace) %{_sysconfdir}/polkit-1/rules.d/50-nova.rules

%dir %attr(0755, nova, root) %{_localstatedir}/log/nova
%dir %attr(0755, nova, root) %{_localstatedir}/run/nova

%{_bindir}/nova-clear-rabbit-queues
# TODO. zmq-receiver may need its own service?
%{_bindir}/nova-rpc-zmq-receiver
%{_bindir}/nova-manage
%{_bindir}/nova-rootwrap

%{_datarootdir}/nova
%{_mandir}/man1/nova*.1.gz

%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova
%dir %{_sharedstatedir}/nova/buckets
%dir %{_sharedstatedir}/nova/instances
%dir %{_sharedstatedir}/nova/keys
%dir %{_sharedstatedir}/nova/networks
%dir %{_sharedstatedir}/nova/tmp

%files compute
%{_bindir}/nova-compute
%{_bindir}/nova-baremetal-deploy-helper
%{_bindir}/nova-baremetal-manage
%{_unitdir}/openstack-nova-compute.service
%{_datarootdir}/nova/rootwrap/compute.filters
%config(noreplace) %{_sysconfdir}/tgt/conf.d/nova.conf

%files network
%{_bindir}/nova-network
%{_bindir}/nova-dhcpbridge
%{_unitdir}/openstack-nova-network.service
%{_datarootdir}/nova/rootwrap/network.filters

%files scheduler
%{_bindir}/nova-scheduler
%{_unitdir}/openstack-nova-scheduler.service

%files cert
%{_bindir}/nova-cert
%{_unitdir}/openstack-nova-cert.service
%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova/CA/
%dir %{_sharedstatedir}/nova/CA/certs
%dir %{_sharedstatedir}/nova/CA/crl
%dir %{_sharedstatedir}/nova/CA/newcerts
%dir %{_sharedstatedir}/nova/CA/projects
%dir %{_sharedstatedir}/nova/CA/reqs
%{_sharedstatedir}/nova/CA/*.sh
%{_sharedstatedir}/nova/CA/openssl.cnf.tmpl
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/cacert.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/crl.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/index.txt
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/openssl.cnf
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/serial
%dir %attr(0750, -, -) %{_sharedstatedir}/nova/CA/private
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/private/cakey.pem

%files api
%{_bindir}/nova-api*
%{_unitdir}/openstack-nova-*api.service
%{_datarootdir}/nova/rootwrap/api-metadata.filters

%files conductor
%{_bindir}/nova-conductor
%{_unitdir}/openstack-nova-conductor.service

%files objectstore
%{_bindir}/nova-objectstore
%{_unitdir}/openstack-nova-objectstore.service

%files console
%{_bindir}/nova-console*
%{_bindir}/nova-xvpvncproxy
%{_bindir}/nova-spicehtml5proxy
%{_unitdir}/openstack-nova-console*.service
%{_unitdir}/openstack-nova-xvpvncproxy.service
%{_unitdir}/openstack-nova-spicehtml5proxy.service

%files cells
%{_bindir}/nova-cells
%{_unitdir}/openstack-nova-cells.service

%files -n python-nova
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitelib}/nova
%{python_sitelib}/nova-%{version}*.egg-info

%if 0%{?with_doc}
%files doc
%doc LICENSE doc/build/html
%endif

%changelog
* Tue Feb 26 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.1-0.7.g3
- Fix dependency issues caused by the Milestone 3 update

* Mon Feb 25 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.1-0.6.g3
- Update to Grizzly milestone 3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.1-0.5.g2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.1-0.4.g2
- Update to Grizzly milestone 2
- Add the version info file
- Add python-stevedore dependency
- Add the cells subpackage and service file

* Thu Dec 06 2012 Nikola Đipanov <ndipanov@redhat.com> - 2013.1-0.3.g1
- signing_dir renamed from incorrect signing_dirname in default nova.conf

* Thu Nov 29 2012 Nikola Đipanov <ndipanov@redhat.com> 2013.1-0.2.g1
-Fix a few spec file issues introduced by the Grizzly update

* Wed Nov 28 2012 Nikola Đipanov <ndipanov@redhat.com> 2013.1-0.1.g1
- Update to Grizzly milestone 1
- Remove volume subpackage - removed from Grizzly
- Add the conductor subpackage - new service added in Grizzly
- Depend on python-libguestfs instead of libguestfs-mount
- Don't add the nova user to the group fuse
- Removes openstack-utils from requirements for nova-common

* Thu Sep 27 2012 Pádraig Brady <pbrady@redhat.com> - 2012.2-1
- Update to folsom final

* Wed Sep 26 2012 Pádraig Brady <pbrady@redhat.com> - 2012.2-0.11.rc1
- Support newer polkit config format to allow communication with libvirtd
- Fix to ensure that tgt configuration is honored

* Fri Sep 21 2012 Pádraig Brady <pbrady@redhat.com> - 2012.2-0.8.rc1
- Update to folsom rc1

* Mon Sep 17 2012 Alan Pevec <apevec@redhat.com> - 2012.2-0.7.f3
- Remove user config from paste ini files

* Mon Aug 27 2012 Pádraig Brady <P@draigBrady.com> - 2012.2-0.6.f3
- Update to folsom milestone 3

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.2-0.4.f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 08 2012 Pádraig Brady <P@draigBrady.com> - 2012.2-0.3.f1
- Enable libguestfs image inspection

* Wed Jun 06 2012 Pádraig Brady <P@draigBrady.com> - 2012.2-0.2.f1
- Fix up protocol case handling for security groups (CVE-2012-2654)

* Tue May 29 2012 Pádraig Brady <P@draigBrady.com> - 2012.2-0.1.f1
- Update to folsom milestone 1

* Wed May 16 2012 Alan Pevec <apevec@redhat.com> - 2012.1-6
- Remove m2crypto and other dependencies no loner needed by Essex

* Wed May 16 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-5
- Sync up with Essex stable branch
- Handle updated qemu-img info output
- Remove redundant and outdated openstack-nova-db-setup

* Wed May 09 2012 Alan Pevec <apevec@redhat.com> - 2012.1-4
- Remove the socat dependency no longer needed by Essex

* Wed Apr 27 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-3
- Reference new Essex services at installation

* Wed Apr 18 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-2
- Sync up with Essex stable branch
- Support more flexible guest image file injection
- Enforce quota on security group rules (#814275, CVE-2012-2101)
- Provide startup scripts for the Essex VNC services
- Provide a startup script for the separated metadata api service

* Sun Apr  8 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-1
- Update to Essex release

* Thu Mar 29 2012 Russell Bryant <rbryant@redhat.com> 2012.1-0.10.rc1
- Remove the outdated nova-debug tool
- CVE-2012-1585 openstack-nova: Long server names grow nova-api log files significantly

* Mon Mar 26 2012 Mark McLoughlin <markmc@redhat.com> - 2012.1-0.9.rc1
- Avoid killing dnsmasq on network service shutdown (#805947)

* Tue Mar 20 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-0.8.rc1
- Update to Essex release candidate 1

* Fri Mar 16 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-0.8.e4
- Include an upstream fix for errors logged when syncing power states
- Support non blocking libvirt operations
- Fix an exception when querying a server through the API (#803905)
- Suppress deprecation warnings with db sync at install (#801302)
- Avoid and cater for missing libvirt instance images (#801791)

* Fri Mar  6 2012 Alan Pevec <apevec@redhat.com> - 2012.1-0.7.e4
- Fixup permissions on nova config files

* Fri Mar  6 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-0.6.e4
- Depend on bridge-utils
- Support fully transparent handling of the new ini config file

* Fri Mar  2 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-0.5.e4
- Update to Essex milestone 4.
- explicitly select the libvirt firewall driver in default nova.conf.
- Add dependency on python-iso8601.
- Enable --force_dhcp_release.
- Switch to the new ini format config file.

* Mon Feb 13 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-0.4.e3
- Support --force_dhcp_release (#788485)

* Thu Feb  2 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-0.3.e3
- Suppress a warning from `nova-manage image convert`
- Add the openstack-nova-cert service which now handles the CA folder
- Change the default message broker from rabbitmq to qpid
- Enable the new rootwrap helper, to minimize sudo config

* Fri Jan 27 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-0.2.e3
- Suppress erroneous output to stdout on package install (#785115)
- Specify a connection_type in nova.conf, needed by essex-3
- Depend on python-carrot, currently needed by essex-3
- Remove the rabbitmq-server dependency as it's now optional
- Have python-nova depend on the messaging libs, not openstack-nova

* Thu Jan 26 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-0.1.e3
- Update to essex milestone 3

* Mon Jan 23 2012 Pádraig Brady <P@draigBrady.com> - 2011.3.1-2
- Fix a REST API v1.0 bug causing a regression with deltacloud

* Fri Jan 20 2012 Pádraig Brady <P@draigBrady.com> - 2011.3.1-1
- Update to 2011.3.1 release
- Allow empty mysql root password in mysql setup script
- Enable mysqld at boot in mysql setup script

* Wed Jan 18 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3.1-0.4.10818%{?dist}
- Update to latest 2011.3.1 release candidate
- Re-add nova-{clear-rabbit-queues,instance-usage-audit}

* Tue Jan 17 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3.1-0.3.10814
- nova-stack isn't missing after all

* Tue Jan 17 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3.1-0.2.10814
- nova-{stack,clear-rabbit-queues,instance-usage-audit} temporarily removed because of lp#917676

* Tue Jan 17 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3.1-0.1.10814
- Update to 2011.3.1 release candidate
- Only adds 4 patches from upstream which we didn't already have

* Wed Jan 11 2012 Pádraig Brady <P@draigBrady.com> - 2011.3-19
- Fix libguestfs support for specified partitions
- Fix tenant bypass by authenticated users using API (#772202, CVE-2012-0030)

* Fri Jan  6 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3-18
- Fix up recent patches which don't apply

* Fri Jan  6 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3-17
- Backport tgtadm off-by-one fix from upstream (#752709)

* Fri Jan  6 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3-16
- Rebase to latest upstream stable/diablo, pulling in ~50 patches

* Fri Jan  6 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3-15
- Move recent patches into git (no functional changes)

* Fri Dec 30 2011 Pádraig Brady <P@draigBrady.com> - 2011.3-14
- Don't require the fuse group (#770927)
- Require the fuse package (to avoid #767852)

* Tue Dec 14 2011 Pádraig Brady <P@draigBrady.com> - 2011.3-13
- Sanitize EC2 manifests and image tarballs (#767236, CVE 2011-4596)
- update libguestfs support

* Tue Dec 06 2011 Russell Bryant <rbryant@redhat.com> - 2011.3-11
- Add --yes, --rootpw, and --novapw options to openstack-nova-db-setup.

* Wed Nov 30 2011 Pádraig Brady <P@draigBrady.com> - 2011.3-10
- Add libguestfs support

* Tue Nov 29 2011 Pádraig Brady <P@draigBrady.com> - 2011.3-9
- Update the libvirt dependency from 0.8.2 to 0.8.7
- Ensure we don't access the net when building docs

* Tue Nov 29 2011 Russell Bryant <rbryant@redhat.com> - 2011.3-8
- Change default database to mysql. (#735012)

* Mon Nov 14 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-7
- Add ~20 significant fixes from upstream stable branch

* Wed Oct 26 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-6
- Fix password leak in EC2 API (#749385, CVE 2011-4076)

* Mon Oct 24 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-5
- Fix block migration (#741690)

* Mon Oct 17 2011 Bob Kukura <rkukura@redhat.com> - 2011.3-4
- Add dependency on python-amqplib (#746685)

* Wed Sep 28 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-3
- Fix lazy load exception with security groups (#741307)
- Fix issue with nova-network deleting the default route (#741686)
- Fix errors caused by MySQL connection pooling (#741312)

* Mon Sep 26 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-2
- Manage the package's patches in git; no functional changes.

* Thu Sep 22 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-1
- Update to Diablo final.
- Drop some upstreamed patches.
- Update the metadata-accept patch to what's proposed for essex.
- Switch rpc impl from carrot to kombu.

* Mon Sep 19 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.10.d4
- Use tgtadm instead of ietadm (#737046)

* Wed Sep 14 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.9.d4
- Remove python-libguestfs dependency (#738187)

* Mon Sep  5 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.8.d4
- Add iptables rule to allow EC2 metadata requests (#734347)

* Sat Sep  3 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.7.d4
- Add iptables rules to allow requests to dnsmasq (#734347)

* Wed Aug 31 2011 Angus Salkeld <asalkeld@redhat.com> - 2011.3-0.6.d4
- Add the one man page provided by nova.
- Start services with --flagfile rather than --flag-file (#735070)

* Tue Aug 30 2011 Angus Salkeld <asalkeld@redhat.com> - 2011.3-0.5.d4
- Switch from SysV init scripts to systemd units (#734345)

* Mon Aug 29 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.4.d4
- Don't generate root CA during %%post (#707199)
- The nobody group shouldn't own files in /var/lib/nova
- Add workaround for sphinx-build segfault

* Fri Aug 26 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.3.d4
- Update to diablo-4 milestone
- Use statically assigned uid:gid 162:162 (#732442)
- Collapse all sub-packages into openstack-nova; w/o upgrade path
- Reduce use of macros
- Rename stack to nova-stack
- Fix openssl.cnf.tmpl script-without-shebang rpmlint warning
- Really remove ajaxterm
- Mark polkit file as %%config

* Mon Aug 22 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.2.1449bzr
- Remove dependency on python-novaclient

* Wed Aug 17 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.1.1449bzr
- Update to latest upstream.
- nova-import-canonical-imagestore has been removed
- nova-clear-rabbit-queues was added

* Tue Aug  9 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.2.1409bzr
- Update to newer upstream
- nova-instancemonitor has been removed
- nova-instance-usage-audit added

* Tue Aug  9 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.1.bzr1130
- More cleanups
- Change release tag to reflect pre-release status

* Wed Jun 29 2011 Matt Domsch <mdomsch@fedoraproject.org> - 2011.3-1087.1
- Initial package from Alexander Sakhnov <asakhnov@mirantis.com>
  with cleanups by Matt Domsch
