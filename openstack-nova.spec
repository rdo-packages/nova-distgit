%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order bashate psycopg2-binary types-paramiko
# Exclude sphinx from BRs if docs are disabled
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif
%global with_doc 0
%global rhosp 0
%if 0%{?rhosp} == 0
%global distro     RDO
%else
%global distro     Red Hat
%endif
%global qemu_version     3.1.0
%global libvirt_version  5.0.0

%global common_desc \
OpenStack Compute (codename Nova) is open source software designed to \
provision and manage large networks of virtual machines, creating a \
redundant and scalable cloud computing platform. It gives you the \
software, control panels, and APIs required to orchestrate a cloud, \
including running instances, managing networks, and controlling access \
through users and projects. OpenStack Compute strives to be both \
hardware and hypervisor agnostic, currently supporting a variety of \
standard hardware configurations and seven major hypervisors.

Name:             openstack-nova
# Liberty semver reset
# https://review.openstack.org/#/q/I6a35fa0dda798fad93b804d00a46af80f08d475c,n,z
Epoch:            1
Version:          XXX
Release:          XXX
Summary:          OpenStack Compute (nova)

License:          Apache-2.0
URL:              http://openstack.org/projects/compute/
Source0:          https://tarballs.openstack.org/nova/nova-%{upstream_version}.tar.gz

Source1:          nova-dist.conf
Source6:          nova.logrotate

Source10:         openstack-nova-api.service
Source12:         openstack-nova-compute.service
Source15:         openstack-nova-scheduler.service
Source25:         openstack-nova-metadata-api.service
Source26:         openstack-nova-conductor.service
Source28:         openstack-nova-spicehtml5proxy.service
Source29:         openstack-nova-novncproxy.service
Source31:         openstack-nova-serialproxy.service
Source32:         openstack-nova-os-compute-api.service

Source22:         nova-ifc-template
Source24:         nova-sudoers
Source30:         openstack-nova-novncproxy.sysconfig
Source34:         policy.json

Source35:         nova_migration-sudoers
Source36:         nova-ssh-config
Source37:         nova-migration-wrapper
Source38:         nova_migration_identity
Source39:         nova_migration_authorized_keys
Source40:         nova_migration-rootwrap.conf
Source41:         nova_migration-rootwrap_cold_migration
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/nova/nova-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:        noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif
BuildRequires:    openstack-macros
BuildRequires:    intltool
BuildRequires:    python3-devel
BuildRequires:    pyproject-rpm-macros
BuildRequires:    git-core

Requires:         openstack-nova-compute = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-scheduler = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-api = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-conductor = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-novncproxy = %{epoch}:%{version}-%{release}
Requires:         openstack-nova-migration = %{epoch}:%{version}-%{release}


%description
%{common_desc}

%package common
Summary:          Components common to all OpenStack Nova services

Requires:         python3-nova = %{epoch}:%{version}-%{release}
%{?systemd_ordering}
Requires(pre):    shadow-utils
BuildRequires:    systemd

# remove old service subpackage
Obsoletes: %{name}-objectstore


%description common
%{common_desc}

This package contains scripts, config and dependencies shared
between all the OpenStack nova services.


%package compute
Summary:          OpenStack Nova Virtual Machine control service

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         curl
Requires:         iptables
Requires:         iptables-services
Requires:         ipmitool
Requires:         /usr/bin/virsh
Requires:         openssh-clients
Requires:         rsync
Requires:         python3-cinderclient >= 3.3.0
Requires:         xorriso

