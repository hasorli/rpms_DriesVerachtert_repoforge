# $Id$

# Authority: atrpms

%define rname Net-SNMP

Summary: Net-SNMP Perl module
Name: perl-Net-SNMP
Version: 4.1.2
Release: 0
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/dist/Net-SNMP/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/D/DT/DTOWN/Net-SNMP-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl >= 0:5.6, perl(Digest::HMAC), perl(Crypt::DES)
Requires: perl >= 0:5.6

%description
The Net::SNMP module implements an object oriented interface to the
Simple Network Management Protocol.

%prep
%setup -n %{rname}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/%{_target_cpu}-linux-thread-multi/
%{__rm} -rf %{buildroot}%{_libdir}/perl5/vendor_perl/*/%{_target_cpu}-linux-thread-multi/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/perl5/

%changelog
* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 4.1.2-1
- Added perl-Crypt-DES BuildRequires. (Russ Herrold)

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 4.1.0-0
- Updated to release 4.1.0.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 4.0.3-0
- Initial package. (using DAR)
