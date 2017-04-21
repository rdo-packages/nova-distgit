%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc %{!?_without_doc:1}%{?_without_doc:0}
%global with_trans %{!?_without_trans:1}%{?_without_trans:0}
%global distro     RDO

Name:             openstack-nova
# Liberty semver reset
# https://review.openstack.org/#/q/I6a35fa0dda798fad93b804d00a46af80f08d475c,n,z
Epoch:            1
Version:          14.0.5
Release:          1%{?dist}
Summary:          OpenStack Compute (nova)

License:          ASL 2.0
URL:              http://openstack.org/projects/compute/
Source0:          https://tarballs.openstack.org/nova/nova-%{upstream_version}.tar.gz

Source1:          nova-dist.conf
Source6:          nova.logrotate

Source10:         openstack-nova-api.service
Source11:         openstack-nova-cert.service
Source12:         openstack-nova-compute.service
Source13:         openstack-nova-network.service
Source15:         openstack-nova-scheduler.service
Source18:         openstack-nova-xvpvncproxy.service
Source19:         openstack-nova-console.service
Source20:         openstack-nova-consoleauth.service
Source25:         openstack-nova-metadata-api.service
Source26:         openstack-nova-conductor.service
Source27:         openstack-nova-cells.service
Source28:         openstack-nova-spicehtml5proxy.service
Source29:         openstack-nova-novncproxy.service
Source31:         openstack-nova-serialproxy.service
Source32:         openstack-nova-os-compute-api.service

Source21:         nova-polkit.pkla
Source23:         nova-polkit.rules
Source22:         nova-ifc-template
Source24:         nova-sudoers
Source30:         openstack-nova-novncproxy.sysconfig
Source33:         nova-placement-api.conf

Source35:         nova_migration-sudoers
Source36:         nova-ssh-config
Source37:         nova-migration-wrapper
Source38:         nova_migration_identity
Source39:         nova_migration_authorized_keys

BuildArch:        noarch
BuildRequires:    intltool
BuildRequires:    python2-devel
BuildRequires:    python-sphinx
BuildRequires:    python-oslo-cache
BuildRequires:    python-oslo-sphinx
BuildRequires:    python-setuptools
BuildRequires:    python-netaddr
BuildRequires:    python-pbr
BuildRequires:    python-d2to1
BuildRequires:    python-six
BuildRequires:    python-oslo-i18n
BuildRequires:    python-cryptography >= 1.0

Requires:         openstack-nova-compute = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-cert = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-scheduler = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-api = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-network = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-conductor = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-console = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-cells = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-novncproxy = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-placement-api = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-migration = %{epoch}:%{version}-%{release}


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

Requires:         python-nova = %{epoch}:%{version}-%{release}
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Requires(pre):    shadow-utils
BuildRequires:    systemd
# Required to build nova.conf.sample
BuildRequires:    python-castellan >= 0.4.0
BuildRequires:    python-glanceclient
BuildRequires:    python-keystonemiddleware
BuildRequires:    python-lxml
BuildRequires:    python-microversion-parse >= 0.1.3
BuildRequires:    python-os-brick
BuildRequires:    python-oslo-db
BuildRequires:    python-oslo-reports
BuildRequires:    python-oslo-service
BuildRequires:    python-oslo-versionedobjects
BuildRequires:    python-paramiko
BuildRequires:    python-websockify
# Required to compile translation files
BuildRequires:    python-babel

