Summary: fd.io packages from the CentOS NFV SIG repository
Name: centos-release-fdio
Version: 1.0
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/NFV
Source0: CentOS-fdio.repo
Source1: COPYING

BuildArch: noarch

%description
yum configuration and basic docs for fd.io packages as delivered via the CentOS NFV SIG.

%prep
cp %{SOURCE1} .

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-fdio.repo


%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-fdio.repo
%license COPYING

%changelog
* Tue Feb 20 2018 Thomas F Herbert <therbert AT redhat.com> - 1.0-1
- Initial version based on centos-release-qemu-ev