# NOTE-1: From RHEL-8 onwards there is no 'qemu-kvm' vs.
#         'qemu-kvm-ev|rhev' RPM split, instead there is only one RPM
#         package: 'qemu-kvm'.
#
#         The 'qemu-kvm' RPM in RHEL-8 allows granular installation of
#         functionality.  I.e. RHEL-8's 'qemu-kvm' RPM pulls in
#         everything, just like it did in RHEL-7.  However, now there is
#         a 'qemu-kvm-core' RPM, which pulls in only the core QEMU
#         functionality.  And several sub-RPMs that provide Block Layer
#         drivers (SSH, Curl, GlusterFS, iSCSI, RBD, etc).
#
# NOTE-2: We're using "Requires(pre)" (instead of "Requires") as a
#         safety check, so that when the 'nova' user is added to the
#         'qemu' and 'libvirt' groups in the %pre section, those
#         groups are guaranteed to exist.
Requires(pre):    qemu-kvm-core >= %{qemu_version}
Requires(pre):    qemu-kvm-block-rbd >= %{qemu_version}
# The "hw-display-virtio-vga.so" used to be part of 'qemu-kvm-common'
# RPM, however now it has moved to its own separate package called
# 'device-display-virtio-vga'.  Having a _libdir-based Requires (instead
# of a package-name based Requires) will allow DNF to transparently
# handle this during updates.
# "hw-display-virtio-vga.so" is not provided for aarch64 so we need to do
# the requires only for x86_64 and ppc64le using boolean dependencies.
Requires(pre):   (%{_prefix}/lib64/qemu-kvm/hw-display-virtio-vga.so if (filesystem(x86-64) or filesystem(ppc-64)))
Requires(pre):   (%{_prefix}/lib64/qemu-kvm/hw-display-virtio-gpu.so if filesystem(aarch-64))
Requires(pre):    python3-libvirt >= %{libvirt_version}
Requires(pre):    libvirt-daemon-driver-nodedev >= %{libvirt_version}
Requires(pre):    libvirt-daemon-driver-nwfilter >= %{libvirt_version}
Requires(pre):    libvirt-daemon-driver-secret >= %{libvirt_version}
Requires(pre):    libvirt-daemon-driver-qemu >= %{libvirt_version}
Requires(pre):    libvirt-daemon-driver-storage-core >= %{libvirt_version}

Requires:         libosinfo

Requires:         python3-libguestfs
Requires:         python3-libvirt


%description compute
%{common_desc}

This package contains the Nova service for controlling Virtual Machines.


%package scheduler
Summary:          OpenStack Nova VM distribution service

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}

%description scheduler
%{common_desc}

This package contains the service for scheduling where
to run Virtual Machines in the cloud.


%package api
Summary:          OpenStack Nova API services

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         python3-cinderclient >= 3.3.0

%description api
%{common_desc}

This package contains the Nova services providing programmatic access.

%package conductor
Summary:          OpenStack Nova Conductor services

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}

%description conductor
%{common_desc}

This package contains the Nova services providing database access for
the compute service

%package novncproxy
Summary:          OpenStack Nova noVNC proxy service

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         novnc
Requires:         python3-websockify >= 0.9.0

%description novncproxy
%{common_desc}

This package contains the Nova noVNC Proxy service that can proxy
VNC traffic over browser websockets connections.

%package spicehtml5proxy
Summary:          OpenStack Nova Spice HTML5 console access service

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         python3-websockify >= 0.9.0

%description spicehtml5proxy
%{common_desc}

This package contains the Nova services providing the
spice HTML5 console access service to Virtual Machines.

%package serialproxy
Summary:          OpenStack Nova serial console access service

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
%description serialproxy
%{common_desc}

This package contains the Nova services providing the
serial console access service to Virtual Machines.

%package migration
Summary:          OpenStack Nova Migration

Requires:         openstack-nova-compute = %{epoch}:%{version}-%{release}

%description migration
%{common_desc}

This package contains scripts and config to support VM migration in Nova.

%package -n       python3-nova
Summary:          Nova Python libraries

Requires:         openssl
# Require openssh for ssh-keygen
Requires:         openssh
Requires:         sudo
# Optional dependency
Requires:         python3-memcached


%description -n   python3-nova
%{common_desc}

