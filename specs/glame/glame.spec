# $Id$

Summary: GNU/Linux Audio Mechanics, the GIMP of audio processing
Name: glame
Version: 1.0.3
Release: 1
License: GPL
Group: Applications/Multimedia
Source: http://dl.sf.net/glame/glame-%{version}.tar.gz
URL: http://glame.sourceforge.net/ 
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): info
Requires(preun): info
BuildRequires: gtk+-devel, gnome-libs-devel, libxml-devel, ORBit-devel
BuildRequires: guile-devel, libglade-devel, fftw-devel
BuildRequires: audiofile-devel, esound-devel, alsa-lib-devel
BuildRequires: libmad-devel, libvorbis-devel, ladspa-devel

%description
GLAME is meant to be the GIMP of audio processing. It is designed to be
a powerful, fast, stable, and easily extensible sound editor for Linux
and compatible systems.


%package devel
Summary: Development libraries from the GNU/Linux Audio Mechanics
Group: Development/Libraries
Requires(post): info
Requires(preun): info
Requires: %{name} = %{version}

%description devel
GLAME is meant to be the GIMP of audio processing. It is designed to be
a powerful, fast, stable, and easily extensible sound editor for Linux
and compatible systems.

These are the development libraries provided by GLAME. You will also
need to install the main lame package in order to install these
libraries.


%prep
%setup


%build
%configure
%{__make}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/install-info %{_infodir}/glame.info.gz %{_infodir}/dir

%preun
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/glame.info.gz %{_infodir}/dir
fi

%post devel
/sbin/install-info %{_infodir}/glame-dev.info.gz %{_infodir}/dir

%preun devel
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/glame-dev.info.gz %{_infodir}/dir
fi


%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING CREDITS ChangeLog NEWS README TODO
%{_bindir}/*
%dir %{_libdir}/glame/
%{_libdir}/glame/*.so*
%{_datadir}/glame/
%{_datadir}/gnome/apps/Multimedia/glame.desktop
%{_infodir}/glame.info*

%files devel
%defattr(-, root, root)
%dir %{_libdir}/glame/
%{_libdir}/glame/*.a
%exclude %{_libdir}/glame/*.la
%{_infodir}/glame-dev.info*


%changelog
* Fri Oct 29 2004 Matthias Saou <http://freshrpms.net/> 1.0.3-1
- Update to 1.0.3.
- Added install-info calls.
- Added fftw, libmad, libvorbis and ladspa support.

* Wed Apr 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.0.

* Tue Jan 29 2002 Matthias Saou <http://freshrpms.net/>
- Updated to 0.6.1.

* Sun Dec 30 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.6.0.

* Mon Dec 10 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.5.4.
- Added the locale files.

* Thu Nov  8 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.5.3.
- No more files in %{_libdir} directly.

* Tue Jul 17 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.5.2.

* Mon May  7 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.
- Split with a -devel package.
- Put the desktop entry in the %files (why wasn't it there?).

* Thu May 03 2001 Daniel Kobras <kobras@linux.de> 0.4.1-1
- Merge with Mandrake's spec file for GLAME 0.4.0.
- Compile with low-latency enabled.
- Don't use mp3lame support in packages.

