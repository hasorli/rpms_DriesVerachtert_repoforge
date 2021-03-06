# $Id$
# Authority: shuff

##ExcludeDist: rh3 rh4

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: converts CVS repository to Subversion
Name: cvs2svn
Version: 2.3.0
Release: 1%{?dist}
License: Apache
Group: Development/Tools
URL: http://cvs2svn.tigris.org/

# this path is unlikely to remain consistent with new releases :(
Source: http://cvs2svn.tigris.org/files/documents/1462/46528/cvs2svn-2.3.0.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.4, python-devel >= 2.4
BuildRequires: rpm-macros-rpmforge
Requires: coreutils
Requires: cvs
Requires: gdbm
Requires: rcs

# we don't want to either provide or require anything from _docdir, per policy
%filter_provides_in %{_docdir}
%filter_requires_in %{_docdir}

# actually set up the filtering
%filter_setup


%description
cvs2svn is a tool for migrating a CVS repository to Subversion or git. The main
design goals are robustness and 100% data preservation. cvs2svn can convert
just about any CVS repository we've ever seen, including gcc, Mozilla, FreeBSD,
KDE, GNOME...

cvs2svn infers what happened in the history of your CVS repository and
replicates that history as accurately as possible in the target SCM. All
revisions, branches, tags, log messages, author names, and commit dates are
converted. cvs2svn deduces what CVS modifications were made at the same time,
and outputs these modifications grouped together as changesets in the target
SCM. cvs2svn also deals with many CVS quirks and is highly configurable.


%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root="%{buildroot}"


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES COMMITTERS COPYING HACKING README
%doc contrib/ doc/ www/ *.options
%{_bindir}/*
%{python_sitearch}/*


%changelog
* Wed Oct 07 2009 Steve Huff <shuff@vecna.org> - 2.3.0-1
- Initial package.