This package contains the nova Python library.

%package -n python3-nova-tests
Summary:        Nova tests
Requires:       openstack-nova = %{epoch}:%{version}-%{release}

%description -n python3-nova-tests
%{common_desc}

This package contains the nova Python library.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Compute

BuildRequires:    graphviz
%description      doc
%{common_desc}

This package contains documentation files for nova.
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n nova-%{upstream_version} -S git

find . \( -name .gitignore -o -name .placeholder \) -delete

find nova -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Disable extra zvm from automatic BRs
sed -i '/^  zvm.*/d' tox.ini

# requirements-override-centos C9S is providing packaging-20.9 while nova introduced >=21.0 with
# no justification
sed -i 's/^packaging.*/packaging>=20.9/g' requirements.txt

# Do not run linters
rm -f nova/tests/unit/test_hacking.py

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

PYTHONPATH=. oslo-config-generator --config-file=etc/nova/nova-config-generator.conf
# Generate a sample compute config file based on etc/nova/nova-config-generator.conf
PYTHONPATH=. oslo-config-generator --summarize --wrap-width 80 \
  --namespace oslo.messaging \
  --namespace oslo.policy \
  --namespace oslo.privsep \
  --namespace oslo.service.periodic_task \
  --namespace oslo.service.service \
  --namespace oslo.concurrency \
  --namespace oslo.reports \
  --namespace osprofiler \
  --namespace nova.common \
  --namespace nova.compute \
  --output-file etc/nova/nova-compute.conf.sample
# Generate a sample policy.yaml file for documentation purposes only
PYTHONPATH=. oslopolicy-sample-generator --config-file=etc/nova/nova-policy-generator.conf

# Programmatically update defaults in sample config
# which is installed at /etc/nova/nova.conf and /etc/nova/nova-compute.conf

#  First we ensure all values are commented in appropriate format.
#  Since icehouse, there was an uncommented keystone_authtoken section
#  at the end of the file which mimics but also conflicted with our
#  distro editing that had been done for many releases.
sed -i '/^[^#[]/{s/^/#/; s/ //g}; /^#[^ ]/s/ = /=/' etc/nova/nova.conf.sample
sed -i '/^[^#[]/{s/^/#/; s/ //g}; /^#[^ ]/s/ = /=/' etc/nova/nova-compute.conf.sample

#  TODO: Make this more robust
#  Note it only edits the first occurrence, so assumes a section ordering in sample
#  and also doesn't support multi-valued variables like dhcpbridge_flagfile.
while read name eq value; do
  test "$name" && test "$value" || continue
  sed -i "0,/^# *$name=/{s!^# *$name=.*!#$name=$value!}" etc/nova/nova.conf.sample
  sed -i "0,/^# *$name=/{s!^# *$name=.*!#$name=$value!}" etc/nova/nova-compute.conf.sample
done < %{SOURCE1}

%install
%pyproject_install

# Generate config files

PYTHONPATH="%{buildroot}/%{python3_sitelib}" oslo-config-generator --config-file=etc/nova/nova-config-generator.conf
# Generate a sample compute config file based on etc/nova/nova-config-generator.conf
PYTHONPATH="%{buildroot}/%{python3_sitelib}" oslo-config-generator --summarize --wrap-width 80 \
  --namespace oslo.messaging \
  --namespace oslo.policy \
  --namespace oslo.privsep \
  --namespace oslo.service.periodic_task \
  --namespace oslo.service.service \
  --namespace oslo.concurrency \
  --namespace oslo.reports \
  --namespace osprofiler \
  --namespace nova.common \
  --namespace nova.compute \
  --output-file etc/nova/nova-compute.conf.sample
# Generate a sample policy.yaml file for documentation purposes only
PYTHONPATH="%{buildroot}/%{python3_sitelib}" oslopolicy-sample-generator --config-file=etc/nova/nova-policy-generator.conf

