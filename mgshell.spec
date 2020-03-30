# Generated with python3 setup.py bdist_rpm --requires python3-click
%define name mgshell
%define version 0.0.1
%define unmangled_version 0.0.1
%define release 1
%define mglibexecdir %{_libexecdir}/%{name}

%define debug_package %nil

%global debug_package %{nil}

Name: %{name}
Version: %{version}
Release: %{release}
Summary: A command line aid for navigating OpenShift 4 must gather reports.
License: MIT
Vendor: Robert Bost <bostrt at gmail dot com>
Url: https://github.com/bostrt/mgshell

Source0: https://github.com/bostrt/mgshell/archive/%{version}.tar.gz
Source1: mgshell-ns.sh
Source2: mgshell-pod.sh
Source3: mgshell-log.sh
Source4: mgshell-mg.sh
Source5: mgshell-profile.sh

Group: Application/Productivity
BuildArch: x86_64

BuildRequires: gcc python3-devel
Requires: python3-click bash-completion

%description
A command line aid for navigating OpenShift 4 must gather reports.

%prep
# Setup Source0
%setup -q -n %{name}-%{version}
# Setup Source1 (completions)

%build
%py3_build
gcc findmgmarker.c -o findmgmarker

%install
%py3_install -- --install-scripts %{mglibexecdir}
mkdir -p %{buildroot}/%{mglibexecdir}
install -p -m 755 findmgmarker %{buildroot}/%{mglibexecdir}/findmgmarker
install -p -D -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/bash_completion.d/mgshell-ns.sh
install -p -D -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/bash_completion.d/mgshell-pod.sh
install -p -D -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/bash_completion.d/mgshell-log.sh
install -p -D -m 644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/bash_completion.d/mgshell-mg.sh
install -p -D -m 755 %{SOURCE5} %{buildroot}/%{_sysconfdir}/profile.d/mgshell.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info
%{mglibexecdir}/mg
%{mglibexecdir}/ns
%{mglibexecdir}/pod
%{mglibexecdir}/log
%{mglibexecdir}/root
%{mglibexecdir}/findmgmarker
%{_sysconfdir}/bash_completion.d/mgshell-log.sh
%{_sysconfdir}/bash_completion.d/mgshell-mg.sh
%{_sysconfdir}/bash_completion.d/mgshell-ns.sh
%{_sysconfdir}/bash_completion.d/mgshell-pod.sh
%{_sysconfdir}/profile.d/mgshell.sh