# remove old service subpackage
Obsoletes: %{name}-objectstore


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

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         curl
Requires:         iscsi-initiator-utils
Requires:         iptables iptables-ipv6
Requires:         ipmitool
Requires:         python-libguestfs
Requires:         libvirt-python
Requires:         libvirt-daemon-kvm
%if 0%{?rhel}==0
Requires:         libvirt-daemon-lxc
%endif
Requires:         openssh-clients
Requires:         rsync
Requires:         lvm2
Requires:         python-cinderclient >= 1.6.0
Requires(pre):    qemu-kvm >= 2.3.0
Requires:         genisoimage
Requires:         bridge-utils
Requires:         sg3_utils
Requires:         sysfsutils
Requires:         libosinfo

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

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         radvd
Requires:         bridge-utils
Requires:         dnsmasq
Requires:         dnsmasq-utils
Requires:         ebtables
Requires:         conntrack-tools

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

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}

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

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}

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

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         python-cinderclient >= 1.6.0

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

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}

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

%package console
Summary:          OpenStack Nova console access services

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
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

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}

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

%package novncproxy
Summary:          OpenStack Nova noVNC proxy service

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         novnc
Requires:         python-websockify


%description novncproxy
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova noVNC Proxy service that can proxy
VNC traffic over browser websockets connections.

%package spicehtml5proxy
Summary:          OpenStack Nova Spice HTML5 console access service

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         python-websockify

%description spicehtml5proxy
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing the
spice HTML5 console access service to Virtual Machines.

%package serialproxy
Summary:          OpenStack Nova serial console access service

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         python-websockify

%description serialproxy
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing the
serial console access service to Virtual Machines.

%package placement-api
Summary:          OpenStack Nova Placement APIservice

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         httpd
Requires:         mod_wsgi

%description placement-api
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova placement service, which will initially
allow for the management of resource providers.

%package migration
Summary:          OpenStack Nova Migration

Requires:         openstack-nova-compute = %{epoch}:%{version}-%{release}

%description migration
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains scripts and config to support VM migration in Nova.

%package -n       python-nova
Summary:          Nova Python libraries

Requires:         openssl
# Require openssh for ssh-keygen
Requires:         openssh
Requires:         sudo

Requires:         python-paramiko

Requires:         python-eventlet >= 0.17.4
Requires:         python-iso8601
Requires:         python-netaddr
Requires:         python-lxml
Requires:         python-anyjson
Requires:         python-boto
Requires:         python-cheetah
Requires:         python-ldap
Requires:         python-stevedore >= 1.16.0

Requires:         python-memcached

Requires:         python-sqlalchemy >= 1.0.10
Requires:         python-migrate >= 0.9.6
Requires:         python-alembic >= 0.8.0

Requires:         python-paste
Requires:         python-paste-deploy
Requires:         python-routes
Requires:         python-webob

Requires:         python-babel
Requires:         python-castellan >= 0.4.0
Requires:         python-cryptography >= 1.0
Requires:         python-glanceclient >= 2.0.0
Requires:         python-keystonemiddleware >= 4.0.0
Requires:         python-keystoneauth1 >= 2.10.0
Requires:         python-jinja2
Requires:         python-jsonschema
Requires:         python-microversion-parse >= 0.1.2
Requires:         python-neutronclient >= 5.0.0
Requires:         python-novaclient >= 2.30.1
Requires:         python-os-brick
Requires:         python-oslo-cache >= 1.5.0
Requires:         python-oslo-concurrency >= 3.8.0
Requires:         python-oslo-config >= 3.14.0
Requires:         python-oslo-context >= 2.6.0
Requires:         python-oslo-db >= 4.10.0
Requires:         python-oslo-i18n >= 2.1.0
Requires:         python-oslo-log >= 1.14.0
Requires:         python-oslo-messaging >= 5.2.0
Requires:         python-oslo-middleware >= 3.0.0
Requires:         python-oslo-policy >= 1.9.0
Requires:         python-oslo-privsep >= 1.9.0
Requires:         python-oslo-reports >= 0.6.0
Requires:         python-oslo-rootwrap >= 5.0.0
Requires:         python-oslo-serialization >= 1.10.0
Requires:         python-oslo-service >= 1.10.0
Requires:         python-oslo-utils >= 3.16.0
Requires:         python-oslo-versionedobjects >= 1.13.0
Requires:         python-os-vif >= 1.1.0
Requires:         python-oslo-vmware >= 1.16.0
Requires:         python-pbr
Requires:         python-posix_ipc
Requires:         python-psutil
Requires:         python-rfc3986
Requires:         python-six >= 1.9.0

