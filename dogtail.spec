Summary: GUI test tool and automation framework
Name: dogtail
Version: 0.7.0
Release: %mkrel 4
License: GPLv2
Group: System/X11
URL: https://fedorahosted.org/dogtail/
Source0: https://fedorahosted.org/released/dogtail/%{name}-%{version}.tar.gz
Patch0: dogtail-0.6.1-desktop-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: imagemagick
BuildArch: noarch
%py_requires -d
Requires: python-rpm
Requires: python-at-spi
Requires: python-imaging
Requires: pygtk2.0-libglade
Requires: gnome-python

%description
GUI test tool and automation framework that uses Accessibility (a11y) 
technologies to communicate with desktop applications.

%prep
%setup -q
%patch0 -p0

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install -O2 --root=$RPM_BUILD_ROOT 

rm -fr $RPM_BUILD_ROOT%{_datadir}/doc/dogtail

mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -resize 16x16 icons/dogtail-head-48.png %buildroot%{_iconsdir}/hicolor/16x16/apps/dogtail-head.png
convert -resize 32x32 icons/dogtail-head-48.png %buildroot%{_iconsdir}/hicolor/32x32/apps/dogtail-head.png
convert -resize 48x48 icons/dogtail-head-48.png %buildroot%{_iconsdir}/hicolor/48x48/apps/dogtail-head.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files 
%defattr(-,root,root,-)
%doc COPYING examples NEWS
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/dogtail
%{py_puresitedir}/dogtail
%{py_puresitedir}/*.egg-info
%{_iconsdir}/hicolor/*/apps/*


%changelog
* Tue Nov 01 2011 Götz Waschk <waschk@mandriva.org> 0.7.0-4mdv2012.0
+ Revision: 708917
- rebuild

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.7.0-3mdv2011.0
+ Revision: 590790
- rebuild for py2.7

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 0.7.0-2mdv2011.0
+ Revision: 578913
- fix deps

* Thu Apr 08 2010 Frederic Crozat <fcrozat@mandriva.com> 0.7.0-1mdv2010.1
+ Revision: 533094
- Release 0.7.0
- fix url

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0.6.1-6mdv2009.1
+ Revision: 324197
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6.1-5mdv2009.0
+ Revision: 244450
- rebuild

* Wed Jul 23 2008 Frederic Crozat <fcrozat@mandriva.com> 0.6.1-4mdv2009.0
+ Revision: 243053
- Add missing dependencies on python-spi and python-rpm

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 26 2007 Frederic Crozat <fcrozat@mandriva.com> 0.6.1-3mdv2008.1
+ Revision: 112145
- Fix typo in post script (Mdv bug #35754)

* Fri Nov 23 2007 Thierry Vignaud <tv@mandriva.org> 0.6.1-2mdv2008.1
+ Revision: 111633
- fix require

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2008.1
+ Revision: 100941
- add icons
- fix desktop file
- New version 0.6.1


* Mon Dec 11 2006 Michael Scherer <misc@mandriva.org> 0.6.0-1mdv2007.0
+ Revision: 95085
- update to 0.6.0

* Wed Dec 06 2006 Michael Scherer <misc@mandriva.org> 0.5.1-4mdv2007.1
+ Revision: 91509
- fix BuildRequires
- rebuild for new python
- use macro and include the .egg-info file
- Import dogtail