# Programmatically update defaults in sample config
# which is installed at /etc/nova/nova.conf and /etc/nova/nova-compute.conf

#  First we ensure all values are commented in appropriate format.
#  Since icehouse, there was an uncommented keystone_authtoken section
#  at the end of the file which mimics but also conflicted with our
#  distro editing that had been done for many releases.
sed -i '/^[^#[]/{s/^/#/; s/ //g}; /^#[^ ]/s/ = /=/' etc/nova/nova.conf.sample
sed -i '/^[^#[]/{s/^/#/; s/ //g}; /^#[^ ]/s/ = /=/' etc/nova/nova-compute.conf.sample

#  TODO: Make this more robust
#  Note it only edits the first occurrence, so assumes a section ordering in sample
#  and also doesn't support multi-valued variables like dhcpbridge_flagfile.
while read name eq value; do
  test "$name" && test "$value" || continue
  sed -i "0,/^# *$name=/{s!^# *$name=.*!#$name=$value!}" etc/nova/nova.conf.sample
  sed -i "0,/^# *$name=/{s!^# *$name=.*!#$name=$value!}" etc/nova/nova-compute.conf.sample
done < %{SOURCE1}

# Generate i18n files
%{__python3} setup.py compile_catalog -d %{buildroot}%{python3_sitelib}/nova/locale -D nova