%description -n   python-nova
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains the nova Python library.

%package -n python-nova-tests
Summary:        Nova tests
Requires:       openstack-nova = %{epoch}:%{version}-%{release}

%description -n python-nova-tests
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains the nova Python library.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Compute

BuildRequires:    graphviz

# Required to build module documents
BuildRequires:    python-boto
BuildRequires:    python-eventlet
BuildRequires:    python-barbicanclient
BuildRequires:    python-cinderclient
BuildRequires:    python-keystoneclient
BuildRequires:    python-neutronclient
BuildRequires:    python-os-win
BuildRequires:    python-oslo-config
BuildRequires:    python-oslo-log
BuildRequires:    python-oslo-messaging
BuildRequires:    python-oslo-policy
BuildRequires:    python-oslo-utils
BuildRequires:    python-oslo-vmware
BuildRequires:    python-redis
BuildRequires:    python-rfc3986
BuildRequires:    python-routes
BuildRequires:    python-sqlalchemy
BuildRequires:    python-webob
BuildRequires:    python-zmq
# while not strictly required, quiets the build down when building docs.
BuildRequires:    python-migrate, python-iso8601

%description      doc
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains documentation files for nova.
%endif

%prep
%setup -q -n nova-%{upstream_version}

find . \( -name .gitignore -o -name .placeholder \) -delete

find nova -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# Remove the requirements file so that pbr hooks don't add it
# to distutils requiers_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
PYTHONPATH=. oslo-config-generator --config-file=etc/nova/nova-config-generator.conf

%{__python2} setup.py build

# Generate i18n files
%{__python2} setup.py compile_catalog -d build/lib/nova/locale

# Avoid http://bugzilla.redhat.com/1059815. Remove when that is closed
sed -i 's|group/name|group;name|; s|\[DEFAULT\]/|DEFAULT;|' etc/nova/nova.conf.sample

# Programmatically update defaults in sample config
# which is installed at /etc/nova/nova.conf

#  First we ensure all values are commented in appropriate format.
#  Since icehouse, there was an uncommented keystone_authtoken section
#  at the end of the file which mimics but also conflicted with our
#  distro editing that had been done for many releases.
sed -i '/^[^#[]/{s/^/#/; s/ //g}; /^#[^ ]/s/ = /=/' etc/nova/nova.conf.sample

#  TODO: Make this more robust
#  Note it only edits the first occurrence, so assumes a section ordering in sample
#  and also doesn't support multi-valued variables like dhcpbridge_flagfile.
while read name eq value; do
  test "$name" && test "$value" || continue
  sed -i "0,/^# *$name=/{s!^# *$name=.*!#$name=$value!}" etc/nova/nova.conf.sample
done < %{SOURCE1}

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

# Remove this once sphinxcontrib.seqdiag becomes available
sed -i -e '/sphinxcontrib.seqdiag/d' doc/source/conf.py
sed -i -e 's#../../etc/nova/nova-config-generator.conf#etc/nova/nova-config-generator.conf#' doc/source/conf.py

%if 0%{?with_doc}
%{__python2} setup.py build_sphinx
%endif

