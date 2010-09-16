Summary: GUI test tool and automation framework
Name: dogtail
Version: 0.7.0
Release: %mkrel 2
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