%if 0%{?with_doc}
%tox -e docs
rm -rf doc/build/html/.{doctrees,buildinfo}
sphinx-build -b man doc/source doc/build/man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 doc/build/man/*.1 %{buildroot}%{_mandir}/man1/
%endif

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/buckets
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/instances
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/keys
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/networks
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/tmp
install -d -m 750 %{buildroot}%{_localstatedir}/log/nova
install -d -m 700 %{buildroot}%{_sharedstatedir}/nova/.ssh

# Install config files
install -d -m 755 %{buildroot}%{_sysconfdir}/nova
install -p -D -m 640 %{SOURCE1} %{buildroot}%{_datarootdir}/nova/nova-dist.conf
install -p -D -m 640 etc/nova/nova.conf.sample  %{buildroot}%{_sysconfdir}/nova/nova.conf
install -p -D -m 640 etc/nova/nova-compute.conf.sample %{buildroot}%{_sysconfdir}/nova/nova-compute.conf
install -p -D -m 640 etc/nova/rootwrap.conf %{buildroot}%{_sysconfdir}/nova/rootwrap.conf
install -p -D -m 640 etc/nova/api-paste.ini %{buildroot}%{_sysconfdir}/nova/api-paste.ini
install -d -m 755 %{buildroot}%{_sysconfdir}/nova/migration
install -p -D -m 600 %{SOURCE38} %{buildroot}%{_sysconfdir}/nova/migration/identity
install -p -D -m 644 %{SOURCE39} %{buildroot}%{_sysconfdir}/nova/migration/authorized_keys
install -p -D -m 640 %{SOURCE40} %{buildroot}%{_sysconfdir}/nova/migration/rootwrap.conf
install -d -m 755 %{buildroot}%{_sysconfdir}/nova/migration/rootwrap.d
install -p -D -m 640 %{SOURCE41} %{buildroot}%{_sysconfdir}/nova/migration/rootwrap.d/cold_migration.filters

# Install empty policy.json file to cover rpm updates with untouched policy files.
install -p -D -m 640 %{SOURCE34} %{buildroot}%{_sysconfdir}/nova/policy.json

# Install version info file
cat > %{buildroot}%{_sysconfdir}/nova/release <<EOF
[Nova]
vendor = %{distro}
product = OpenStack Compute
package = %{release}
EOF

# Install initscripts for Nova services
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/openstack-nova-api.service
install -p -D -m 644 %{SOURCE12} %{buildroot}%{_unitdir}/openstack-nova-compute.service
install -p -D -m 644 %{SOURCE15} %{buildroot}%{_unitdir}/openstack-nova-scheduler.service
install -p -D -m 644 %{SOURCE25} %{buildroot}%{_unitdir}/openstack-nova-metadata-api.service
install -p -D -m 644 %{SOURCE26} %{buildroot}%{_unitdir}/openstack-nova-conductor.service
install -p -D -m 644 %{SOURCE28} %{buildroot}%{_unitdir}/openstack-nova-spicehtml5proxy.service
install -p -D -m 644 %{SOURCE29} %{buildroot}%{_unitdir}/openstack-nova-novncproxy.service
install -p -D -m 644 %{SOURCE31} %{buildroot}%{_unitdir}/openstack-nova-serialproxy.service
install -p -D -m 644 %{SOURCE32} %{buildroot}%{_unitdir}/openstack-nova-os-compute-api.service

# (amoralej) we need to keep this until https://review.opendev.org/686816 is merged
rm -f %{buildroot}%{_bindir}/nova-network

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
install -p -D -m 644 %{SOURCE22} %{buildroot}%{_datarootdir}/nova/interfaces.template

# Install rootwrap files in /usr/share/nova/rootwrap
mkdir -p %{buildroot}%{_datarootdir}/nova/rootwrap/
install -p -D -m 644 etc/nova/rootwrap.d/* %{buildroot}%{_datarootdir}/nova/rootwrap/

# Install novncproxy service options template
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE30} %{buildroot}%{_sysconfdir}/sysconfig/openstack-nova-novncproxy

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/nova/locale/*/LC_*/nova*po
rm -f %{buildroot}%{python3_sitelib}/nova/locale/*pot
mv %{buildroot}%{python3_sitelib}/nova/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang nova --all-name

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/nova-debug
rm -fr %{buildroot}%{python3_sitelib}/run_tests.*
rm -f %{buildroot}%{_bindir}/nova-combined
rm -f %{buildroot}/usr/share/doc/nova/README*

# Remove duplicated configuration files deployed at /usr/etc
rm -rf %{buildroot}%{_prefix}/etc/nova

# FIXME(jpena): unit tests are taking too long in the current DLRN infra
# Until we have a better architecture, let's not run them when under DLRN
%check
# Limit the number of concurrent workers to 2
%tox -e %{default_toxenv} -- -- --concurrency 2

%pre common
getent group nova >/dev/null || groupadd -r nova --gid 162
if ! getent passwd nova >/dev/null; then
  useradd -u 162 -r -g nova -G nova,nobody -d %{_sharedstatedir}/nova -s /sbin/nologin -c "OpenStack Nova Daemons" nova
fi
exit 0

%pre compute
usermod -a -G qemu nova
usermod -a -G libvirt nova
%pre migration
getent group nova_migration >/dev/null || groupadd -r nova_migration
getent passwd nova_migration >/dev/null || \
    useradd -r -g nova_migration -d / -s /bin/bash -c "OpenStack Nova Migration" nova_migration
exit 0

%post compute
%systemd_post %{name}-compute.service
%post scheduler
%systemd_post %{name}-scheduler.service
%post api
%systemd_post %{name}-api.service %{name}-metadata-api.service %{name}-os-compute-api.service
%post conductor
%systemd_post %{name}-conductor.service
%post novncproxy
%systemd_post %{name}-novncproxy.service
%post spicehtml5proxy
%systemd_post %{name}-spicehtml5proxy.service
%post serialproxy
%systemd_post %{name}-serialproxy.service

%preun compute
%systemd_preun %{name}-compute.service
%preun scheduler
%systemd_preun %{name}-scheduler.service
%preun api
%systemd_preun %{name}-api.service %{name}-metadata-api.service %{name}-os-compute-api.service
%preun conductor
%systemd_preun %{name}-conductor.service
%preun novncproxy
%systemd_preun %{name}-novncproxy.service
%preun spicehtml5proxy
%systemd_preun %{name}-spicehtml5proxy.service
%preun serialproxy
%systemd_preun %{name}-serialproxy.service

%postun compute
%systemd_postun_with_restart %{name}-compute.service
%postun scheduler
%systemd_postun_with_restart %{name}-scheduler.service
%postun api
%systemd_postun_with_restart %{name}-api.service %{name}-metadata-api.service %{name}-os-compute-api.service
%postun conductor
%systemd_postun_with_restart %{name}-conductor.service
%postun novncproxy
%systemd_postun_with_restart %{name}-novncproxy.service
%postun spicehtml5proxy
%systemd_postun_with_restart %{name}-spicehtml5proxy.service
%postun serialproxy
%systemd_postun_with_restart %{name}-serialproxy.service

%files

%files common -f nova.lang
%license LICENSE
%doc etc/nova/policy.yaml.sample
%dir %{_datarootdir}/nova
%attr(-, root, nova) %{_datarootdir}/nova/nova-dist.conf
%{_datarootdir}/nova/interfaces.template
%dir %{_sysconfdir}/nova
%{_sysconfdir}/nova/release
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/nova.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/api-paste.ini
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/rootwrap.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-nova
%config(noreplace) %{_sysconfdir}/sudoers.d/nova

%dir %attr(0750, nova, root) %{_localstatedir}/log/nova
%dir %attr(0755, nova, root) %{_localstatedir}/run/nova

%{_bindir}/nova-manage
%{_bindir}/nova-policy
%{_bindir}/nova-rootwrap
%{_bindir}/nova-rootwrap-daemon
%{_bindir}/nova-status

%if 0%{?with_doc}
%{_mandir}/man1/nova*.1.gz
%endif

%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova
%dir %{_sharedstatedir}/nova/buckets
%dir %{_sharedstatedir}/nova/instances
%dir %{_sharedstatedir}/nova/keys
%dir %{_sharedstatedir}/nova/networks
%dir %{_sharedstatedir}/nova/tmp

%files compute
%{_bindir}/nova-compute
%{_unitdir}/openstack-nova-compute.service
%{_datarootdir}/nova/rootwrap/compute.filters
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/nova-compute.conf

%files scheduler
%{_bindir}/nova-scheduler
%{_unitdir}/openstack-nova-scheduler.service

%files api
%{_bindir}/nova-api*
%{_bindir}/nova-metadata-wsgi
%{_unitdir}/openstack-nova-*api.service

%files conductor
%{_bindir}/nova-conductor
%{_unitdir}/openstack-nova-conductor.service

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

%files migration
%{_bindir}/nova-migration-wrapper
%config(noreplace) %{_sysconfdir}/sudoers.d/nova_migration
%dir %attr(0700, nova, nova) %{_sharedstatedir}/nova/.ssh
%attr(0600, nova, nova) %{_sharedstatedir}/nova/.ssh/config
%dir %{_sysconfdir}/nova/migration
%config(noreplace) %attr(0640, root, nova_migration) %{_sysconfdir}/nova/migration/authorized_keys
%config(noreplace) %attr(0600, nova, nova) %{_sysconfdir}/nova/migration/identity
%config(noreplace) %attr(0640, root, root) %{_sysconfdir}/nova/migration/rootwrap.conf
%dir %{_sysconfdir}/nova/migration/rootwrap.d
%config(noreplace) %attr(0640, root, root) %{_sysconfdir}/nova/migration/rootwrap.d/cold_migration.filters

%files -n python3-nova
%license LICENSE
%{python3_sitelib}/nova
%{python3_sitelib}/nova-*.dist-info
%exclude %{python3_sitelib}/nova/tests

%files -n python3-nova-tests
%license LICENSE
%{python3_sitelib}/nova/tests

%if 0%{?with_doc}
%files doc
%license LICENSE
%doc doc/build/html
%endif

%changelog