%{__python2} setup.py build_sphinx --builder man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 doc/build/man/*.1 %{buildroot}%{_mandir}/man1/

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/buckets
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/instances
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/keys
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/networks
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/tmp
install -d -m 750 %{buildroot}%{_localstatedir}/log/nova
install -d -m 700 %{buildroot}%{_sharedstatedir}/nova/.ssh

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
install -p -D -m 640 %{SOURCE1} %{buildroot}%{_datarootdir}/nova/nova-dist.conf
install -p -D -m 640 etc/nova/nova.conf.sample  %{buildroot}%{_sysconfdir}/nova/nova.conf
install -p -D -m 640 etc/nova/rootwrap.conf %{buildroot}%{_sysconfdir}/nova/rootwrap.conf
install -p -D -m 640 etc/nova/api-paste.ini %{buildroot}%{_sysconfdir}/nova/api-paste.ini
install -p -D -m 640 etc/nova/policy.json %{buildroot}%{_sysconfdir}/nova/policy.json
install -p -D -m 640 %{SOURCE33} %{buildroot}%{_sysconfdir}/httpd/conf.d/00-nova-placement-api.conf
install -d -m 755 %{buildroot}%{_sysconfdir}/nova/migration
install -p -D -m 600 %{SOURCE38} %{buildroot}%{_sysconfdir}/nova/migration/identity
install -p -D -m 644 %{SOURCE39} %{buildroot}%{_sysconfdir}/nova/migration/authorized_keys

# Install version info file
cat > %{buildroot}%{_sysconfdir}/nova/release <<EOF
[Nova]
vendor = %{distro}
product = OpenStack Compute
package = %{release}
EOF

# Install initscripts for Nova services
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/openstack-nova-api.service
install -p -D -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/openstack-nova-cert.service
install -p -D -m 644 %{SOURCE12} %{buildroot}%{_unitdir}/openstack-nova-compute.service
install -p -D -m 644 %{SOURCE13} %{buildroot}%{_unitdir}/openstack-nova-network.service
install -p -D -m 644 %{SOURCE15} %{buildroot}%{_unitdir}/openstack-nova-scheduler.service
install -p -D -m 644 %{SOURCE18} %{buildroot}%{_unitdir}/openstack-nova-xvpvncproxy.service
install -p -D -m 644 %{SOURCE19} %{buildroot}%{_unitdir}/openstack-nova-console.service
install -p -D -m 644 %{SOURCE20} %{buildroot}%{_unitdir}/openstack-nova-consoleauth.service
install -p -D -m 644 %{SOURCE25} %{buildroot}%{_unitdir}/openstack-nova-metadata-api.service
install -p -D -m 644 %{SOURCE26} %{buildroot}%{_unitdir}/openstack-nova-conductor.service
install -p -D -m 644 %{SOURCE27} %{buildroot}%{_unitdir}/openstack-nova-cells.service
install -p -D -m 644 %{SOURCE28} %{buildroot}%{_unitdir}/openstack-nova-spicehtml5proxy.service
install -p -D -m 644 %{SOURCE29} %{buildroot}%{_unitdir}/openstack-nova-novncproxy.service
install -p -D -m 644 %{SOURCE31} %{buildroot}%{_unitdir}/openstack-nova-serialproxy.service
install -p -D -m 644 %{SOURCE32} %{buildroot}%{_unitdir}/openstack-nova-os-compute-api.service

# Install sudoers
install -p -D -m 440 %{SOURCE24} %{buildroot}%{_sysconfdir}/sudoers.d/nova
install -p -D -m 440 %{SOURCE35} %{buildroot}%{_sysconfdir}/sudoers.d/nova_migration

# Install nova ssh client config for migration
install -p -D -m 600 %{SOURCE36} %{buildroot}%{_sharedstatedir}/nova/.ssh/config

# Install nova migration ssh wrapper command
install -p -D -m 755 %{SOURCE37} %{buildroot}%{_bindir}/nova-migration-wrapper

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

# Install novncproxy service options template
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE30} %{buildroot}%{_sysconfdir}/sysconfig/openstack-nova-novncproxy

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python2_sitelib}/nova/locale/*/LC_*/nova*po
rm -f %{buildroot}%{python2_sitelib}/nova/locale/*pot
mv %{buildroot}%{python2_sitelib}/nova/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang nova --all-name

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/nova-debug
rm -fr %{buildroot}%{python2_sitelib}/run_tests.*
rm -f %{buildroot}%{_bindir}/nova-combined
rm -f %{buildroot}/usr/share/doc/nova/README*

%pre common
getent group nova >/dev/null || groupadd -r nova --gid 162
if ! getent passwd nova >/dev/null; then
  useradd -u 162 -r -g nova -G nova,nobody -d %{_sharedstatedir}/nova -s /sbin/nologin -c "OpenStack Nova Daemons" nova
fi
exit 0

%pre compute
usermod -a -G qemu nova
%pre migration
getent group nova_migration >/dev/null || groupadd -r nova_migration
getent passwd nova_migration >/dev/null || \
    useradd -r -g nova_migration -d / -s /bin/bash -c "OpenStack Nova Migration" nova_migration
exit 0

%post compute
%systemd_post %{name}-compute.service
%post network
%systemd_post %{name}-network.service
%post scheduler
%systemd_post %{name}-scheduler.service
%post cert
%systemd_post %{name}-cert.service
%post api
%systemd_post %{name}-api.service %{name}-metadata-api.service %{name}-os-compute-api.service
%post conductor
%systemd_post %{name}-conductor.service
%post console
%systemd_post %{name}-console.service %{name}-consoleauth.service %{name}-xvpvncproxy.service
%post cells
%systemd_post %{name}-cells.service
%post novncproxy
%systemd_post %{name}-novncproxy.service
%post spicehtml5proxy
%systemd_post %{name}-spicehtml5proxy.service
%post serialproxy
%systemd_post %{name}-serialproxy.service

%preun compute
%systemd_preun %{name}-compute.service
%preun network
%systemd_preun %{name}-network.service
%preun scheduler
%systemd_preun %{name}-scheduler.service
%preun cert
%systemd_preun %{name}-cert.service
%preun api
%systemd_preun %{name}-api.service %{name}-metadata-api.service %{name}-os-compute-api.service
%preun conductor
%systemd_preun %{name}-conductor.service
%preun console
%systemd_preun %{name}-console.service %{name}-consoleauth.service %{name}-xvpvncproxy.service
%preun cells
%systemd_preun %{name}-cells.service
%preun novncproxy
%systemd_preun %{name}-novncproxy.service
%preun spicehtml5proxy
%systemd_preun %{name}-spicehtml5proxy.service
%preun serialproxy
%systemd_preun %{name}-serialproxy.service

%postun compute
%systemd_postun_with_restart %{name}-compute.service
%postun network
%systemd_postun_with_restart %{name}-network.service
%postun scheduler
%systemd_postun_with_restart %{name}-scheduler.service
%postun cert
%systemd_postun_with_restart %{name}-cert.service
%postun api
%systemd_postun_with_restart %{name}-api.service %{name}-metadata-api.service %{name}-os-compute-api.service
%postun conductor
%systemd_postun_with_restart %{name}-conductor.service
%postun console
%systemd_postun_with_restart %{name}-console.service %{name}-consoleauth.service %{name}-xvpvncproxy.service
%postun cells
%systemd_postun_with_restart %{name}-cells.service
%postun novncproxy
%systemd_postun_with_restart %{name}-novncproxy.service
%postun spicehtml5proxy
%systemd_postun_with_restart %{name}-spicehtml5proxy.service
%postun serialproxy
%systemd_postun_with_restart %{name}-serialproxy.service

%files
%doc LICENSE
%{_bindir}/nova-all

%files common -f nova.lang
%doc LICENSE
%dir %{_datarootdir}/nova
%attr(-, root, nova) %{_datarootdir}/nova/nova-dist.conf
%{_datarootdir}/nova/client.ovpn.template
%{_datarootdir}/nova/interfaces.template
%{_datarootdir}/nova/rootwrap/network.filters
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

%dir %attr(0750, nova, root) %{_localstatedir}/log/nova
%dir %attr(0755, nova, root) %{_localstatedir}/run/nova

%{_bindir}/nova-manage
%{_bindir}/nova-policy
%{_bindir}/nova-rootwrap
%{_bindir}/nova-rootwrap-daemon

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
%{_bindir}/nova-idmapshift
%{_unitdir}/openstack-nova-compute.service
%{_datarootdir}/nova/rootwrap/compute.filters

%files network
%{_bindir}/nova-network
%{_bindir}/nova-dhcpbridge
%{_unitdir}/openstack-nova-network.service

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

%files console
%{_bindir}/nova-console*
%{_bindir}/nova-xvpvncproxy
%{_unitdir}/openstack-nova-console*.service
%{_unitdir}/openstack-nova-xvpvncproxy.service

%files cells
%{_bindir}/nova-cells
%{_unitdir}/openstack-nova-cells.service

%files novncproxy
%{_bindir}/nova-novncproxy
%{_unitdir}/openstack-nova-novncproxy.service
%config(noreplace) %{_sysconfdir}/sysconfig/openstack-nova-novncproxy

%files spicehtml5proxy
%{_bindir}/nova-spicehtml5proxy
%{_unitdir}/openstack-nova-spicehtml5proxy.service

%files serialproxy
%{_bindir}/nova-serialproxy
%{_unitdir}/openstack-nova-serialproxy.service

%files placement-api
%config(noreplace) %{_sysconfdir}/httpd/conf.d/00-nova-placement-api.conf
%{_bindir}/nova-placement-api

%files migration
%{_bindir}/nova-migration-wrapper
%config(noreplace) %{_sysconfdir}/sudoers.d/nova_migration
%dir %attr(0700, nova, nova) %{_sharedstatedir}/nova/.ssh
%attr(0600, nova, nova) %{_sharedstatedir}/nova/.ssh/config
%dir %{_sysconfdir}/nova/migration
%config(noreplace) %attr(0640, root, nova_migration) %{_sysconfdir}/nova/migration/authorized_keys
%config(noreplace) %attr(0600, nova, nova) %{_sysconfdir}/nova/migration/identity

%files -n python-nova
%doc LICENSE
%{python2_sitelib}/nova
%{python2_sitelib}/nova-*.egg-info
%exclude %{python2_sitelib}/nova/tests

%files -n python-nova-tests
%license LICENSE
%{python2_sitelib}/nova/tests

%if 0%{?with_doc}
%files doc
%doc LICENSE doc/build/html
%endif

%changelog
* Wed Mar 22 2017 Alfredo Moralejo <amoralej@redhat.com> 1:14.0.5-1
- Update to 14.0.5

* Tue Feb 28 2017 Alfredo Moralejo <amoralej@redhat.com> 1:14.0.4-1
- Update to 14.0.4

* Fri Jan 06 2017 Jon Schlueter <jschluet@redhat.com> 1:14.0.3-1
- Update to 14.0.3
- include libosinfo as Requires for compute RPM

* Mon Nov 07 2016 Alfredo Moralejo <amoralej@redhat.com> 1:14.0.2-1
- Update to 14.0.2

* Thu Oct 13 2016 Alfredo Moralejo <amoralej@redhat.com> 1:14.0.1-1
- Update to 14.0.1

* Thu Oct 06 2016 Haikel Guemar <hguemar@fedoraproject.org> 1:14.0.0-1
- Update to 14.0.0

* Thu Sep 29 2016 Haikel Guemar <hguemar@fedoraproject.org> 1:14.0.0-0.3.0rc2
- Update to 14.0.0.0rc2

* Wed Sep 21 2016 Alfredo Moralejo <amoralej@redhat.com> 1:14.0.0-0.2.0rc1
- Update to 14.0.0.0rc1

* Wed Sep 14 2016 Haikel Guemar <hguemar@fedoraproject.org> 1:14.0.0-0.1.0b3
- Update to 14.0.0.0b3

