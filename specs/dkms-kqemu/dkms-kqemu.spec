# $Id$
# Authority: matthias
# Dist: nodist

%define pre pre11

Summary: QEMU accelerator kernel module
Name: dkms-kqemu
Version: 1.3.0
Release: 0.1.%{pre}
License: GPL
Group: System Environment/Kernel
URL: http://fabrice.bellard.free.fr/qemu/
Source: http://fabrice.bellard.free.fr/qemu/kqemu-%{version}%{pre}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms

%description
QEMU accelerator kernel module, a host driver to achieve near native
performances when using QEMU as a virtualizer.


%prep
%setup -n kqemu-%{version}%{pre}


%build


%install
%{__rm} -rf %{buildroot}

%define dkms_name kqemu
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a * %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="./configure --kernel-path=${kernel_source_dir} && make"
BUILT_MODULE_NAME[0]=kqemu
DEST_MODULE_LOCATION[0]=/kernel/drivers/misc
AUTOINSTALL="YES"
EOF


%clean
%{__rm} -rf %{buildroot}


%post
# Add to DKMS registry
dkms add -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
# Rebuild and make available for the currenty running kernel
dkms build -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
dkms install -m %{dkms_name} -v %{dkms_vers} %{?quiet} --force || :

%preun
# Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{dkms_vers} %{?quiet} --all || :


%files
%defattr(-, root, root, 0755)
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/


%changelog
* Thu Feb 15 2007 Dag Wieers <dag@wieers.com> - 1.3.0-0.1.pre11
- Updated to release 1.3.0pre11.

* Tue Feb  6 2007 Matthias Saou <http://freshrpms.net/> 1.3.0-0.1.pre10
- Initial RPM release.
